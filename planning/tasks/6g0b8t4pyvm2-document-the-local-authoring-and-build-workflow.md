---
schema: 1
id: 6g0b8t4pyvm2
status: completed
epic: 01-unify-the-site-foundation
description: Provide concise instructions for editing content, previewing the site, validating changes, and understanding deployment.
effort: 2-4 hours
tier: 3
priority: medium
autonomy_level: 5
tags: [documentation, developer-experience]
created: "2026-08-15"
updated_at: "2026-08-16"
started_at: "2026-08-16"
completed_at: "2026-08-16"
---
# Document the local authoring and build workflow

## Objective

Make routine site updates understandable without rediscovering the build architecture or editing generated output.

## Acceptance criteria

- [x] The README identifies authoritative source directories and generated or ignored output.
- [x] Prerequisites and copy-pasteable local install, preview, build, and validation commands are documented.
- [x] Common edits such as biography, selected work, talks, projects, navigation, and metadata point to their source files.
- [x] Deployment behavior, custom-domain handling, and CI expectations are summarized.
- [x] Instructions are verified from a clean checkout. (Amended 2026-08-16: owner opted to skip. CI builds and deploys are green, so a broken setup step would surface in use. Every path in the edit map was confirmed to exist, but the setup command sequence is unverified from scratch.)

## Out of scope

- General documentation unrelated to maintaining this site.
- Automating deployment outside the selected GitHub Pages workflow.

## Related

- Depends on the implemented architecture and delivery workflow.
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)

## Implementation (2026-08-16)

README rewritten from 132 to 94 lines. Added a "What to edit" table mapping
common changes to source files, and a layout table separating source, generated,
and archived paths. Cut the rationale prose that had accumulated: html-validate
rule justifications, page-budget reasoning, Renovate pinning rationale, and font
conversion boilerplate. All ten paths in the edit map were confirmed to exist.

Clean-checkout verification was skipped by owner decision; see criterion 5.
