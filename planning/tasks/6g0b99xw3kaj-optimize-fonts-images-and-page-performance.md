---
schema: 1
id: 6g0b99xw3kaj
status: ready-to-start
epic: 04-harden-delivery-and-discoverability
description: Reduce transferred bytes and layout instability through deliberate font formats, image sizing, loading behavior, and lightweight page budgets.
effort: 4-8 hours
tier: 2
priority: medium
autonomy_level: 4
tags: [performance, fonts, images]
created: "2026-08-15"
---
# Optimize fonts images and page performance

## Objective

Keep the minimal site genuinely lightweight, especially on mobile networks, while preserving sufficient visual quality.

## Acceptance criteria

- [ ] Only used font families, weights, and styles are shipped in modern browser formats with an intentional fallback and font-display strategy.
- [ ] Raster images are resized and encoded appropriately for their rendered use, with intrinsic dimensions and responsive sources where beneficial.
- [ ] Below-the-fold media is lazy-loaded and primary visible content is not delayed unnecessarily.
- [ ] Unused Bootstrap, icon, font, and legacy asset payloads are absent from the production artifact.
- [ ] Page weight and core performance measurements are captured for representative mobile and desktop runs.
- [ ] A small performance budget is documented and primary pages meet it or record an explicit exception.

## Out of scope

- Sacrificing meaningful image quality for an arbitrary perfect score.
- Adding a runtime image service or new CDN.

## Related

- Follows asset cleanup and the consolidated responsive layout.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)