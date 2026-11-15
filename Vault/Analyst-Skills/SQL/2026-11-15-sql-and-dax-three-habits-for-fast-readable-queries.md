---
title: 'SQL and DAX: three habits for fast, readable queries'
date: '2026-11-15'
source: https://dev.to/jwsolutions/sql-and-dax-three-habits-for-fast-readable-queries-kdi
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-03-22-format-sql-queries-in-seconds-no-extensions-no-installs]]'
- '[[2026-11-07-what-really-happens-after-you-execute-a-sql-query-in-oracle]]'
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-06-07-sql-for-developers-the-practical-guide-2026]]'
- '[[2026-06-03-sql-for-developers-the-practical-guide-2026]]'
status: unread
---

> **TL;DR:** Tip of the week In SQL, select only the columns you need and filter early. In DAX, store intermediate results in variables ( VAR ) so they are evaluated once. SELECT o . id , o . total , c . name FROM orders AS o JOIN cu…

## What’s new and why it matters
Tip of the week In SQL, select only the columns you need and filter early. In DAX, store intermediate results in variables ( VAR ) so they are evaluated once. SELECT o . id , o . total , c . name FROM orders AS o JOIN customers AS c ON c . id = o . customer_id WHERE o . created_at >= DATE '2026-01-01' ORDER BY o . total DESC ; Ventas YTD Margen = VAR Ventas = [Ventas Totales] VAR Costo = [Costo Total] RETURN DIVIDE(Ventas - Costo, Ventas) Quick rules Avoid SELECT * in production. Use DIVIDE in DAX to avoid division-by-zero errors. One measure, one responsibility: compose measures instead of du…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jwsolutions/sql-and-dax-three-habits-for-fast-readable-queries-kdi

## Related notes
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-03-22-format-sql-queries-in-seconds-no-extensions-no-installs]]
- [[2026-11-07-what-really-happens-after-you-execute-a-sql-query-in-oracle]]
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-06-07-sql-for-developers-the-practical-guide-2026]]
- [[2026-06-03-sql-for-developers-the-practical-guide-2026]]
