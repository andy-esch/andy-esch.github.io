---
schema: 1
id: 6g0b99y3cpr8
status: ready-to-start
epic: 04-harden-delivery-and-discoverability
description: Provide complete titles, descriptions, canonical URLs, link-preview metadata, icons, structured data, sitemap, and crawler guidance.
effort: 4-8 hours
tier: 2
priority: medium
autonomy_level: 3
tags: [seo, metadata, sharing]
created: "2026-08-15"
---
# Add metadata and discovery surfaces

## Objective

Ensure each public page is described accurately when indexed, bookmarked, or shared without turning the site into an SEO-heavy product.

## Acceptance criteria

- [ ] Every indexable page has a unique descriptive title and meta description derived from authoritative content.
- [ ] Canonical URLs use the approved HTTPS custom domain and respect the final route contract.
- [ ] Open Graph and relevant social-card metadata produce a useful preview with an approved image or intentional text-only fallback.
- [ ] Favicon and application icon assets cover common modern browser needs without unnecessary variants.
- [ ] Valid Person structured data represents only factual approved identity, role, and profile destinations.
- [ ] Sitemap and robots guidance reflect the generated public routes and exclude source or planning paths.
- [ ] Metadata output is validated on representative pages.

## Out of scope

- Keyword stuffing, ranking guarantees, or paid search work.
- Adding analytics or user tracking.
- Inventing a personal logo solely for metadata.

## Related

- Depends on final routes and approved homepage positioning.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)