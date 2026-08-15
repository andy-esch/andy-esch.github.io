---
schema: 1
id: 6g0b8t40fpc8
status: ready-to-start
epic: 01-unify-the-site-foundation
description: Compare viable static-site approaches and record the selected source, build, output, dependency, and URL-preservation strategy.
effort: 4-6 hours
tier: 1
priority: high
autonomy_level: 3
tags: [architecture, decision, jekyll]
created: "2026-08-15"
---
# Decide and document the site generation architecture

## Objective

Choose the smallest maintainable architecture that can provide shared layouts and structured content without compromising the minimal static-site character.

## Acceptance criteria

- [ ] Hand-written static HTML, the existing Jekyll foundation, and at least one reasonable alternative are compared against maintenance, build, dependency, GitHub Pages, and authoring needs.
- [ ] One approach is selected with a clear source directory, generated output, local preview command, and deployment boundary.
- [ ] The decision states whether Bootstrap and production JavaScript remain, with a default preference for removing dependencies that provide no user value.
- [ ] Public URL preservation and migration or rollback expectations are documented.
- [ ] The route and asset audit findings are explicitly addressed.

## Out of scope

- Performing the migration itself.
- Choosing a visual redesign.

## Related

- Depends on completion of "Audit published routes and assets".
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)