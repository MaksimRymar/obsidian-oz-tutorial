---
title: Your database reads pages, not rows
date: '2026-10-21'
source: https://dev.to/ajitkumar_singh_7a94b3eaa/your-database-reads-pages-not-rows-en2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-23-oracle-indexes-when-they-help-when-they-hurt-and-how-to-tell]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** You ask for one 120-byte row. The storage engine reads an 8 KiB page, because that is the smallest unit the disk and the buffer pool exchange. If your row sits alone on that page, you paid 8 KiB for 120 bytes. If the nei…

## What’s new and why it matters
You ask for one 120-byte row. The storage engine reads an 8 KiB page, because that is the smallest unit the disk and the buffer pool exchange. If your row sits alone on that page, you paid 8 KiB for 120 bytes. If the neighbours you also wanted are on it too, you paid 8 KiB for all of them. That ratio is locality, and it is the most useful single lens for reasoning about storage performance. How many rows share a page With nothing else taking space, an 8 KiB page would hold 68 rows of 120 bytes. A PostgreSQL heap page also spends 24 bytes on its page header and, for every row, 4 bytes on a line…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ajitkumar_singh_7a94b3eaa/your-database-reads-pages-not-rows-en2

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-23-oracle-indexes-when-they-help-when-they-hurt-and-how-to-tell]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
