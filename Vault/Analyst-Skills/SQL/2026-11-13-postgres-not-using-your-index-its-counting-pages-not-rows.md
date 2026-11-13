---
title: Postgres not using your index? It's counting pages, not rows
date: '2026-11-13'
source: https://dev.to/immunefomo/postgres-not-using-your-index-its-counting-pages-not-rows-k4g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]'
- '[[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
- '[[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
status: unread
---

> **TL;DR:** Slow Postgres, part 1 of 8. The SQL and raw numbers for every test are on GitHub . A Seq Scan reads each page once, in order. An index lookup walks the B-tree and then reads one heap page per TID. You add an index on sta…

## What’s new and why it matters
Slow Postgres, part 1 of 8. The SQL and raw numbers for every test are on GitHub . A Seq Scan reads each page once, in order. An index lookup walks the B-tree and then reads one heap page per TID. You add an index on status , run EXPLAIN , and Postgres reads the whole table anyway. ANALYZE doesn't change the plan. Someone suggests SET enable_seqscan = off , the plan finally shows your index, and the query gets slower. Usually the planner is right. It prices a plan by the 8 KB pages it has to read and by whether it reads them in order or jumps around between them, and once you count pages the s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/immunefomo/postgres-not-using-your-index-its-counting-pages-not-rows-k4g

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]
- [[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
- [[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
