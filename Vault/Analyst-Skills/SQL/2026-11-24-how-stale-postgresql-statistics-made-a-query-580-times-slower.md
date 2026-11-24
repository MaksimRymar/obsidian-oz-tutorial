---
title: How Stale PostgreSQL Statistics Made a Query 580 Times Slower
date: '2026-11-24'
source: https://medium.com/@Anatolii_Zhadan/how-stale-postgresql-statistics-made-a-query-580-times-slower-19696100c0ac?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-27-postgresql-19-vs-18-what-actually-changed-feature-by-feature]]'
- '[[2026-04-27-we-used-mongodb-because-it-scales-at-10m-documents-postgresql-wouldve-been-faster]]'
- '[[2026-10-15-a-600-gb-postgresql-table-has-no-index-how-do-you-find-the-latest-row]]'
- '[[2026-06-19-10-postgresql-tricks-that-made-our-apis-feel-faster]]'
- '[[2026-06-09-why-a-single-where-clause-can-make-a-query-1000x-slower]]'
- '[[2026-07-22-one-index-turned-my-12-second-query-into-40ms-after-2-years-of-suffering]]'
status: unread
---

> **TL;DR:** PostgreSQL 18, like 17, auto-analyzes a table only after 10% of it changes, and a 9.3% backfill left a query on the wrong index. Continue reading on Medium »

## What’s new and why it matters
PostgreSQL 18, like 17, auto-analyzes a table only after 10% of it changes, and a 9.3% backfill left a query on the wrong index. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@Anatolii_Zhadan/how-stale-postgresql-statistics-made-a-query-580-times-slower-19696100c0ac?source=rss------sql-5

## Related notes
- [[2026-07-27-postgresql-19-vs-18-what-actually-changed-feature-by-feature]]
- [[2026-04-27-we-used-mongodb-because-it-scales-at-10m-documents-postgresql-wouldve-been-faster]]
- [[2026-10-15-a-600-gb-postgresql-table-has-no-index-how-do-you-find-the-latest-row]]
- [[2026-06-19-10-postgresql-tricks-that-made-our-apis-feel-faster]]
- [[2026-06-09-why-a-single-where-clause-can-make-a-query-1000x-slower]]
- [[2026-07-22-one-index-turned-my-12-second-query-into-40ms-after-2-years-of-suffering]]
