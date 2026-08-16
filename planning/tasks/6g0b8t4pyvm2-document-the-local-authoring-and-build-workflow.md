---
schema: 1
id: 6g0b8t4pyvm2
status: in-progress
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
---
# Document the local authoring and build workflow

## Objective

Make routine site updates understandable without rediscovering the build architecture or editing generated output.

## Acceptance criteria

- [ ] The README identifies authoritative source directories and generated or ignored output.
- [ ] Prerequisites and copy-pasteable local install, preview, build, and validation commands are documented.
- [ ] Common edits such as biography, selected work, talks, projects, navigation, and metadata point to their source files.
- [ ] Deployment behavior, custom-domain handling, and CI expectations are summarized.
- [ ] Instructions are verified from a clean checkout or equivalent isolated environment.

## Out of scope

- General documentation unrelated to maintaining this site.
- Automating deployment outside the selected GitHub Pages workflow.

## Related

- Depends on the implemented architecture and delivery workflow.
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)