---
title: The dbt test that would have caught our duplicate orders
date: '2026-10-29'
source: https://dev.to/mira_lund/the-dbt-test-that-would-have-caught-our-duplicate-orders-3oc5
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-14-one-cast-made-a-view-13x-slower-in-postgresql-so-i-benchmarked-mysql-84-against-postgresql-17]]'
status: unread
---

> **TL;DR:** Six weeks of duplicate orders in a revenue dashboard, and the fix was a test we already knew how to write. What happened: our orders source table got a second feed during a migration. Both feeds used the same order id, s…

## What’s new and why it matters
Six weeks of duplicate orders in a revenue dashboard, and the fix was a test we already knew how to write. What happened: our orders source table got a second feed during a migration. Both feeds used the same order id, so joins against order items fanned out and every affected order counted twice. Nobody noticed because the number went up slowly, and up looks like growth. The test that would have caught it on day one is boring: a uniqueness test on order_id in the staging model. Not on the mart, on staging, where the two feeds first meet. We had a uniqueness test on the mart's order_id, and it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mira_lund/the-dbt-test-that-would-have-caught-our-duplicate-orders-3oc5

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-14-one-cast-made-a-view-13x-slower-in-postgresql-so-i-benchmarked-mysql-84-against-postgresql-17]]
