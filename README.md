# andyes.ch

Personal website of Andy Eschbacher: <https://andyes.ch>

The site is generated with the Hugo version pinned in `.hugo-version`. It
intentionally has no theme, browser JavaScript, or Ruby dependency, and the
published pages ship no JavaScript. Node is a development-only dependency used
by the quality gates; nothing in `public/` needs it.

Install the pinned standard Hugo binary with Go if it is not already available:

```sh
go install github.com/gohugoio/hugo@v$(cat .hugo-version)
```

Preview locally:

```sh
hugo server
```

## Validating the artifact

Install the pinned check dependencies once, then build and validate the exact
GitHub Pages artifact:

```sh
npm ci
npx playwright install --only-shell chromium

hugo build --gc --minify
bash scripts/check-site.sh
```

`scripts/check-site.sh` is the whole gate and runs these checks in order:

| Check | Command | Covers |
| --- | --- | --- |
| Boundary | inline in `scripts/check-site.sh` | Expected routes, no source or JavaScript leaking into output, no unsafe HTML in `data/talks.json` |
| Structure and links | `python3 scripts/check_generated_site.py public` | Document structure, duplicate IDs and attributes, local links, fragments, and HTML/CSS resource targets |
| HTML specification | `npx html-validate "public/**/*.html"` | HTML5 conformance and WCAG markup rules, configured in `.htmlvalidate.json` |
| CSS specification | `node scripts/check_stylesheets.mjs public` | Unknown properties and invalid values, checked against the W3C/MDN value definitions |
| Accessibility and overflow | `node scripts/check_browser.mjs public` | axe-core WCAG 2.0/2.1 A and AA on every route at 320px, 768px, and 1280px, plus a no-horizontal-overflow assertion |

Every check is offline. External URLs are deliberately reported but not
requested, so an unrelated third-party outage cannot block a deployment.

The browser check discovers routes from the built artifact instead of a
hard-coded list, so a new page template is covered as soon as it is built.
`.htmlvalidate.json` disables only formatting rules that `hugo --minify` legally
controls — attribute quoting, doctype case, void-element and boolean-attribute
style, trailing whitespace — and `no-raw-characters` runs in its relaxed mode so
that a bare `&` fails only when it is genuinely ambiguous, matching the HTML5
parsing rules.

Pull requests run the same build and validation job in GitHub Actions. Only a
successful non-PR run is permitted to deploy that validated artifact to GitHub
Pages.

Only `public/` is deployable. It is generated output and must not be edited or committed.

Retired files live in [`archive/`](archive/) at their original relative paths.
Hugo never reads them and the validation gate fails if they reach the artifact;
see [`archive/README.md`](archive/README.md) for what is kept and why.

## Dependency updates

Renovate proposes updates, matching the setup used in this account's other
repositories. `renovate.json` covers three things:

- **GitHub Actions** in `.github/workflows/static.yml`, held at major-version
  tags rather than commit SHAs. This is a static personal site with no secrets
  in the build, so the review cost of digest pinning is not worth it here.
- **npm devDependencies** for the quality gates. `playwright` and
  `@axe-core/playwright` are grouped into a single PR because the browser
  install and the axe integration have to move together.
- **Hugo**, via a custom manager on `.hugo-version`. That file is a bare version
  string no built-in manager reads, and the workflow builds its download URL
  from the same file, so one bump moves local and CI together.

Non-major updates are grouped per manager; majors arrive as individual PRs
labelled `requires-review`. Nothing automerges. The dependency dashboard issue
lists everything pending.

To move a dependency by hand, edit `.hugo-version` or run `npm update`, then
rebuild and revalidate before committing:

```sh
hugo build --gc --minify
bash scripts/check-site.sh
```

Renovate must be enabled for this repository in the GitHub App's settings before
it will open anything.
