---
schema: 1
id: 6g0b8ycm10ps
status: ready-to-start
epic: 02-responsive-and-accessible-experience
description: Capture current layout, overflow, keyboard, semantics, contrast, and automated accessibility behavior across representative viewports.
effort: 4-6 hours
tier: 1
priority: high
autonomy_level: 4
tags: [audit, responsive, accessibility]
created: "2026-08-15"
---
# Establish the responsive and accessibility baseline

## Objective

Turn the observed mobile awkwardness into a reproducible baseline and an explicit acceptance matrix for the redesign.

## Acceptance criteria

- [ ] Homepage, talks, projects, and 404 are reviewed at representative widths including 320, 375, 768, 1024, and 1440 pixels.
- [ ] Horizontal overflow, clipping, fixed-height collisions, long text, date layout, embed behavior, and touch-target problems are recorded with evidence.
- [ ] Keyboard navigation, focus visibility, landmark and heading structure, link naming, icon alternatives, and color contrast are assessed.
- [ ] Automated accessibility and performance baseline results are captured with tool versions.
- [ ] A concise must-pass browser, viewport, and accessibility matrix is agreed for later validation.

## Out of scope

- Fixing issues during the baseline.
- Expanding the site content.

## Related

- Can begin while the site architecture is being decided, then must be refreshed against the consolidated build.
- Epic [02-responsive-and-accessible-experience](../epics/02-responsive-and-accessible-experience.md)