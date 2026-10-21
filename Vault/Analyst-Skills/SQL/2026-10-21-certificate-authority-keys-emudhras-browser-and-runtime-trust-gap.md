---
title: 'Certificate authority keys: eMudhra''s browser and runtime trust gap'
date: '2026-10-21'
source: https://dev.to/axrisi/certificate-authority-keys-emudhras-browser-and-runtime-trust-gap-4edc
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]'
- '[[2026-10-19-my-coding-agents-share-a-room-now-what-changed-in-quorus-060]]'
status: unread
---

> **TL;DR:** The eMudhra certificate authority incident has an awkward developer-facing cleanup problem. Browser vendors can block a compromised certificate chain while a deployed application keeps reading an older CA bundle. Eight i…

## What’s new and why it matters
The eMudhra certificate authority incident has an awkward developer-facing cleanup problem. Browser vendors can block a compromised certificate chain while a deployed application keeps reading an older CA bundle. Eight intermediate signing keys were compromised, and your browser's update history cannot tell you which trust material a containerized service has loaded. The place to close the incident is the deployed client's actual validation path. TL;DR Mozilla's incident report identifies eight compromised intermediate signing keys: six for TLS and two for code signing. A compromised intermedi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/axrisi/certificate-authority-keys-emudhras-browser-and-runtime-trust-gap-4edc

## Related notes
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]
- [[2026-10-19-my-coding-agents-share-a-room-now-what-changed-in-quorus-060]]
