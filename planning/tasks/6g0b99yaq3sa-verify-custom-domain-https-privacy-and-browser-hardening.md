---
schema: 1
id: 6g0b99yaq3sa
status: ready-to-start
epic: 04-harden-delivery-and-discoverability
description: Confirm domain ownership and canonical HTTPS behavior, eliminate mixed content, and document practical browser-security limits on GitHub Pages.
effort: 3-5 hours
tier: 2
priority: high
autonomy_level: 2
tags: [domain, https, security, privacy]
created: "2026-08-15"
---
# Verify custom-domain HTTPS privacy and browser hardening

## Objective

Close realistic hardening gaps for a static personal site while clearly separating repository changes from settings or DNS actions that require owner authority.

## Acceptance criteria

- [ ] GitHub custom-domain verification status, DNS health, HTTPS enforcement, and apex or www canonical behavior are checked and documented.
- [ ] Public pages and retained embeds contain no mixed active content or insecure asset requests.
- [ ] Third-party browser runtime code is removed where unnecessary; any retained external resource has an explicit purpose and appropriate integrity or isolation treatment where supported.
- [ ] The site does not add analytics, tracking, forms, or external requests without an explicit privacy decision.
- [ ] Referrer, content-security, framing, and other controls are assessed against what GitHub Pages can actually configure, with unsupported controls not falsely claimed.
- [ ] Required DNS or repository-setting changes are presented for owner approval rather than performed implicitly.

## Out of scope

- Migrating hosting solely to gain configurable response headers.
- Penetration testing server infrastructure operated by GitHub.
- Collecting visitor data.

## Related

- Uses the final deployment artifact, domain, routes, and external embed decisions.
- Epic [04-harden-delivery-and-discoverability](../epics/04-harden-delivery-and-discoverability.md)