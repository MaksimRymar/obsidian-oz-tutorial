---
title: 'How to Do Pagination Right: Row Comparison, Datatypes, and Index Range Scans'
date: '2026-10-05'
source: https://dev.to/franckpachot/how-to-do-pagination-right-row-comparison-datatypes-and-index-range-scans-4n2g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** OFFSET is simple to implement, but the database still needs to read and discard rows before reaching the requested page. Keyset pagination improves this by beginning after the last row from the previous page. Since diffe…

## What’s new and why it matters
OFFSET is simple to implement, but the database still needs to read and discard rows before reaching the requested page. Keyset pagination improves this by beginning after the last row from the previous page. Since different databases have various query planner optimizations and index access methods, the only way to ensure correctness is to examine the execution plan. The usual example, which I take from Vlad Mihalcea's blog post , orders posts by date and uses the identifier as a unique tie-breaker: ORDER BY created_on DESC , id DESC The next page should begin after the last row, and the most…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/how-to-do-pagination-right-row-comparison-datatypes-and-index-range-scans-4n2g

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
