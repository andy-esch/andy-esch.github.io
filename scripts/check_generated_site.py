#!/usr/bin/env python3
"""Validate the generated static-site artifact without making network requests."""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urljoin, urlsplit


VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}

REFERENCE_ATTRIBUTES = {
    "a": ("href",),
    "audio": ("src",),
    "form": ("action",),
    "iframe": ("src",),
    "img": ("src",),
    "link": ("href",),
    "object": ("data",),
    "script": ("src",),
    "source": ("src",),
    "video": ("poster", "src"),
}

CSS_URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)


@dataclass(frozen=True)
class Reference:
    source: Path
    line: int
    value: str


@dataclass
class Document:
    path: Path
    route: str
    ids: dict[str, list[int]] = field(default_factory=lambda: defaultdict(list))
    references: list[Reference] = field(default_factory=list)
    canonical_hosts: set[str] = field(default_factory=set)


class GeneratedHTMLParser(HTMLParser):
    """Apply strict structural checks to the HTML emitted by this site."""

    def __init__(self, document: Document) -> None:
        super().__init__(convert_charrefs=True)
        self.document = document
        self.doctype_count = 0
        self.tags: Counter[str] = Counter()
        self.stack: list[tuple[str, int]] = []
        self.errors: list[str] = []
        self.title_parts: list[str] = []
        self._inside_title = False

    def handle_decl(self, decl: str) -> None:
        if decl.strip().lower() == "doctype html":
            self.doctype_count += 1
        else:
            self._error(f"unsupported declaration <!{decl}>")

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        tag = tag.lower()
        line, _ = self.getpos()
        self.tags[tag] += 1

        names = [name.lower() for name, _ in attrs]
        duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
        if duplicates:
            self._error(f"duplicate attribute(s) on <{tag}>: {', '.join(duplicates)}")

        attributes = {name.lower(): value for name, value in attrs}
        element_id = attributes.get("id")
        if element_id is not None:
            if not element_id.strip():
                self._error(f"empty id on <{tag}>")
            else:
                self.document.ids[element_id].append(line)

        for attribute in REFERENCE_ATTRIBUTES.get(tag, ()):
            value = attributes.get(attribute)
            if value:
                self.document.references.append(
                    Reference(source=self.document.path, line=line, value=value)
                )

        if tag == "link" and "canonical" in (attributes.get("rel") or "").split():
            canonical_host = urlsplit(attributes.get("href") or "").hostname
            if canonical_host:
                self.document.canonical_hosts.add(canonical_host.lower())

        if tag == "html" and not attributes.get("lang"):
            self._error("<html> must have a lang attribute")
        if tag == "title":
            self._inside_title = True
        if tag not in VOID_ELEMENTS:
            self.stack.append((tag, line))

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID_ELEMENTS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in VOID_ELEMENTS:
            self._error(f"void element </{tag}> must not have an end tag")
            return
        if not self.stack:
            self._error(f"unexpected closing tag </{tag}>")
            return

        open_tag, open_line = self.stack.pop()
        if open_tag != tag:
            self._error(
                f"closing tag </{tag}> does not match <{open_tag}> opened on line {open_line}"
            )
        if tag == "title":
            self._inside_title = False

    def handle_data(self, data: str) -> None:
        if self._inside_title:
            self.title_parts.append(data)

    def close(self) -> None:
        super().close()
        for tag, line in reversed(self.stack):
            self.errors.append(f"unclosed <{tag}> opened on line {line}")
        self.stack.clear()

        if self.doctype_count != 1:
            self.errors.append(
                f"expected one HTML5 doctype; found {self.doctype_count}"
            )
        for tag in ("html", "head", "body", "title", "main"):
            if self.tags[tag] != 1:
                self.errors.append(f"expected one <{tag}>; found {self.tags[tag]}")
        if not "".join(self.title_parts).strip():
            self.errors.append("<title> must not be empty")

    def _error(self, message: str) -> None:
        line, _ = self.getpos()
        self.errors.append(f"line {line}: {message}")


def route_for(path: Path, site_dir: Path) -> str:
    relative = path.relative_to(site_dir).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return f"/{relative[: -len('index.html')]}"
    return f"/{relative}"


def parse_documents(site_dir: Path) -> tuple[dict[Path, Document], list[str]]:
    site_dir = site_dir.resolve()
    documents: dict[Path, Document] = {}
    errors: list[str] = []

    for path in sorted(site_dir.rglob("*.html")):
        document = Document(path=path, route=route_for(path, site_dir))
        parser = GeneratedHTMLParser(document)
        try:
            parser.feed(path.read_text(encoding="utf-8"))
            parser.close()
        except (OSError, UnicodeError) as error:
            errors.append(f"{path.relative_to(site_dir)}: cannot read as UTF-8: {error}")
            continue

        relative = path.relative_to(site_dir)
        errors.extend(f"{relative}: {message}" for message in parser.errors)
        for element_id, lines in sorted(document.ids.items()):
            if len(lines) > 1:
                errors.append(
                    f"{relative}: duplicate id {element_id!r} on lines "
                    + ", ".join(str(line) for line in lines)
                )
        documents[path.resolve()] = document

    if not documents:
        errors.append("no generated HTML documents found")
    return documents, errors


def local_target(
    site_dir: Path, source_route: str, value: str, local_hosts: set[str] | None = None
) -> tuple[Path | None, str | None, bool]:
    parsed = urlsplit(value)
    local_hosts = local_hosts or set()
    if parsed.scheme.lower() in {"http", "https"} and (
        parsed.hostname or ""
    ).lower() in local_hosts:
        decoded_path = unquote(parsed.path)
    elif parsed.scheme or parsed.netloc:
        return None, None, True
    else:
        decoded_path = unquote(parsed.path)
    if decoded_path:
        joined = urljoin(source_route, decoded_path)
        normalized = posixpath.normpath(urlsplit(joined).path)
    else:
        normalized = source_route

    if not normalized.startswith("/"):
        normalized = f"/{normalized}"
    relative = PurePosixPath(normalized.lstrip("/"))
    if any(part == ".." for part in relative.parts):
        return None, parsed.fragment or None, False

    target = site_dir.joinpath(*relative.parts)
    if normalized.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target.resolve(), unquote(parsed.fragment) or None, False


def validate_references(
    site_dir: Path, documents: dict[Path, Document]
) -> tuple[list[str], int]:
    site_dir = site_dir.resolve()
    errors: list[str] = []
    external_count = 0
    local_hosts = {
        host for document in documents.values() for host in document.canonical_hosts
    }

    for document in documents.values():
        for reference in document.references:
            scheme = urlsplit(reference.value).scheme.lower()
            if scheme in {"javascript", "vbscript"}:
                errors.append(
                    f"{reference.source.relative_to(site_dir)}:{reference.line}: "
                    f"unsafe URL scheme: {reference.value!r}"
                )
                continue
            target, fragment, external = local_target(
                site_dir, document.route, reference.value, local_hosts
            )
            if external:
                external_count += 1
                continue
            relative_source = reference.source.relative_to(site_dir)
            prefix = f"{relative_source}:{reference.line}"
            if target is None or not target.is_relative_to(site_dir.resolve()):
                errors.append(f"{prefix}: local URL escapes the site: {reference.value!r}")
                continue
            if not target.is_file():
                errors.append(f"{prefix}: missing local target: {reference.value!r}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_document = documents.get(target)
                if target_document is None:
                    errors.append(
                        f"{prefix}: HTML target was not validated: {reference.value!r}"
                    )
                elif fragment not in target_document.ids:
                    errors.append(
                        f"{prefix}: missing fragment #{fragment} in "
                        f"{target.relative_to(site_dir)}"
                    )

    return errors, external_count


def validate_stylesheets(site_dir: Path) -> tuple[list[str], int, int]:
    site_dir = site_dir.resolve()
    errors: list[str] = []
    stylesheet_count = 0
    external_count = 0

    for path in sorted(site_dir.rglob("*.css")):
        stylesheet_count += 1
        try:
            css = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{path.relative_to(site_dir)}: cannot read as UTF-8: {error}")
            continue

        for match in CSS_URL.finditer(css):
            value = match.group(2).strip()
            target, _, external = local_target(
                site_dir, route_for(path, site_dir), value
            )
            if external or value.startswith("data:"):
                external_count += 1
                continue
            if target is None or not target.is_relative_to(site_dir.resolve()):
                errors.append(
                    f"{path.relative_to(site_dir)}: CSS URL escapes the site: {value!r}"
                )
            elif not target.is_file():
                errors.append(
                    f"{path.relative_to(site_dir)}: missing CSS resource: {value!r}"
                )

    if not stylesheet_count:
        errors.append("no generated stylesheets found")
    return errors, stylesheet_count, external_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "site_dir",
        nargs="?",
        default="public",
        type=Path,
        help="generated site directory (default: public)",
    )
    args = parser.parse_args()
    site_dir = args.site_dir.resolve()

    if not site_dir.is_dir():
        print(f"generated site directory does not exist: {site_dir}", file=sys.stderr)
        return 1

    documents, errors = parse_documents(site_dir)
    reference_errors, external_html = validate_references(site_dir, documents)
    stylesheet_errors, stylesheet_count, external_css = validate_stylesheets(site_dir)
    errors.extend(reference_errors)
    errors.extend(stylesheet_errors)

    if errors:
        print("generated site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"validated {len(documents)} HTML document(s) and "
        f"{stylesheet_count} stylesheet(s)"
    )
    print(
        f"checked local links, fragments, and resources; skipped "
        f"{external_html + external_css} external URL(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
