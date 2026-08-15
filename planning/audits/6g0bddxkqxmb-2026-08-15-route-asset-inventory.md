---
schema: 1
id: 6g0bddxkqxmb
bucket: open
area: route-asset-inventory
date: "2026-08-15"
---
# Audit: route-asset-inventory — 2026-08-15

## Scope and method

This audit compares the deployed site at https://andyes.ch with the repository at commit fd1dc30. Evidence came from Chrome at its normal desktop viewport and at 375 by 812 pixels, direct HTTP status checks, repository references and history, exact file hashes, and local byte counts. No site code, routes, DNS, or deployment settings were changed.

## Route inventory

| Route | Current result | Source or history | Proposed disposition |
|---|---|---|---|
| `/` | 200; current homepage | `index.html` | **Preserve** as the canonical homepage. |
| `/index.html` | 200; same homepage | `index.html` | **Preserve as a compatibility alias** and declare `/` canonical unless the selected host can safely redirect it. |
| `/presentations.html` | 200; current talks archive | `presentations.html` | **Preserve through migration.** Owner chooses whether this remains canonical or redirects to a clearer final talks/archive route. |
| `/presentations/` | 404 | Historical permalink in `presentations.md.old` | **Add a compatibility alias or redirect** to the final talks archive. |
| `/projects/` | 404 | Intended permalink in `projects.md` and linked from `index.md.old` | **Replace/restore** with selected work plus an archive under the content plan. |
| `/projects.html` | 404 | Linked by dormant `404.md` | **Redirect or alias** to the restored projects route if compatibility is retained. |
| `/404.html` | 404 with the generic GitHub Pages body | Intended custom page in `404.md` | **Replace** with a generated custom 404 that still returns a 404 response for unknown routes. |
| `/bacher/` | 200; legacy personal page | `bacher/index.html` at audit time | **Remove.** The owner approved retirement with no redirect or tombstone; the source was removed on 2026-08-15 and the route will disappear at the next deployment. |
| `/teaching/` | 404 | Linked from `index.md.old` | **Owner decision:** likely redirect to the homepage teaching section rather than restore a standalone page. |
| `/talks.html` and `/talks/` | 404 | Older deleted `talks.md` history | **Remove from the supported contract** unless analytics or owner knowledge shows meaningful inbound links. |

The apex domain, `www` host, HTTP URLs, and the `andy-esch.github.io` origin all ultimately reach `https://andyes.ch/`. HTTPS works. Repository and DNS verification settings still require the later domain-hardening task because they are not observable from site content alone.

## Source-only routes currently exposed

The root artifact publishes source files rather than only browser-ready output. Representative confirmed 200 responses include:

- `/projects.md`
- `/README.md`
- `/_data/talks.js`
- `/_layouts/default.html`
- `/assets/css/style.scss`
- `/planning/epics/01-unify-the-site-foundation.md`
- `/planning/tasks/6g0b8nxr5jvd-audit-published-routes-and-assets.md`
- `/.tskflwctl.toml`

These files are already in a public repository, so this is not currently a secret disclosure. They should nevertheless be **removed from the deploy artifact** to create a clear publication boundary, avoid accidental future exposure, and prevent source files from becoming crawlable site routes.

## Source-of-truth inventory

### Active hand-written site

- `index.html`: homepage.
- `presentations.html`: hard-coded talks archive with 19 entries.
- `css/index.css`: all active custom CSS.
- `assets/Archivo-Regular.ttf` and `assets/Archivo-Bold.ttf`: active fonts.
- `assets/icon-email.svg`, `assets/icon-github.svg`, and `assets/icon-linkedin.svg`: active icons.
- `bacher/index.html`: independently styled legacy route.
- `CNAME` and `.github/workflows/static.yml`: domain marker and deploy workflow.

### Dormant Jekyll path

- `projects.md` and `404.md` declare layouts and permalinks but are never built.
- `_layouts/default.html`, `_sass/`, `_includes/`, and `assets/css/style.scss` form the older Jekyll theme.
- `_data/talks.js` and `_data/workshops.json` are not consumed by the active HTML. The talks file uses JavaScript export syntax rather than the earlier Jekyll JSON source.
- `assets/fonts/Noto-Sans-*/`, `assets/img/`, and `assets/js/scale.fix.js` support only the dormant path.
- `index.md.old` and `presentations.md.old` are historical backups, not build inputs.
- No `_config.yml`, `Gemfile`, package manifest, lockfile, or other current site build manifest exists. Git history shows those Jekyll build files were deliberately removed when the hand-written pages took over.
- The README still describes the site as a modified Jekyll Minimal theme, which no longer describes production.

## Asset and dependency inventory

The non-planning working files occupy about 2.0 MiB; `assets/` accounts for about 1.8 MiB.

| Group | Approximate size | Current use |
|---|---:|---|
| Eight Archivo TTF variants | 756.1 KiB | Only Regular and Bold, totaling 190.7 KiB, load on active pages. |
| Legacy Noto font formats | 477.7 KiB | Dormant Jekyll stylesheet only. |
| Project/profile images | 482.9 KiB | Dormant projects/layout path; not reachable through a working project page. |
| Active local stylesheet | 1.4 KiB | Loaded by homepage and talks page. |
| Active email/GitHub/LinkedIn SVGs | 2.0 KiB | Loaded through CSS-generated content. |
| Exact duplicate include/asset files | 10 pairs | Duplicate footer, figure, icon HTML, and icon SVG copies under `_includes/` and `assets/`. |

Chrome observed eight homepage assets: two stylesheets, one script, two fonts, and three icons. The external Bootstrap 5.0.0-beta2 stylesheet is 153.4 KiB uncompressed; the bundle script is also loaded even though the page exposes no interactive Bootstrap component. Both active pages depend on jsDelivr and carry SRI attributes. The custom CSS loads raw TTF fonts rather than smaller WOFF2 files.

The CSS also references a Twitter icon that is not rendered. Six Archivo variants, all Noto formats, all project images, and the duplicate include/asset set are unused by the active site.

## External runtime and delivery dependencies

- Browser runtime: jsDelivr-hosted Bootstrap 5.0.0-beta2 CSS and bundle JavaScript.
- Local browser assets: Archivo Regular/Bold TTF and three SVG icons.
- Deployment actions: `actions/checkout@v3`, `actions/configure-pages@v2`, `actions/upload-pages-artifact@v3`, and `actions/deploy-pages@v4`.
- Dormant-only runtime references: html5shiv, optional legacy Google Analytics, and `scale.fix.js`; none execute on the current public pages.
- The legacy `/bacher/` page requests an HTTP image from `andy-esch.github.io`; Chrome reports a completed image with natural size 0 by 0, so it is visibly broken.
- Content links to GitHub, LinkedIn, publishers, projects, and conference sites are editorial destinations, not runtime dependencies.

## Responsive and semantic evidence

At the normal 1512 pixel desktop viewport, the homepage container is exactly 840 pixels wide. At a 375 pixel viewport:

- The document scroll width remains 840 pixels, creating 465 pixels of horizontal overflow.
- The name remains 48 pixels and extends beyond the viewport.
- The talks page also remains 840 pixels wide; all 19 floated talk dates land outside the initial 375 pixel viewport.
- The homepage has no `h1`, heading elements, `header`, `nav`, `main`, or `footer` landmarks and contains one empty anchor.
- The talks page has one `h3` but no `h1`.
- `/bacher/` has no language attribute, viewport meta tag, or heading, and its image is broken.

## Decisions requiring owner input

1. **Resolved:** retire `/bacher/` completely, with no archive, redirect, or tombstone. Its only source file was removed on 2026-08-15.
2. Whether the canonical talks URL remains `/presentations.html` for maximum continuity or moves to a cleaner route with compatibility aliases.
3. Whether `/teaching/` had enough historical use to warrant a compatibility redirect.
4. Which dormant projects and embeds deserve restoration versus archival text or removal.
5. Whether any privacy-preserving analytics are wanted; none should be introduced implicitly.

## Findings

#### H1. Repository root is the publication boundary  · **Status:** landed

**File:** .github/workflows/static.yml:35 | **Component:** deployment
**Effort:** M · **Urgency:** soon

The workflow uploads `.` directly. Source-only Markdown, Liquid, SCSS, data, planning, and configuration files are publicly served as site routes. Jekyll content is not transformed, so source exposure and missing generated pages are two sides of the same build-boundary problem.

**Recommendation:** Produce and validate a dedicated browser-ready output directory, then deploy only that directory.

#### H2. Intended projects and custom 404 routes are not built  · **Status:** open

**File:** projects.md:1 | **Component:** routing
**Effort:** M · **Urgency:** soon

`/projects/`, `/projects.html`, and the intended custom `/404.html` do not exist in the artifact. Visitors receive the generic GitHub Pages 404, while `projects.md` is served as Markdown source.

**Recommendation:** Resolve the route contract, generate projects and custom 404 output through the chosen architecture, and add compatibility aliases where approved.

#### H3. Fixed dimensions make both primary pages unusable on phones  · **Status:** landed

**File:** index.html:19 | **Component:** responsive layout
**Effort:** M · **Urgency:** acute

Both primary pages force an 840 pixel inline width and fixed 126 pixel header heights. A 375 pixel viewport has 840 pixels of document width, clipped name text, and talks metadata outside the viewport.

**Recommendation:** Replace fixed dimensions with a mobile-first intrinsic layout and validate the agreed viewport matrix.

#### H4. Production and dormant Jekyll sources have diverged  · **Status:** in-progress

**File:** _layouts/default.html:1 | **Component:** architecture
**Effort:** L · **Urgency:** soon

Headers, contact details, talks, icons, fonts, and styles exist in parallel hand-written and Jekyll-era forms. Ten files are exact duplicates, talks have multiple divergent sources, and the README documents the inactive architecture.

**Recommendation:** Select one source and build path, migrate shared layout/data, verify route equivalence, and only then remove superseded files.

#### H5. Pages ship unnecessary runtime and asset weight  · **Status:** in-progress

**File:** index.html:9 | **Component:** dependencies
**Effort:** M · **Urgency:** eventually

Both pages load an old Bootstrap beta stylesheet and JavaScript bundle without an interactive component. The repository also contains roughly 1.7 MiB of dormant fonts and images plus unused font variants and Twitter assets.

**Recommendation:** Remove Bootstrap if the architecture decision confirms no required behavior, retain only used asset variants, and optimize surviving fonts and images.

#### H6. Public pages lack basic document semantics  · **Status:** in-progress

**File:** index.html:18 | **Component:** accessibility
**Effort:** M · **Urgency:** soon

The homepage has no headings or structural landmarks and includes an empty link. The talks page begins at H3. The legacy page lacks language, viewport, and heading metadata.

**Recommendation:** Add a coherent heading hierarchy, semantic landmarks, meaningful navigation, accessible icon treatment, and keyboard/zoom validation.

#### H7. Legacy bacher route is approved for retirement  · **Status:** landed

**File:** bacher/index.html:1 | **Component:** legacy route
**Effort:** S · **Urgency:** eventually

The deployed route exposes outdated Twitter information and a broken HTTP image. The owner approved complete retirement with no redirect or tombstone, and `bacher/index.html` was removed locally on 2026-08-15. The finding remains open only until a deployment confirms the public route returns 404.

**Recommendation:** Confirm `/bacher/` returns 404 after the next deployment, then close this finding.

## Candidate tasks

All remediation work was already represented in the planning backlog before this audit:

- ✅ [Decide and document the site generation architecture](../tasks/6g0b8t40fpc8-decide-and-document-the-site-generation-architecture.md) — resolved the architecture portion of H1 and H4.
- ✅ [Consolidate shared layouts and structured content](../tasks/6g0b8t482mtm-consolidate-shared-layouts-and-structured-content.md) — resolved the implementation half of H2 and H4.
- ⚠️ [Remove obsolete code assets and runtime dependencies](../tasks/6g0b8t4fpqsy-remove-obsolete-code-assets-and-runtime-dependencies.md) — production runtime cleanup is landed; dormant repository assets remain under H4 and H5.
- ⚠️ [Implement the mobile-first layout and type system](../tasks/6g0b8ycx0ghw-implement-the-mobile-first-layout-and-type-system.md) — the layout fix is landed; the formal acceptance matrix remains.
- ⚠️ [Improve semantic and keyboard accessibility](../tasks/6g0b8ydbcahf-improve-semantic-and-keyboard-accessibility.md) — core semantics are landed; complete validation and remaining refinements under H6.
- ⚠️ [Implement consistent navigation and route recovery](../tasks/6g0b93sv7f7d-implement-consistent-navigation-and-route-recovery.md) — shared navigation is landed; route decisions and the custom 404 remain under H2.
- ✅ [Build and deploy a deterministic site artifact](../tasks/6g0b99x5kres-build-and-deploy-a-deterministic-site-artifact.md) — resolved H1.
- ⏳ [Optimize fonts images and page performance](../tasks/6g0b99xw3kaj-optimize-fonts-images-and-page-performance.md) — resolves the performance portion of H5.
- ⏳ [Verify custom-domain HTTPS privacy and browser hardening](../tasks/6g0b99yaq3sa-verify-custom-domain-https-privacy-and-browser-hardening.md) — verifies the domain/settings observations.

## Post-deployment reconciliation (2026-08-15)

- **H1 — landed:** GitHub Actions now builds the pinned Hugo source into `public/`, validates the generated boundary, uploads only that directory, and deploys it from a separate job. After deployment, representative repository-source URLs such as `/README.md` and `/planning/epics/01-unify-the-site-foundation.md` return 404.
- **H3 — landed:** The deployed Hugo layouts replace the fixed-width document with a fluid small-screen layout while preserving the original 840px desktop composition. Local browser checks at 320px and 375px found exact viewport/document widths, no offscreen elements, and intentionally stacked archive metadata.
- **H4 — in progress:** Hugo is now the sole production build and the active hand-written duplicates were removed. Dormant Jekyll-era sources and duplicate assets remain for the dedicated cleanup task.
- **H5 — in progress:** Production no longer loads Bootstrap or browser JavaScript, and only the required Archivo weights and contact icons are emitted. Unused source assets remain in the repository for the dedicated cleanup and performance tasks.
- **H6 — in progress:** The generated pages now have language and viewport metadata, coherent headings, header/nav/main structure, a skip link, visible focus styling, and decorative icon treatment. Contrast, touch-target, keyboard, zoom, and automated accessibility validation remain outstanding.
- **H7 — landed:** After the successful main-branch deployment, `https://andyes.ch/bacher/` returns 404 as approved.
