---
schema: 1
id: 6g0b99x5kres
status: completed
epic: 04-harden-delivery-and-discoverability
description: Produce the site into a dedicated output directory and configure GitHub Pages to publish only validated generated files.
effort: 4-8 hours
tier: 1
priority: high
autonomy_level: 4
tags: [build, deployment, github-pages]
created: "2026-08-15"
updated_at: "2026-08-15"
completed_at: "2026-08-15"
---
# Build and deploy a deterministic site artifact

## Objective

Replace whole-repository upload with a reproducible build whose artifact contains exactly the files intended for public delivery.

## Acceptance criteria

- [x] A documented clean build produces a dedicated output directory from authoritative sources.
- [x] The artifact contains the homepage, currently approved routes, required assets, and custom-domain behavior, but excludes planning files, source-only files, and repository metadata; the custom 404 remains owned by the navigation and route-recovery task.
- [x] GitHub Pages configuration publishes only that artifact and reports the deployed URL.
- [x] Build and deploy responsibilities are separated so deployment cannot occur after a failed build or validation.
- [x] Local output can be served and compared with production route behavior.
- [x] A fresh GitHub Actions environment reproduces the artifact without uncommitted files.

## Out of scope

- Migrating to another host.
- Introducing a server-side runtime.
- Updating page design or copy.

## Related

- Depends on the selected site generation architecture.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)

## Implementation and verification (2026-08-15)

- The workflow installs Hugo 0.164.0 from `.hugo-version`, builds into ignored `public/`, validates the output boundary, uploads only `public/`, and makes deployment depend on the successful build job.
- The generated artifact preserves `/`, `/presentations.html`, and `CNAME`; it contains the fingerprinted stylesheet, two active Archivo font files, and three contact icons while excluding planning and dormant source files.
- Local production builds and `scripts/check-site.sh` passed, and both approved routes were served for desktop and narrow-screen comparison.
- Main-branch GitHub Actions runs `31899799327` (migration merge) and `31900023956` (follow-up content merge) both completed successfully and deployed the site.
- Post-deployment checks returned 200 for `/` and `/presentations.html`, and 404 for `/bacher/`, `/README.md`, `/projects.md`, and representative planning paths.
