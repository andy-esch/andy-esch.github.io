---
schema: 1
status: active
description: Choose and implement one maintainable static-site architecture, consolidate shared content, and remove obsolete or duplicated code and dependencies.
priority: high
tags: [architecture, maintenance, dependencies]
created: "2026-08-15"
---
# Unify the Site Foundation

**Goal.** Establish one clear source of truth and build path for the site while keeping the production experience small and static.

## Why this is its own epic

The repository currently contains a hand-written static site alongside dormant Jekyll layouts, Markdown pages, data files, and duplicated assets. Resolving that split affects every later design, content, and delivery change and should be completed as an explicit architectural migration.

## Out of scope

- A broad visual redesign or new brand identity.
- Substantive rewriting of portfolio content.
- Server-side features, a CMS, or application-style interactivity.