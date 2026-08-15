---
schema: 1
id: 6g0b8ydjk0as
status: ready-to-start
epic: 02-responsive-and-accessible-experience
description: Run the agreed device, browser, keyboard, zoom, and automated checks and resolve release-blocking experience regressions.
effort: 4-8 hours
tier: 1
priority: high
autonomy_level: 4
tags: [qa, responsive, accessibility]
created: "2026-08-15"
---
# Validate responsive behavior and accessibility

## Objective

Provide final evidence that the public experience meets the baseline acceptance matrix rather than relying on a single desktop inspection.

## Acceptance criteria

- [ ] All public routes pass the agreed viewport matrix without horizontal document overflow, clipped text, or overlapping regions.
- [ ] Current Chromium, Firefox, and WebKit or representative Safari behavior is checked at desktop and mobile sizes.
- [ ] Keyboard-only navigation, visible focus, 200 percent zoom, and text enlargement checks pass.
- [ ] Automated accessibility checks report no serious or critical violations, with any accepted exception documented.
- [ ] Before and after evidence is retained in the task notes or audit artifact.
- [ ] Any remaining non-blocking issues are converted into explicitly scoped follow-up tasks.

## Out of scope

- Pixel-identical rendering across browsers.
- Expanding scope to unrelated content or branding changes.

## Related

- Depends on completion of the responsive, rich-content, and semantic accessibility implementation tasks.
- Epic [02-responsive-and-accessible-experience](../epics/02-responsive-and-accessible-experience.md)