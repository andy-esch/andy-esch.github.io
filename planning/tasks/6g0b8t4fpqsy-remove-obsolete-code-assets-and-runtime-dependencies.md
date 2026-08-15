---
schema: 1
id: 6g0b8t4fpqsy
status: ready-to-start
epic: 01-unify-the-site-foundation
description: Delete superseded site paths and unused assets after migration, and minimize third-party code shipped to browsers.
effort: 4-8 hours
tier: 2
priority: medium
autonomy_level: 4
tags: [cleanup, dependencies, assets]
created: "2026-08-15"
---
# Remove obsolete code assets and runtime dependencies

## Objective

Reduce maintenance and supply-chain surface after the consolidated site has demonstrated route and content equivalence.

## Acceptance criteria

- [ ] Superseded HTML, Jekyll, include, data, font, icon, script, and stylesheet files identified by the audit are removed or deliberately retained with documentation.
- [ ] Bootstrap CSS and JavaScript are removed if the architecture decision confirms they provide no required behavior; otherwise they are upgraded and centrally managed.
- [ ] The obsolete viewport-manipulation script and any unreachable legacy page are removed unless a verified compatibility need exists.
- [ ] Each remaining asset is referenced by the built site or documented as intentionally retained.
- [ ] Build, internal-link, and visual smoke checks pass after cleanup.

## Out of scope

- Recompressing or redesigning retained images and fonts.
- Removing a public URL without the approved redirect or compatibility treatment.

## Related

- Depends on completion of "Consolidate shared layouts and structured content".
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)