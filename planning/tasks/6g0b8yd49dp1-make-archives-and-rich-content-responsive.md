---
schema: 1
id: 6g0b8yd49dp1
status: ready-to-start
epic: 02-responsive-and-accessible-experience
description: Ensure talks, dates, descriptions, code, long URLs, images, and embedded maps remain readable and contained on narrow screens.
effort: 4-8 hours
tier: 2
priority: high
autonomy_level: 4
tags: [responsive, archives, media]
created: "2026-08-15"
updated_at: "2026-08-15"
---
# Make archives and rich content responsive

## Objective

Handle content shapes that stress the general layout so archive and project pages do not regress on phones.

## Acceptance criteria

- [ ] Talk titles, venue metadata, and dates use an intentional narrow-screen arrangement without float collisions.
- [ ] Long URLs, prose, lists, and code blocks wrap or scroll within their content region without widening the page.
- [ ] Images include intrinsic dimensions and scale within their containers.
- [ ] Retained maps or other embeds use a responsive wrapper, descriptive title, and usable fallback link.
- [ ] Archive density remains scannable on both narrow and wide screens.

## Out of scope

- Editorially curating which talks or projects appear.
- Replacing third-party embeds with new applications.

## Related

- Depends on "Implement the mobile-first layout and type system".
- Epic [02-responsive-and-accessible-experience](../epics/02-responsive-and-accessible-experience.md)

## Landed implementation progress (2026-08-15)

The generated presentations archive now stacks venue metadata and dates at the mobile breakpoint, allows long descriptions and destinations to wrap within the content column, and retains a flat, scannable wide-screen layout faithful to the prior site. The two approved routes currently contain no project images, maps, code blocks, or embeds, so those cases remain conditional on later page-inclusion decisions. Keep this task open until the refreshed responsive matrix and cross-browser checks confirm the deployed archive.
