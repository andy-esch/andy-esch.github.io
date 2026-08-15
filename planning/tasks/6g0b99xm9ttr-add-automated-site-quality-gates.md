---
schema: 1
id: 6g0b99xm9ttr
status: ready-to-start
epic: 04-harden-delivery-and-discoverability
description: Run repeatable build, markup, internal-link, accessibility, and smoke checks before changes can produce a deployment artifact.
effort: 1 day
tier: 1
priority: high
autonomy_level: 4
tags: [ci, validation, quality]
created: "2026-08-15"
---
# Add automated site quality gates

## Objective

Catch structural and user-facing regressions in pull requests and deployment runs without making CI dependent on unstable third-party websites.

## Acceptance criteria

- [ ] CI builds the site from a clean checkout for pull requests and relevant main-branch changes.
- [ ] Generated HTML validity, duplicate IDs, missing local resources, and broken internal links fail the check.
- [ ] A documented automated accessibility smoke check covers all primary page templates.
- [ ] CSS or stylesheet validation and a basic no-horizontal-overflow regression check are included where reliable.
- [ ] External-link checks are separated or configured to avoid transient third-party failures blocking every deployment.
- [ ] Deployment consumes the exact artifact that passed the required gates.
- [ ] Local commands reproduce each required check.

## Out of scope

- Replacing manual cross-browser and editorial review.
- Building a large test framework for a small static site.

## Related

- Depends on a deterministic build output.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)