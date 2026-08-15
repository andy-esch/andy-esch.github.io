---
schema: 1
id: 6g0b8t482mtm
status: ready-to-start
epic: 01-unify-the-site-foundation
description: Migrate public pages to the selected architecture with one shared shell and authoritative structured sources for repeated content.
effort: 1-2 days
tier: 1
priority: high
autonomy_level: 4
tags: [architecture, templates, content-data]
created: "2026-08-15"
---
# Consolidate shared layouts and structured content

## Objective

Implement the selected architecture so public pages share one document shell and repeated talks, projects, navigation, contact, and metadata are maintained in authoritative sources.

## Acceptance criteria

- [ ] Homepage, talks, projects, and 404 output are generated or authored through the selected source path.
- [ ] Shared head, header, navigation, contact, and footer markup exists in one maintainable location.
- [ ] Talks and other repeated collections have one authoritative structured source instead of divergent HTML and data copies.
- [ ] Generated output preserves the approved public URL contract.
- [ ] A clean local build succeeds without hand-editing generated files.

## Out of scope

- Final copywriting and portfolio curation.
- Final responsive and accessibility polish.
- Deleting legacy files before equivalence is verified.

## Related

- Depends on completion of "Decide and document the site generation architecture".
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)