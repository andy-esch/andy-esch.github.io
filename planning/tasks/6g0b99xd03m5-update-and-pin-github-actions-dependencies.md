---
schema: 1
id: 6g0b99xd03m5
status: ready-to-start
epic: 04-harden-delivery-and-discoverability
description: Upgrade official Pages workflow actions, pin immutable revisions, retain least-privilege permissions, and automate future update proposals.
effort: 3-5 hours
tier: 1
priority: high
autonomy_level: 4
tags: [github-actions, security, dependencies]
created: "2026-08-15"
---
# Update and pin GitHub Actions dependencies

## Objective

Modernize the deployment supply chain and make workflow dependency changes explicit and reviewable.

## Acceptance criteria

- [ ] Checkout, Configure Pages, Upload Pages Artifact, and Deploy Pages use supported compatible releases.
- [ ] Each action is pinned to a verified full-length commit SHA with a readable release-version comment.
- [ ] Job and workflow permissions are reduced to the minimum needed for build and deploy responsibilities.
- [ ] Action compatibility, runtime requirements, and artifact-version coupling are verified in an actual workflow run.
- [ ] Dependabot or an equivalent repository-native mechanism proposes future GitHub Actions updates on a reasonable cadence.
- [ ] Update documentation explains how to verify and refresh pinned SHAs.

## Out of scope

- Adding unrelated marketplace actions without a justified need.
- Automatically merging dependency updates.

## Related

- Coordinates with "Build and deploy a deterministic site artifact".
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)