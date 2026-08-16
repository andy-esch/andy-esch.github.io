---
schema: 1
id: 6g0b99xd03m5
status: in-progress
epic: 04-harden-delivery-and-discoverability
description: Upgrade official Pages workflow actions, pin immutable revisions, retain least-privilege permissions, and automate future update proposals.
effort: 3-5 hours
tier: 1
priority: high
autonomy_level: 4
tags: [github-actions, security, dependencies]
created: "2026-08-15"
updated_at: "2026-08-16"
started_at: "2026-08-16"
---
# Update and pin GitHub Actions dependencies

## Objective

Modernize the deployment supply chain and make workflow dependency changes explicit and reviewable.

## Acceptance criteria

- [x] Checkout, Configure Pages, Upload Pages Artifact, and Deploy Pages use supported compatible releases.
- [x] Each action is held at a verified major-version tag, with Renovate proposing upgrades. (Amended 2026-08-16: the original criterion required full-length commit SHAs. The owner scoped that out for this low-stakes static site, matching the `desirelines` precedent.)
- [x] Job and workflow permissions are reduced to the minimum needed for build and deploy responsibilities.
- [ ] Action compatibility, runtime requirements, and artifact-version coupling are verified in an actual workflow run.
- [ ] Dependabot or an equivalent repository-native mechanism proposes future GitHub Actions updates on a reasonable cadence.
- [x] Update documentation explains how to verify and refresh pinned SHAs.

## Out of scope

- Adding unrelated marketplace actions without a justified need.
- Automatically merging dependency updates.

## Related

- Coordinates with "Build and deploy a deterministic site artifact".
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)

## Implementation (2026-08-16)

**Pinning style amended by the owner.** The task originally required full-length
commit SHAs. All four actions were pinned that way and then reverted: the owner
scoped digest pinning out for this low-stakes static site, preferring the
`desirelines` precedent of major-version tags kept current by Renovate. The
verification work still stands — each major tag was resolved through the GitHub
API and confirmed to point at the same commit as its newest release tag, so none
is stale:

| Action | Tag | Newest release | Commit |
|---|---|---|---|
| `actions/checkout` | `v7` | v7.0.1 | `3d3c42e` |
| `actions/setup-node` | `v7` | v7.0.0 | `8207627` |
| `actions/upload-pages-artifact` | `v5` | v5.0.0 | `fc324d3` |
| `actions/deploy-pages` | `v5` | v5.0.0 | `cd2ce8f` |

`actions/configure-pages` is deliberately absent. It exists to inject a Pages
base URL into the build, and `hugo.toml` already sets `baseURL` to the custom
domain, so adding it would introduce a dependency with nothing to do.

Permissions were already least-privilege from the earlier deterministic-artifact
work and are unchanged: workflow-level `contents: read`, with `pages: write` and
`id-token: write` confined to the deploy job. The build job that runs on pull
requests never holds write scope.

`renovate.json` follows the `desirelines` config: `config:recommended`,
`:dependencyDashboard`, and `:semanticCommits`, non-majors grouped per manager,
majors labelled `requires-review`, nothing automerged. Two repo-specific rules
were added. `playwright` and `@axe-core/playwright` are grouped because
`@axe-core/playwright` takes `playwright-core` as a peer dependency and CI
installs the browser via `playwright install`, so runner, browser, and
integration must move in one PR. A custom regex manager tracks `.hugo-version`,
a bare version string no built-in manager reads; the workflow builds its Hugo
download URL from that same file, so one bump moves local and CI together.

The config validates against Renovate 44.30.4 via `renovate-config-validator`.
Two traps were worth recording. `npx` silently reused a cached Renovate 37,
which rejects `managerFilePatterns` (the field that replaced `fileMatch`), so
the version must be pinned explicitly when validating. A full
`--platform=local` dry run could not run at all: Renovate 44 requires Node
`^24.11.0` and this machine is on Node 26. The custom manager was therefore
verified directly instead — the `matchStrings` regex extracts `0.164.0` from
`.hugo-version`, and `extractVersionTemplate` reduces Hugo's `v0.165.0` release
tag to a comparable bare version. Hugo 0.165.0 is already released, so Renovate
has a real bump to propose as soon as it is enabled.

README gained a "Dependency updates" section covering what is tracked, the
grouping rules, how to move a dependency by hand, and the fact that Renovate
must be enabled for this repository in the GitHub App settings before it opens
anything.
