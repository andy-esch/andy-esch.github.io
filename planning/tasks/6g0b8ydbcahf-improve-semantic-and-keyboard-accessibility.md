---
schema: 1
id: 6g0b8ydbcahf
status: ready-to-start
epic: 02-responsive-and-accessible-experience
description: Use meaningful HTML, focus behavior, labels, contrast, and target sizing so the site works without a mouse or visual styling.
effort: 4-8 hours
tier: 1
priority: high
autonomy_level: 4
tags: [accessibility, html, keyboard]
created: "2026-08-15"
updated_at: "2026-08-15"
---
# Improve semantic and keyboard accessibility

## Objective

Make the site understandable and operable through document semantics, the keyboard, and common assistive technology.

## Acceptance criteria

- [ ] Pages use one descriptive H1 and coherent heading levels within header, nav, main, sections, and footer landmarks.
- [ ] All links and icon-bearing controls have meaningful accessible names and no empty interactive elements remain.
- [ ] Keyboard focus is visible, ordered logically, and never obscured; touch targets are comfortably sized.
- [ ] Text, links, focus indicators, and section colors meet WCAG 2.2 AA contrast expectations.
- [ ] Zoom to 200 percent and increased text size do not hide content or functionality.
- [ ] Decorative images are ignored appropriately and informative images or embeds have useful alternatives.

## Out of scope

- Claiming formal accessibility certification.
- Adding custom widgets when native HTML provides the behavior.

## Related

- Applies to the consolidated shared layout and responsive components.
- Epic [02-responsive-and-accessible-experience](../epics/02-responsive-and-accessible-experience.md)

## Landed implementation progress (2026-08-15)

The shared Hugo shell now provides language and viewport metadata, one page H1, coherent section headings, header/nav/main structure, a skip link, visible focus styling, named contact and navigation links, and decorative treatment for the contact SVGs beside readable labels. This task remains open for measured contrast and touch-target review, full keyboard traversal, 200 percent zoom/text enlargement, and automated accessibility checks.
