---
title: 9 PostgreSQL fixes that took real queries from ~100 ms to under 1 ms (with
  EXPLAIN output)
date: '2026-11-18'
source: https://dev.to/left_right_fa0ba71ad8ef57/9-postgresql-fixes-that-took-real-queries-from-100-ms-to-under-1-ms-with-explain-output-3mmi
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-11-13-postgres-not-using-your-index-its-counting-pages-not-rows]]'
- '[[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]'
- '[[2026-11-04-postgresql-indexing-cheat-sheet-for-busy-developers]]'
- '[[2026-11-12-stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]'
status: unread
---

> **TL;DR:** Most "slow database" problems I see are not exotic. They are the same handful of patterns: a missing index on a foreign key, a function wrapped around a column, an OFFSET that reads 200,000 rows to show 20. I ran each pa…

## What’s new and why it matters
Most "slow database" problems I see are not exotic. They are the same handful of patterns: a missing index on a foreign key, a function wrapped around a column, an OFFSET that reads 200,000 rows to show 20. I ran each pattern below on a 1,000,000-row orders table in PostgreSQL 16.6, captured EXPLAIN (ANALYZE, BUFFERS) before and after the fix, and kept the numbers as they came out. Your timings will differ — the shape of the plan is what matters. Fix Before After Index the foreign key 67.7 ms 0.10 ms Composite index (equality first, then sort column) 80.0 ms 0.20 ms Expression index for lower(…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/left_right_fa0ba71ad8ef57/9-postgresql-fixes-that-took-real-queries-from-100-ms-to-under-1-ms-with-explain-output-3mmi

## Related notes
- [[2026-11-13-postgres-not-using-your-index-its-counting-pages-not-rows]]
- [[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]
- [[2026-11-04-postgresql-indexing-cheat-sheet-for-busy-developers]]
- [[2026-11-12-stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]
