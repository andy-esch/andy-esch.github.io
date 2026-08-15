from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from check_generated_site import (
    parse_documents,
    validate_references,
    validate_stylesheets,
)


DOCUMENT = """<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <title>Test</title>
  <link rel="canonical" href="https://example.test{route}">
  <link rel="stylesheet" href="/site.css">
</head>
<body><main id="main">{content}</main></body>
</html>
"""


class GeneratedSiteCheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.site_dir = Path(self.temp_dir.name)
        (self.site_dir / "index.html").write_text(
            DOCUMENT.format(
                route="/",
                content='<a href="/other.html#target">Other</a>',
            ),
            encoding="utf-8",
        )
        (self.site_dir / "other.html").write_text(
            DOCUMENT.format(
                route="/other.html",
                content='<h1 id="target">Target</h1>',
            ),
            encoding="utf-8",
        )
        (self.site_dir / "site.css").write_text(
            "body { background-image: url('/asset.svg'); }",
            encoding="utf-8",
        )
        (self.site_dir / "asset.svg").write_text("<svg></svg>", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def validate(self) -> list[str]:
        documents, errors = parse_documents(self.site_dir)
        reference_errors, _ = validate_references(self.site_dir, documents)
        stylesheet_errors, _, _ = validate_stylesheets(self.site_dir)
        return errors + reference_errors + stylesheet_errors

    def test_valid_site_passes(self) -> None:
        self.assertEqual(self.validate(), [])

    def test_duplicate_id_fails(self) -> None:
        index = self.site_dir / "index.html"
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "</main>", '<p id="main">Duplicate</p></main>'
            ),
            encoding="utf-8",
        )
        self.assertTrue(any("duplicate id 'main'" in error for error in self.validate()))

    def test_missing_local_resource_fails(self) -> None:
        (self.site_dir / "asset.svg").unlink()
        self.assertTrue(
            any("missing CSS resource" in error for error in self.validate())
        )

    def test_missing_fragment_fails(self) -> None:
        index = self.site_dir / "index.html"
        index.write_text(
            index.read_text(encoding="utf-8").replace("#target", "#absent"),
            encoding="utf-8",
        )
        self.assertTrue(any("missing fragment #absent" in error for error in self.validate()))

    def test_same_host_absolute_link_is_internal(self) -> None:
        index = self.site_dir / "index.html"
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "/other.html#target", "https://example.test/missing.html"
            ),
            encoding="utf-8",
        )
        self.assertTrue(any("missing local target" in error for error in self.validate()))


if __name__ == "__main__":
    unittest.main()
