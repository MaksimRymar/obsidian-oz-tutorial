---
title: 'ORA-04068 After a Deploy: The Retry Works. The Package State Is Gone.'
date: '2026-11-18'
source: https://dev.to/uptimearchitect/ora-04068-after-a-deploy-the-retry-works-the-package-state-is-gone-29ah
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
status: unread
---

> **TL;DR:** The release went fine. Every script ran, every package compiled, the smoke test passed. A minute later the application log fills with this: ORA-04068: existing state of packages has been discarded ORA-04061: existing sta…

## What’s new and why it matters
The release went fine. Every script ran, every package compiled, the smoke test passed. A minute later the application log fills with this: ORA-04068: existing state of packages has been discarded ORA-04061: existing state of package body "APP.PRICING" has been invalidated ORA-04065: not executed, altered or dropped package body "APP.PRICING" Then it stops. A few dozen errors, one per connection, and nothing after. Someone opens an incident, someone else suggests rolling back, and by the time anyone looks, the errors are gone. The package isn't broken. It holds state, the deploy threw that sta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/uptimearchitect/ora-04068-after-a-deploy-the-retry-works-the-package-state-is-gone-29ah

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
