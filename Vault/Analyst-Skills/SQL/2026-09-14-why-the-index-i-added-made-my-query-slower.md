---
title: Why the index I added made my query slower
date: '2026-09-14'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/why-the-index-i-added-made-my-query-slower-4ga2
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-13-your-index-only-scan-is-lying-covering-indexes-and-the-visibility-map]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** I added CREATE INDEX ON events (status) on a Friday. By Monday the dashboard query that looks for pending events was slower than before I touched it. The index was not corrupt, the query was not wrong, and nothing had be…

## What’s new and why it matters
I added CREATE INDEX ON events (status) on a Friday. By Monday the dashboard query that looks for pending events was slower than before I touched it. The index was not corrupt, the query was not wrong, and nothing had been deployed in between. The planner had just picked a plan that costs more on this table. The plan changed, not the data status has four values, and pending is most of the rows, especially right after a backlog. Postgres will still reach for an index when the predicate is not selective, because the planner decides from the row estimate in pg_statistic , which is built by sampli…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/why-the-index-i-added-made-my-query-slower-4ga2

## Related notes
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-13-your-index-only-scan-is-lying-covering-indexes-and-the-visibility-map]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
