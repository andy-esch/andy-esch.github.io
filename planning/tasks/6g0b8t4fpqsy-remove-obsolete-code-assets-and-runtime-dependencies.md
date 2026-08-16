---
schema: 1
id: 6g0b8t4fpqsy
status: completed
epic: 01-unify-the-site-foundation
description: Delete superseded site paths and unused assets after migration, and minimize third-party code shipped to browsers.
effort: 4-8 hours
tier: 2
priority: medium
autonomy_level: 4
tags: [cleanup, dependencies, assets]
created: "2026-08-15"
updated_at: "2026-08-16"
started_at: "2026-08-16"
completed_at: "2026-08-16"
---
# Remove obsolete code assets and runtime dependencies

## Objective

Reduce maintenance and supply-chain surface after the consolidated site has demonstrated route and content equivalence.

## Acceptance criteria

- [x] Superseded HTML, Jekyll, include, data, font, icon, script, and stylesheet files identified by the audit are removed or deliberately retained with documentation.
- [x] Bootstrap CSS and JavaScript are removed if present. (Resolved 2026-08-16: not applicable. A case-insensitive search across all HTML, CSS, SCSS, JS, Markdown, and TOML found no Bootstrap in the repository — the only matches are planning documents naming it as a thing to check for. Nothing to remove or upgrade.)
- [x] The obsolete viewport-manipulation script and any unreachable legacy page are removed unless a verified compatibility need exists.
- [x] Each remaining asset is referenced by the built site or documented as intentionally retained.
- [x] Build, internal-link, and visual smoke checks pass after cleanup.

## Out of scope

- Recompressing or redesigning retained images and fonts.
- Removing a public URL without the approved redirect or compatibility treatment.

## Related

- Depends on completion of "Consolidate shared layouts and structured content".
- Epic [01-unify-the-site-foundation](../epics/01-unify-the-site-foundation.md)

## Implementation (2026-08-16)

The owner asked for retired content to be archived rather than deleted, so it can
be resurrected without mining git history. Dormant files moved to `archive/` at
their **original relative paths**, making restoration a single `git mv` with no
mapping document to consult. `archive/README.md` records what each item is.

**Liveness was determined by tracing the build, not by guessing.** Hugo reads
only `hugo.toml`, `content/`, `layouts/`, `data/`, `static/`, and whatever
`assets/` files are pulled in by `resources.Get`. Three traps came out of that
trace:

- `assets/OFL.txt` reads like a stray text file but is the SIL Open Font License
  for Archivo, the family the site actively ships. Retained; removing it would
  have stripped the license from shipped fonts.
- `assets/` was mixed, not disposable: three live icon SVGs beside a dormant
  `icon-twitter.svg`, two live Archivo weights beside six unused ones, and the
  live `site.css` beside the dead Jekyll `style.scss`. Cleanup had to be
  file-level, not directory-level.
- `_data/workshops.json` is dormant while `data/talks.json` is live via
  `hugo.Data.talks` — one letter of directory apart.

**Deleted rather than archived**, per the owner's call: `assets/fonts/Noto-Sans-*`
(536K, retired Jekyll theme) and six unused Archivo weights (588K). Both are
freely re-downloadable under the OFL, so archiving them would only have added
1.1M of recoverable bytes. Personal originals in `assets/img/` — a headshot, a
FOSS4G Seoul 2015 photo, and two PECAN diagrams — were archived instead.

`projects.md` and `404.md` were archived but explicitly flagged as live decision
inputs, not history: they are the only surviving record of the intended
`/projects/` and `/404.html` permalinks that audit finding H2 and the
information-architecture route decision still have to resolve.
`archive/README.md` cross-links all three and says not to delete them until the
route contract is settled.

**Verification.** The generated artifact was hashed before and after: all nine
files are byte-for-byte identical, proving nothing removed was reachable from
the built site. This required installing Hugo 0.165.0 first, since the local
toolchain was still on 0.164.0 after the Renovate bump merged and a mismatched
build would have made the comparison meaningless. The full gate passes, and
`archive` was added to the artifact tripwire list in `scripts/check-site.sh` and
mutation-tested: planting `public/archive/leaked.txt` fails the build as
intended.

`assets/` now contains exactly seven files, six referenced by the build and
`OFL.txt` documented as a required license.
