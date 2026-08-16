---
schema: 1
id: 6g0b99xm9ttr
status: completed
epic: 04-harden-delivery-and-discoverability
description: Run repeatable build, markup, internal-link, accessibility, and smoke checks before changes can produce a deployment artifact.
effort: 1 day
tier: 1
priority: high
autonomy_level: 4
tags: [ci, validation, quality]
created: "2026-08-15"
updated_at: "2026-08-15"
started_at: "2026-08-15"
completed_at: "2026-08-15"
---
# Add automated site quality gates

## Objective

Catch structural and user-facing regressions in pull requests and deployment runs without making CI dependent on unstable third-party websites.

## Acceptance criteria

- [x] CI builds the site from a clean checkout for pull requests and relevant main-branch changes.
- [x] Generated HTML validity, duplicate IDs, missing local resources, and broken internal links fail the check.
- [x] A documented automated accessibility smoke check covers all primary page templates.
- [x] CSS or stylesheet validation and a basic no-horizontal-overflow regression check are included where reliable.
- [x] External-link checks are separated or configured to avoid transient third-party failures blocking every deployment.
- [x] Deployment consumes the exact artifact that passed the required gates.
- [x] Local commands reproduce each required check.

## Out of scope

- Replacing manual cross-browser and editorial review.
- Building a large test framework for a small static site.

## Related

- Depends on a deterministic build output.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)

## Current deployment evidence and first slice (2026-08-15)

Main-branch workflow runs `31899799327` and `31900023956` built and deployed successfully, confirming the production path. PR #9 itself reported no status checks because `.github/workflows/static.yml` currently triggers only on pushes to `main` and manual dispatch. The first implementation slice should add a `pull_request` build trigger, prevent the deploy job from running for pull requests, and make the existing pinned Hugo build plus generated-boundary validation a required pre-merge signal before layering markup, internal-link, accessibility, CSS, and overflow checks.

## First implementation slice (2026-08-15)

The Pages workflow now runs the pinned Hugo build for pull requests and `main`, while Pages write and OIDC permissions plus deployment are confined to the non-PR deploy job. The upload remains after validation, so deployment consumes the artifact that passed the required gates.

`scripts/check_generated_site.py` validates every emitted HTML document with Python standard-library tooling: strict document structure, duplicate attributes and IDs, internal files, same-site absolute and relative links, fragments, and HTML/CSS resource references. It makes no external requests and reports skipped third-party URLs separately. Five mutation-oriented unit tests exercise a valid artifact plus duplicate-ID, missing-fragment, missing-resource, and same-site broken-link failures. `bash scripts/check-site.sh` reproduces the complete gate locally.

Fresh Hugo output passes the combined check (two HTML documents, one stylesheet, and 59 external URLs skipped); the unit tests, workflow YAML parse, shell syntax check, `git diff --check`, and planning lint also pass. Standards-level HTML/CSS validation plus automated browser accessibility and horizontal-overflow coverage remain, so the combined markup and local-reproduction criteria stay open. Dependency metadata/install access was unavailable in this environment, so no unpinned Node dependency or lockfile was improvised.

## Second implementation slice (2026-08-15)

Dependency acquisition works now, so the remaining standards-level and browser
checks landed against a `package-lock.json`. Every version in `package.json` is
an exact pin: `html-validate` 11.6.2, `csstree-validator` 4.0.1, `playwright`
1.62.1, and `@axe-core/playwright` 4.13.0, for 26 packages total. Node is a
development-only dependency; the published pages still ship no JavaScript. The
W3C `vnu` and `css-validator` jars were rejected because this machine has no
Java runtime, which would have broken the local-reproduction criterion.

`.htmlvalidate.json` extends the `recommended`, `document`, and `a11y` presets.
It disables only the formatting rules that `hugo --minify` legally controls
(attribute quoting, doctype case, void-element and boolean-attribute style,
trailing whitespace) and runs `no-raw-characters` in relaxed mode so a bare `&`
fails only when genuinely ambiguous, which matches the HTML5 parsing rules. The
first run surfaced a real defect: `aria-label="Contact"` on the `<address>` in
`layouts/_partials/site-header.html`. `<address>` has no implicit ARIA role, so
the label was never exposed to assistive technology; it was removed rather than
suppressed.

`scripts/check_stylesheets.mjs` validates declarations against the W3C/MDN value
definitions. `scripts/check_browser.mjs` serves the artifact from an ephemeral
local port and loads every discovered route in headless Chromium at 320px,
768px, and 1280px, asserting no axe-core `wcag2a`/`wcag2aa`/`wcag21a`/`wcag21aa`
violations and no horizontal overflow. Routes are discovered from the artifact
rather than hard-coded, so a new template is covered as soon as it is built.
Both remain offline: the server only reads under the site directory and
axe-core is bundled.

Each gate was mutation-tested rather than trusted on a green run. An injected
unknown property, invalid value, and over-long shorthand were all caught by the
CSS check; an injected `<img>` without `alt` was caught by both `html-validate`
(`wcag/h37`) and axe (`image-alt`, critical) at all three viewports; and an
injected 3000px element was caught as horizontal overflow at all three, each
reported with the offending element and its right edge.

`bash scripts/check-site.sh` runs the whole gate in one command and fails with
an actionable message when `node_modules` is absent. Against fresh output it
reports 2 HTML documents, 1 stylesheet, 59 skipped external URLs, HTML5 and CSS
conformance, and 6 clean page loads. The workflow gained pinned
`actions/setup-node@v7`, `npm ci`, and `playwright install --with-deps
--only-shell chromium` ahead of the build; validation still runs before the
artifact upload, so deployment continues to consume only an artifact that
passed every required gate. README now documents each check and its standalone
command.
