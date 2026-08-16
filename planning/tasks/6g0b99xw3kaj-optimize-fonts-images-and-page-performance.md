---
schema: 1
id: 6g0b99xw3kaj
status: completed
epic: 04-harden-delivery-and-discoverability
description: Reduce transferred bytes and layout instability through deliberate font formats, image sizing, loading behavior, and lightweight page budgets.
effort: 4-8 hours
tier: 2
priority: medium
autonomy_level: 4
tags: [performance, fonts, images]
created: "2026-08-15"
updated_at: "2026-08-16"
started_at: "2026-08-16"
completed_at: "2026-08-16"
---
# Optimize fonts images and page performance

## Objective

Keep the minimal site genuinely lightweight, especially on mobile networks, while preserving sufficient visual quality.

## Acceptance criteria

- [x] Only used font families, weights, and styles are shipped in modern browser formats with an intentional fallback and font-display strategy.
- [x] Raster images are resized and encoded appropriately for their rendered use. (Resolved 2026-08-16: not applicable. The artifact ships no raster images at all — the five originals in `assets/img/` were archived during the asset cleanup and no layout references them. The only images served are three SVG icons totalling 2.0 KiB.)
- [x] Below-the-fold media is lazy-loaded and primary visible content is not delayed unnecessarily. (Resolved 2026-08-16: no media to lazy-load. Nothing blocks first paint — the pages ship no JavaScript, and the single stylesheet is 4.0 KiB with `font-display: swap` so text renders immediately in the fallback face.)
- [x] Unused Bootstrap, icon, font, and legacy asset payloads are absent from the production artifact.
- [x] Page weight and core performance measurements are captured for representative mobile and desktop runs.
- [x] A small performance budget is documented and primary pages meet it or record an explicit exception.

## Out of scope

- Sacrificing meaningful image quality for an arbitrary perfect score.
- Adding a runtime image service or new CDN.

## Related

- Follows asset cleanup and the consolidated responsive layout.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)

## Implementation (2026-08-16)

The asset cleanup shrank this task before it started. `assets/img/` was archived
and no layout references an image, so the raster-image and lazy-loading criteria
had nothing to act on; both were resolved as not applicable with evidence rather
than ticked. What remained was fonts and a budget.

**Fonts were 87% of the page.** The artifact served 214.2 KiB, of which 186.3 KiB
was two raw Archivo TTFs. Converting them to WOFF2 with fonttools cut them 63%,
to 69.0 KiB, taking the whole artifact to **97.0 KiB — a 55% reduction** with no
visual change. `font-display: swap` and the
`"Helvetica Neue", Helvetica, Arial, sans-serif` fallback were already in place.
WOFF2 has near-universal support, so the TTFs were dropped rather than retained
as a second format; they are freely available upstream and the README documents
the conversion command. `assets/OFL.txt` still ships, since it licenses the faces.

| | Before | After |
|---|---:|---:|
| Archivo Regular | 92.2 KiB | 34.4 KiB |
| Archivo Bold | 94.1 KiB | 34.7 KiB |
| Whole artifact | 214.2 KiB | 97.0 KiB |

**Two gates were added to `scripts/check_browser.mjs`.** The webfont assertion
exists because a broken font is otherwise invisible: the browser silently falls
back to Helvetica, and every other check — axe, overflow, HTML and CSS
validation — still passes. It now confirms each face reaches the browser, has
`status === "loaded"`, and is usable for rendering at 400 and 700. The
page-weight budget is 150 KiB per route, measured by tallying bytes in the
static server rather than in the browser so the number is deterministic, with a
fresh context per route so no route is scored against a cache the previous one
warmed. Current usage: `/` at 78.9 KiB and `/presentations.html` at 93.3 KiB.

**Two things surfaced during verification.** The font check failed on its first
run and the check was wrong, not the fonts — Chromium normalizes
`FontFace.family` to lowercase, so a case-sensitive comparison matched nothing;
confirmed against a live page reporting `status: "loaded"` and a rendering
difference from a bogus family before fixing the comparison. Separately, an
attempt to test the budget by padding the stylesheet instead demonstrated that
the `<link>` carries an SRI `integrity` hash: Chromium rejected the tampered
sheet outright and no `@font-face` reached the page. The budget was then verified
by lowering the ceiling to 80 KiB, which correctly failed only
`/presentations.html` with both numbers named.

Both new gates were mutation-tested: a corrupted WOFF2 produces
`Archivo 700 failed to load (status: error)` plus a usability failure at every
viewport, and an exceeded budget names the route and both figures.
