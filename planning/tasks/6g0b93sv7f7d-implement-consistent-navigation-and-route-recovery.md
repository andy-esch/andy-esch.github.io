---
schema: 1
id: 6g0b93sv7f7d
status: ready-to-start
epic: 03-refresh-portfolio-content-and-navigation
description: Provide a small shared navigation model, reliable home and archive links, current-page context, and a useful generated 404 page.
effort: 4-6 hours
tier: 2
priority: high
autonomy_level: 4
tags: [navigation, routes, "404"]
created: "2026-08-15"
---
# Implement consistent navigation and route recovery

## Objective

Ensure visitors can move among the homepage, selected work, talks, and other retained pages without dead ends or route confusion.

## Acceptance criteria

- [ ] Shared navigation exposes only the routes approved by the information architecture and appears consistently on public pages.
- [ ] Current-page context is conveyed without relying only on color.
- [ ] Logo or name, archive links, and back-navigation use root-safe URLs that work on the custom domain and local preview.
- [ ] The deployed 404 page uses the shared site shell and offers useful routes back to live content.
- [ ] Approved legacy URLs resolve directly or use the documented compatibility treatment.
- [ ] Navigation remains usable at all accepted viewports and by keyboard.

## Out of scope

- A complex menu or client-side router.
- Preserving accidental repository paths that were never public.

## Related

- Depends on the approved route inventory and information architecture.
- Epic [03-refresh-portfolio-content-and-navigation](../epics/03-refresh-portfolio-content-and-navigation.md)