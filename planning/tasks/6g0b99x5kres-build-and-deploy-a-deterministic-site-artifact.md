---
schema: 1
id: 6g0b99x5kres
status: ready-to-start
epic: 04-harden-delivery-and-discoverability
description: Produce the site into a dedicated output directory and configure GitHub Pages to publish only validated generated files.
effort: 4-8 hours
tier: 1
priority: high
autonomy_level: 4
tags: [build, deployment, github-pages]
created: "2026-08-15"
---
# Build and deploy a deterministic site artifact

## Objective

Replace whole-repository upload with a reproducible build whose artifact contains exactly the files intended for public delivery.

## Acceptance criteria

- [ ] A documented clean build produces a dedicated output directory from authoritative sources.
- [ ] The artifact contains the homepage, approved routes, assets, custom-domain behavior, and generated 404 page, but excludes planning files, source-only files, and repository metadata.
- [ ] GitHub Pages configuration publishes only that artifact and reports the deployed URL.
- [ ] Build and deploy responsibilities are separated so deployment cannot occur after a failed build or validation.
- [ ] Local output can be served and compared with production route behavior.
- [ ] A fresh environment can reproduce the artifact without uncommitted files.

## Out of scope

- Migrating to another host.
- Introducing a server-side runtime.
- Updating page design or copy.

## Related

- Depends on the selected site generation architecture.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)