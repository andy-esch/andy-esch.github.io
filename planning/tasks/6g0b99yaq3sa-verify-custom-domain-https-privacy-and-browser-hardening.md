---
schema: 1
id: 6g0b99yaq3sa
status: completed
epic: 04-harden-delivery-and-discoverability
description: Confirm domain ownership and canonical HTTPS behavior, eliminate mixed content, and document practical browser-security limits on GitHub Pages.
effort: 3-5 hours
tier: 2
priority: high
autonomy_level: 2
tags: [domain, https, security, privacy]
created: "2026-08-15"
updated_at: "2026-08-17"
started_at: "2026-08-17"
completed_at: "2026-08-17"
---
# Verify custom-domain HTTPS privacy and browser hardening

## Objective

Close realistic hardening gaps for a static personal site while clearly separating repository changes from settings or DNS actions that require owner authority.

## Acceptance criteria

- [x] GitHub custom-domain verification status, DNS health, HTTPS enforcement, and apex or www canonical behavior are checked and documented.
- [x] Public pages and retained embeds contain no mixed active content or insecure asset requests.
- [x] Third-party browser runtime code is removed where unnecessary; any retained external resource has an explicit purpose and appropriate integrity or isolation treatment where supported.
- [x] The site does not add analytics, tracking, forms, or external requests without an explicit privacy decision.
- [x] Referrer, content-security, framing, and other controls are assessed against what GitHub Pages can actually configure, with unsupported controls not falsely claimed.
- [x] Required DNS or repository-setting changes are presented for owner approval rather than performed implicitly.

## Out of scope

- Migrating hosting solely to gain configurable response headers.
- Penetration testing server infrastructure operated by GitHub.
- Collecting visitor data.

## Related

- Uses the final deployment artifact, domain, routes, and external embed decisions.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)

## Verification (2026-08-17)

**Domain and HTTPS.** `gh api repos/.../pages` reports `protected_domain_state:
verified`, `https_enforced: true`, `cname: andyes.ch`, `build_type: workflow`,
and a certificate in state `approved` covering `andyes.ch` and `www.andyes.ch`.
Live redirect behaviour, all 301 with the path preserved:

| From | To |
| --- | --- |
| `http://andyes.ch` | `https://andyes.ch/` |
| `https://www.andyes.ch` | `https://andyes.ch/` |
| `https://andy-esch.github.io` | `https://andyes.ch/` |
| `http://andyes.ch/presentations.html` | `https://andyes.ch/presentations.html` |

**No mixed content, because there is no third-party runtime at all.** Every
subresource in the artifact is local: two WOFF2 faces, one stylesheet, three
SVGs. Zero external scripts, stylesheets, fonts, or images. The only absolute
URLs in `<head>` are the canonical links, which are not requests. No analytics,
tracking, forms, or embeds. The one script on the page is ~15 lines inline for
the email copy button and makes no network calls.

**Security headers cannot be set on GitHub Pages and are not claimed.** A live
`HEAD` returns no `strict-transport-security`, `content-security-policy`,
`x-frame-options`, `referrer-policy`, or `x-content-type-options`. Pages serves
static files with no header configuration, so CSP, framing, and referrer
controls are unavailable by hosting choice. Notably HSTS is absent from
responses despite `https_enforced: true`; the redirect chain is the actual
enforcement mechanism. A meta-tag CSP was considered and rejected: it cannot
cover framing or referrer and would add maintenance for no real gain on a site
with no third-party resources.

**No changes required.** Domain verification, HTTPS enforcement, and the
certificate are all already in the desired state, so nothing needed owner
approval.

**Two findings referred elsewhere, not fixed here:**

- Eight talk destinations in `data/talks.json` are `http://` anchors
  (barcampphilly, three FOSS4G sites, two NACIS URLs, cvxopt). Anchors are not
  mixed content, so this is a link-quality issue for
  [Complete the editorial and destination review](../tasks/6g0b93t294wm-complete-the-editorial-and-destination-review.md).
- `custom_404: false` confirms audit finding H2 from the API side.
