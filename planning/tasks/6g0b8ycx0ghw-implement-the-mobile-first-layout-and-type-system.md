---
schema: 1
id: 6g0b8ycx0ghw
status: ready-to-start
epic: 02-responsive-and-accessible-experience
description: Replace fixed dimensions with a fluid page shell, responsive header, readable measure, and scalable typography.
effort: 1-2 days
tier: 1
priority: high
autonomy_level: 4
tags: [css, responsive, typography]
created: "2026-08-15"
updated_at: "2026-08-15"
---
# Implement the mobile-first layout and type system

## Objective

Create a small CSS system that works from narrow screens upward while retaining the existing restrained palette and section-bar character.

## Acceptance criteria

- [ ] No public page relies on a fixed 840 pixel container, fixed header height, or large-screen-only grid behavior.
- [ ] The page shell uses fluid gutters and a readable maximum content width without horizontal document overflow at the accepted viewports.
- [ ] Name, role, contact links, navigation, section headings, and body content reflow intentionally from phone to desktop.
- [ ] Typography and spacing use a documented small scale with comfortable line length and no clipped zoomed text.
- [ ] CSS remains dependency-light and avoids viewport-specific duplication where intrinsic layout is sufficient.

## Out of scope

- Rewriting page content.
- Adding a component framework or JavaScript layout logic.
- Final rich-content and accessibility validation.

## Related

- Depends on the selected shared layout architecture and baseline acceptance matrix.
- Epic [02-responsive-and-accessible-experience](../epics/02-responsive-and-accessible-experience.md)

## Landed implementation progress (2026-08-15)

The Hugo migration deployed a fluid page shell that preserves the original 840px desktop composition while switching to full-width cells and 16px gutters on narrow screens. The name, role, contact icons, navigation, section headings, body copy, and talks metadata reflow without JavaScript. Local Chrome checks at 320px and 375px found exact viewport/document widths and no offscreen elements. This task remains open until the refreshed acceptance matrix covers intermediate widths, zoom/text enlargement, and the final typography/spacing review.
