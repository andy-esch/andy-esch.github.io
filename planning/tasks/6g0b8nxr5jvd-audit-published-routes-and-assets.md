---
schema: 1
id: 6g0b8nxr5jvd
status: completed
epic: 01-unify-the-site-foundation
description: Inventory public URLs, source files, assets, and external runtime dependencies before consolidating the site.
effort: 4-6 hours
tier: 1
priority: high
autonomy_level: 4
tags: [audit, architecture, routes, assets]
created: "2026-08-15"
started_at: "2026-08-15"
updated_at: "2026-08-15"
completed_at: "2026-08-15"
---
# Audit published routes and assets

## Objective

Establish an evidence-backed inventory of what is published, what is merely present in the repository, and what must be preserved before selecting or implementing a single site architecture.

## Acceptance criteria

- [x] Every intended public route is listed with its current source, observed behavior, and proposed disposition: preserve, redirect, replace, or remove.
- [x] The hand-written HTML path and dormant Jekyll path are mapped, including duplicated content and files that are not part of the deployed experience.
- [x] Local fonts, images, icons, includes, scripts, data files, and external runtime dependencies are inventoried with references and approximate size.
- [x] Existing custom-domain, 404, and deep-link compatibility requirements are recorded.
- [x] Unknown ownership or editorial decisions are called out without silently choosing an outcome.

## Out of scope

- Deleting files or changing published routes.
- Selecting the final generator or build implementation.

## Related

- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)
- Audit [route and asset inventory](../audits/6g0bddxkqxmb-2026-08-15-route-asset-inventory.md)

## Completion notes

- Compared the deployed site with commit `fd1dc30` using Chrome desktop/mobile rendering, direct HTTP status checks, repository history, reference searches, hashes, and byte counts.
- Recorded ten candidate public routes, representative source-only routes, the active and dormant source paths, asset/runtime inventories, five owner decisions, and seven actionable findings.
- Confirmed that the existing backlog already contains tasks covering every remediation finding; no additional task was required by this audit.
