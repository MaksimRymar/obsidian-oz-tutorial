---
title: Database index on generated column to speed up selection on date (for daily
  stats)
date: '2026-09-18'
source: https://dev.to/cyrille37/database-index-on-generated-column-to-speed-up-selection-on-date-for-daily-stats-4phe
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-03-pandas-secret-mini-language]]'
- '[[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]'
- '[[2026-09-14-ddl-and-dml-what-are-they]]'
- '[[2026-05-29-part-11-indexes-and-performance]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
status: unread
---

> **TL;DR:** Hello Database index on generated column to speed up selection on date to easily compile daily statistics: CREATE TABLE logs ( ... `date` DATETIME , -- Generated column for date part (yyy-mm-dd) `date_only` DATE AS ( DAT…

## What’s new and why it matters
Hello Database index on generated column to speed up selection on date to easily compile daily statistics: CREATE TABLE logs ( ... `date` DATETIME , -- Generated column for date part (yyy-mm-dd) `date_only` DATE AS ( DATE ( `date` )) STORED , ... INDEX ( `date_only` ) ); With 10 453 162 rows: date >= “2026-07-08” → 28 secondes date_only >= “2026-07-08” → 2 secondes

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cyrille37/database-index-on-generated-column-to-speed-up-selection-on-date-for-daily-stats-4phe

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-03-pandas-secret-mini-language]]
- [[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]
- [[2026-09-14-ddl-and-dml-what-are-they]]
- [[2026-05-29-part-11-indexes-and-performance]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
