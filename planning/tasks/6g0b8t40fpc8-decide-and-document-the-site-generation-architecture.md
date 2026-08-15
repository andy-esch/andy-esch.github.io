---
schema: 1
id: 6g0b8t40fpc8
status: completed
epic: 01-unify-the-site-foundation
description: Compare viable static-site approaches and record the selected source, build, output, dependency, and URL-preservation strategy.
effort: 4-6 hours
tier: 1
priority: high
autonomy_level: 3
tags: [architecture, decision, jekyll]
created: "2026-08-15"
updated_at: "2026-08-15"
started_at: "2026-08-15"
completed_at: "2026-08-15"
---
# Decide and document the site generation architecture

## Objective

Choose the smallest maintainable architecture that can provide shared layouts and structured content without compromising the minimal static-site character.

## Acceptance criteria

- [x] Hand-written static HTML, the existing Jekyll foundation, and at least one reasonable alternative are compared against maintenance, build, dependency, GitHub Pages, and authoring needs.
- [x] One approach is selected with a clear source directory, generated output, local preview command, and deployment boundary.
- [x] The decision states whether Bootstrap and production JavaScript remain, with a default preference for removing dependencies that provide no user value.
- [x] Public URL preservation and migration or rollback expectations are documented.
- [x] The route and asset audit findings are explicitly addressed.

## Out of scope

- Performing the migration itself.
- Choosing a visual redesign.

## Related

- Depends on completion of "Audit published routes and assets".
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)

## Working comparison (2026-08-15)

| Approach | Maintenance and dependencies | Authoring fit | GitHub Pages fit | Assessment |
| --- | --- | --- | --- | --- |
| Hand-written HTML/CSS, no build | No toolchain, but shared chrome and structured talks/projects must be duplicated or maintained manually. | Familiar and transparent; increasingly awkward as shared pages return. | Native static upload, but the current root upload also publishes source-only and planning files. | Viable only if zero tooling matters more than shared layouts and structured content. |
| Jekyll | Ruby, RubyGems, Bundler, compiler prerequisites, Gemfile, and lock/version policy. | Strong Markdown, Liquid, layouts, data, and permalink support. | First-class Pages history and official build support. | Valid, but adopting it would be a fresh reintroduction: the repository's working Ruby/Jekyll toolchain was deliberately removed and the surviving files are dormant fragments. |
| Eleventy | One local Node development dependency plus package and lock files; no client runtime required. | Processes HTML, Markdown, Liquid, Nunjucks, and data; well matched to gradual extraction from the current pages. | Build in Actions, validate, and upload only the generated directory through the generator-neutral Pages workflow. | The smallest JavaScript-based option, but less attractive once the owner's preference for a Go-oriented toolchain is included. |
| Astro | Node toolchain with file-based pages, components, content collections, static output, and opt-in client islands. | Excellent if the site grows into a component-rich or interactive portfolio. | Official GitHub Pages action and static output deployment. | Good future-facing option, but more architecture than these few mostly textual pages currently need. |
| Hugo | One pinned Hugo binary, Go templates, Markdown/data content, and generated `public/` output; no browser runtime or package manager is required for this scope. | Requires a small template/data translation, but aligns with the owner's Go preference and supports an intentionally small two-page site. | Official Actions deployment path. | Recommended after owner discussion: its main migration cost is bounded by excluding dormant content by default. |

Primary sources consulted: [Jekyll quickstart](https://jekyllrb.com/docs/), [Eleventy getting started](https://www.11ty.dev/docs/), [Astro static rendering](https://docs.astro.build/en/basics/rendering-modes/), [Hugo quickstart](https://gohugo.io/getting-started/quick-start/), and [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Decision

- **Selected by the owner on 2026-08-15:** Use Hugo as a build-time-only generator, with no third-party theme and no Hugo Modules initially. Pin the Hugo binary version in automation and document the matching local version.
- Use Hugo's conventional `content/`, `layouts/`, `data/`, `assets/`, and `static/` source directories; reserve `public/` for disposable generated output and do not commit it.
- Use `hugo server` for local preview and `hugo build --gc --minify` for production.
- In GitHub Actions, install the pinned Hugo version, build and validate `public/`, and upload only `public/` to Pages. This replaces the unsafe repository-root publication boundary.
- Keep the browser output as plain semantic HTML and custom CSS. Remove Bootstrap and ship no production JavaScript unless a later feature demonstrates a user-facing need.
- Limit the first migration to `/` and `/presentations.html`. Set the presentations page's explicit Hugo URL to `/presentations.html` so inbound links remain unchanged.
- Treat every other dormant or historical page as excluded by default. Add it only after an explicit page-by-page content decision; migration is not evidence that stale content should survive.
- Convert the talks source from JavaScript to a supported Hugo data format only after curating it. Existing description strings containing HTML must be rewritten as structured/Markdown content or individually reviewed before any explicit safe-HTML rendering.
- Make rollback a deployment of the last known-good static artifact/commit.
- Retire `/bacher/` with no redirect or tombstone, as approved by the owner on 2026-08-15.

## Audit disposition

- H1: replace repository-root publication with validated `public/`-only deployment.
- H2: do not implicitly revive projects or other dormant routes; decide them page by page. A custom 404 remains a separate explicit inclusion decision.
- H3 and H6: preserve responsibility for responsive layout and semantics in their dedicated implementation tasks.
- H4: make Hugo sources authoritative and treat all Jekyll-era and hand-generated duplicates as migration inputs only.
- H5: remove Bootstrap and retain no production JavaScript without a demonstrated feature need.
- H7: retire `/bacher/` completely, as already approved and removed locally.

The implementation migration remains out of scope for this completed decision task.
