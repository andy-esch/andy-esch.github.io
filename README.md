# andyes.ch

Personal website of Andy Eschbacher: <https://andyes.ch>

A Hugo site with no theme and no browser JavaScript. Node is a development-only
dependency for the quality checks.

## Setup

```sh
go install github.com/gohugoio/hugo@v$(cat .hugo-version)
npm ci
npx playwright install --only-shell chromium
```

## Everyday commands

```sh
hugo server                              # preview at localhost:1313

hugo build --gc --minify                 # build the exact deployable artifact
bash scripts/check-site.sh               # validate it
```

Run both before pushing. CI runs the same two commands.

## What to edit

| To change | Edit |
| --- | --- |
| Homepage bio and sections | `content/_index.md` |
| Presentations page intro | `content/presentations.md` |
| Talks and workshops list | `data/talks.json` |
| Navigation and contact links | `layouts/_partials/site-header.html` |
| Footer | `layouts/_partials/site-footer.html` |
| `<head>`, meta tags, page shell | `layouts/baseof.html` |
| Styles, fonts, colors | `assets/css/site.css` |
| Site title, description, base URL | `hugo.toml` |
| Custom domain | `static/CNAME` |

There is no projects route yet; `archive/projects.md` holds the intended
permalink pending the route decision.

## Layout

| Path | Role |
| --- | --- |
| `content/`, `data/`, `layouts/`, `assets/`, `static/` | Source |
| `public/` | Generated. Never edit or commit. |
| `archive/` | Retired files at their original paths. Not built. |
| `scripts/` | Validation |

## Checks

`scripts/check-site.sh` runs all of these. Each is offline — external URLs are
reported, never requested.

| Check | Command |
| --- | --- |
| Routes, leaked source, unsafe data | inline in `scripts/check-site.sh` |
| Structure, duplicate IDs, local links | `python3 scripts/check_generated_site.py public` |
| HTML5 conformance | `npx html-validate "public/**/*.html"` |
| CSS validity | `node scripts/check_stylesheets.mjs public` |
| axe WCAG 2 A/AA, overflow, fonts, page weight | `node scripts/check_browser.mjs public` |

The browser check loads every route at 320px, 768px, and 1280px, and enforces a
150 KiB per-route budget.

## Deployment

Pushing to `main` builds, validates, then deploys to GitHub Pages. Pull requests
build and validate but do not deploy. Only the artifact that passed the checks
is deployed.

## Dependencies

Renovate opens update PRs for GitHub Actions, npm packages, and the Hugo version
in `.hugo-version`. Majors come as individual PRs labelled `requires-review`;
nothing automerges. See `renovate.json`.

Fonts are committed as WOFF2. To regenerate from a TTF:

```sh
pip install fonttools brotli
python3 -c 'from fontTools.ttLib import TTFont
f = TTFont("Archivo-Regular.ttf"); f.flavor = "woff2"; f.save("assets/Archivo-Regular.woff2")'
```
