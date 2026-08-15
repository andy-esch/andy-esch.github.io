---
schema: 1
id: 6g0b8t482mtm
status: completed
epic: 01-unify-the-site-foundation
description: Establish Hugo around the homepage and presentations route with one shared shell, curated talk data, and a safe generated-output boundary.
effort: 1-2 days
tier: 1
priority: high
autonomy_level: 4
tags: [architecture, templates, content-data]
created: "2026-08-15"
updated_at: "2026-08-15"
started_at: "2026-08-15"
completed_at: "2026-08-15"
---
# Consolidate shared layouts and structured content

## Objective

Establish the selected Hugo architecture around the two approved first-wave routes so the homepage and presentations page share one document shell and curated talks, navigation, contact, and metadata have authoritative sources.

## Acceptance criteria

- [x] A minimal, version-pinned Hugo project generates `/` and `/presentations.html`; no other dormant content route is revived implicitly.
- [x] Shared head, header, navigation, contact, and footer markup exists in one maintainable location.
- [x] Included talks have one curated Hugo-supported structured source instead of divergent JavaScript data and hand-generated HTML copies.
- [x] Generated output preserves `/` and `/presentations.html`, excludes `/bacher/`, and contains no planning or source-only repository files.
- [x] `hugo server` previews the site locally and a clean pinned production build succeeds without hand-editing `public/`.

## Out of scope

- Final copywriting and portfolio curation.
- Restoring projects, teaching, a custom 404, or any other dormant route before its page-level inclusion decision.
- Final responsive and accessibility polish.
- Deleting legacy files before equivalence is verified.

## Related

- Depends on completion of "Decide and document the site generation architecture".
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)

## Implementation and verification (2026-08-15)

- Pinned Hugo 0.164.0 in `.hugo-version` and added a theme-free `hugo.toml` that disables RSS, sitemap, taxonomy, and term output.
- Added Markdown/metadata sources for only the homepage and `/presentations.html`, a shared base shell with header/navigation/contact/footer partials, a responsive handcrafted stylesheet, and one JSON source for 20 preserved talk records.
- Kept Hugo's default content security policy. The landing page is Markdown; the small set of source-controlled legacy description fragments was audited against an executable-HTML denylist before explicit safe rendering.
- Replaced the repository-root Pages upload with a pinned Hugo build, generated-boundary validation, and `public/`-only artifact deployment. The artifact contains exactly two HTML files, one fingerprinted stylesheet, and `CNAME`.
- After route/content equivalence was verified, removed the superseded root `index.html`, `presentations.html`, `_data/talks.js`, `css/index.css`, and root `CNAME`. Dormant Jekyll/projects content remains excluded and untouched for later page-level decisions.
- Validation passed with warnings promoted to errors, valid 20-record JSON, workflow YAML parsing, planning lint, shellcheck, and `git diff --check`. Chrome verification covered desktop, 375px, and 320px viewports; both routes had exact viewport/document widths, correct heading/navigation state, all talks present, and no offscreen elements at 320px.
