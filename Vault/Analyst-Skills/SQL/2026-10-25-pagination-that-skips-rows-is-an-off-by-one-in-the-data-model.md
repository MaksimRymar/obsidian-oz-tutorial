---
title: Pagination That Skips Rows Is an Off-by-One in the Data Model
date: '2026-10-25'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/pagination-that-skips-rows-is-an-off-by-one-in-the-data-model-48af
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-20-offset-vs-cursor-pagination-why-limitoffset-breaks-at-scale-and-what-to-use-instead]]'
status: unread
---

> **TL;DR:** A customer exported their transaction history and got 4,127 rows. The database said 4,203. Nobody could reproduce it, because the export had paginated through a table that was being written to at the time. OFFSET is a co…

## What’s new and why it matters
A customer exported their transaction history and got 4,127 rows. The database said 4,203. Nobody could reproduce it, because the export had paginated through a table that was being written to at the time. OFFSET is a count, not a position SELECT * FROM transactions WHERE account_id = $ 1 ORDER BY created_at DESC LIMIT 100 OFFSET 2000 ; OFFSET 2000 means "skip the first 2000 rows of a result I am computing right now". If three rows were inserted at the top between page 20 and page 21, every subsequent page shifts by three and the reader never sees three rows. Delete three instead and three row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/pagination-that-skips-rows-is-an-off-by-one-in-the-data-model-48af

## Related notes
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-20-offset-vs-cursor-pagination-why-limitoffset-breaks-at-scale-and-what-to-use-instead]]
