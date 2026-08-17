---
schema: 1
id: 6g0b99y3cpr8
status: completed
epic: 04-harden-delivery-and-discoverability
description: Provide complete titles, descriptions, canonical URLs, link-preview metadata, icons, structured data, sitemap, and crawler guidance.
effort: 4-8 hours
tier: 2
priority: medium
autonomy_level: 3
tags: [seo, metadata, sharing]
created: "2026-08-15"
started_at: "2026-08-17"
updated_at: "2026-08-17"
completed_at: "2026-08-17"
---
# Add metadata and discovery surfaces

## Objective

Ensure each public page is described accurately when indexed, bookmarked, or shared without turning the site into an SEO-heavy product.

## Acceptance criteria

- [x] Every indexable page has a unique descriptive title and meta description derived from authoritative content.
- [x] Canonical URLs use the approved HTTPS custom domain and respect the final route contract.
- [x] Open Graph and relevant social-card metadata produce a useful preview with an approved image or intentional text-only fallback.
- [x] Favicon and application icon assets cover common modern browser needs without unnecessary variants.
- [x] Valid Person structured data represents only factual approved identity, role, and profile destinations.
- [x] Sitemap and robots guidance. (Resolved 2026-08-17: sitemap declined by the owner — two routes make it pointless and it would need rewriting once the H2 route contract settles, so `disableKinds` keeps it off. `static/robots.txt` was added as an AI-crawler opt-out at the owner's request.)
- [x] Metadata output is validated on representative pages.

## Out of scope

- Keyword stuffing, ranking guarantees, or paid search work.
- Adding analytics or user tracking.
- Inventing a personal logo solely for metadata.

## Related

- Depends on final routes and approved homepage positioning.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)

## Implementation (2026-08-17)

Titles, descriptions, and canonicals already existed and were correct; the work
was the missing surfaces plus a check so none of it can silently regress.

**Favicon.** `static/favicon.svg` is an "AE" mark in the site gold (`#dec367`)
with dark letters, matching the header band rather than gold-on-dark because it
stays legible at 16px. The glyphs are Archivo Bold **outlines, not text** — SVG
favicons render in a context where webfonts are not guaranteed — extracted from
`assets/Archivo-Bold.woff2` with fontTools and flipped to SVG's y-down axis.
`static/apple-touch-icon.png` (180px) was rasterised from the same source. No
legacy `.ico`. `theme-color` set to the same gold.

**Social cards are text-only** by owner decision: `twitter:card` is `summary`
rather than `summary_large_image` and there is no `og:image`, since the site
ships no raster images.

**Person structured data** on the home page only, so the identity is asserted
once. Owner-approved facts: name, `Staff Machine Learning Engineer`, `worksFor`
Ethyca (ethyca.com), and `sameAs` GitHub and LinkedIn. **Email is deliberately
omitted** — it is already on the page as selectable text, and repeating it in
JSON-LD would make it trivially machine-harvestable, which runs against
replacing the `mailto:` with a copy button.

Canonicals derive from Hugo's `.Permalink`, so they track whatever the H2 route
contract becomes without further edits.

**Validation.** `scripts/check_generated_site.py` now asserts every page has a
non-empty `description`, `og:title`, `og:description`, `og:url`, and
`twitter:card`, plus `<link rel=canonical>` and `<link rel=icon>`, and that any
`application/ld+json` block parses. Mutation-tested: removing `og:url`, removing
the canonical, and corrupting the JSON-LD each fail with a precise message. Two
unit tests were added for the new assertions, and the existing fixture was
extended — it initially failed because it referenced `/favicon.svg` without
creating it, which was the reference checker working correctly.

## robots.txt (2026-08-17)

Added `static/robots.txt` as an AI-crawler opt-out. It distinguishes training
crawlers from AI search crawlers: training bots (GPTBot, ClaudeBot,
anthropic-ai, CCBot, Google-Extended, Applebot-Extended, meta-externalagent,
Bytespider, Omgilibot, omgili, Diffbot, cohere-ai, ImagesiftBot, Timpibot) are
disallowed because they send no traffic back, while AI search crawlers
(OAI-SearchBot, Claude-SearchBot, Claude-User, PerplexityBot, YouBot) stay
allowed because they cite the site with a link — blocking them would cut against
a portfolio site being found. Those are listed commented-out for a one-step
full opt-out. `Google-Extended` and `Applebot-Extended` are training-only
signals, so this does not affect Google Search, Siri, or Spotlight.

Verified with Python `urllib.robotparser` against the built file: Googlebot and
Bingbot can fetch `/`, every training crawler cannot, and the AI search
crawlers can. robots.txt is voluntary and the file says so.
