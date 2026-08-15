---
schema: 1
id: 6g0b8ycm10ps
status: ready-to-start
epic: 02-responsive-and-accessible-experience
description: Capture the deployed Hugo site's layout, overflow, keyboard, semantics, contrast, and automated accessibility behavior across representative viewports.
effort: 4-6 hours
tier: 1
priority: high
autonomy_level: 4
tags: [audit, responsive, accessibility]
created: "2026-08-15"
updated_at: "2026-08-15"
---
# Establish the responsive and accessibility baseline

## Objective

Turn the deployed Hugo site's responsive and accessibility behavior into a reproducible baseline and an explicit acceptance matrix for measured improvements that preserve the existing visual design.

## Acceptance criteria

- [ ] The currently approved homepage and presentations routes are reviewed at representative widths including 320, 375, 768, 1024, and 1440 pixels; absent future routes are recorded rather than implicitly restored.
- [ ] Horizontal overflow, clipping, fixed-height collisions, long text, date layout, embed behavior, and touch-target problems are recorded with evidence.
- [ ] Keyboard navigation, focus visibility, landmark and heading structure, link naming, icon alternatives, and color contrast are assessed.
- [ ] Automated accessibility and performance baseline results are captured with tool versions.
- [ ] A concise must-pass browser, viewport, and accessibility matrix is agreed for later validation.

## Out of scope

- Fixing issues during the baseline.
- Expanding the site content.
- Redesigning the established visual language.

## Related

- Can begin while the site architecture is being decided, then must be refreshed against the consolidated build.
- Epic [02-responsive-and-accessible-experience](../epics/02-responsive-and-accessible-experience.md)
