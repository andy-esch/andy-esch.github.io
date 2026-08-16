# Archive

Retired files kept for possible reuse. Nothing here is read by Hugo, shipped to
browsers, or deployed — `scripts/check-site.sh` fails the build if `archive/`
ever appears in the generated artifact.

**Paths are preserved.** Every file sits at the relative path it originally
occupied, so restoring one is a single move with no mapping to look up:

```sh
git mv archive/assets/img/me-small.jpg assets/img/me-small.jpg
```

Archived 2026-08-16, when the Hugo migration's dormant Jekyll-era sources were
cleared out. The generated artifact was byte-for-byte identical before and after,
confirming nothing here was reachable from the built site.

## Contents

| Path | What it is |
| --- | --- |
| `_includes/`, `_layouts/`, `_sass/` | The Jekyll Minimal theme customizations that predate the Hugo migration. The closest record of the site's earlier visual language. |
| `_data/workshops.json` | Workshop metadata never consumed by the Hugo build. Not to be confused with `data/talks.json`, which is live. |
| `assets/css/style.scss` | Jekyll theme stylesheet entry point, superseded by `assets/css/site.css`. |
| `assets/js/scale.fix.js` | Viewport-manipulation script from the Jekyll theme. Obsolete — the Hugo layouts set a proper `<meta name="viewport">`. |
| `assets/img/` | Original images: a headshot, a FOSS4G Seoul 2015 talk photo, and two PECAN project diagrams. Personal originals, not re-downloadable. |
| `assets/*.html`, `assets/icon-twitter.svg` | Jekyll include wrappers and the Twitter icon, dropped when the header's contact links were revised. |
| `index.md.old`, `presentations.md.old` | Pre-migration page sources, kept as historical backups. |
| `projects.md`, `404.md` | **Live decision inputs, not just history.** See below. |

## `projects.md` and `404.md` are still needed

These two are dead as build inputs but are the only surviving record of the
intended `/projects/` and `/404.html` permalinks. Both are open questions in:

- Audit finding **H2** — "Intended projects and custom 404 routes are not built"
  ([route-asset-inventory](../planning/audits/6g0bddxkqxmb-2026-08-15-route-asset-inventory.md))
- [Define the audience and portfolio information architecture](../planning/tasks/6g0b93rybhjx-define-the-audience-and-portfolio-information-architecture.md),
  whose route-hierarchy criterion has to resolve them
- [Implement consistent navigation and route recovery](../planning/tasks/6g0b93sv7f7d-implement-consistent-navigation-and-route-recovery.md)

Do not delete them until that route contract is settled.

## Deleted rather than archived

Two font sets were removed outright because they are freely re-downloadable and
carry no project-specific work:

- `assets/fonts/Noto-Sans-*/` — Noto Sans web fonts belonging to the retired
  Jekyll theme, in five formats each (~536K).
- Six unused Archivo weights — BoldItalic, Italic, Medium, MediumItalic,
  SemiBold, SemiBoldItalic (~588K). The site ships only Regular and Bold, both
  still in `assets/`, licensed by `assets/OFL.txt`.
