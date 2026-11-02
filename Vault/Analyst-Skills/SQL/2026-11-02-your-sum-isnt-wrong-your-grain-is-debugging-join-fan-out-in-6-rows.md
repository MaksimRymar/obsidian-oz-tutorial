---
title: 'Your SUM() isn''t wrong, your grain is: debugging JOIN fan-out in 6 rows'
date: '2026-11-02'
source: https://dev.to/alapha888/your-sum-isnt-wrong-your-grain-is-debugging-join-fan-out-in-6-rows-5ch5
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
status: unread
---

> **TL;DR:** A query runs, returns plausible numbers, and revenue is 4× what finance says. No syntax error, no NULLs, no warning. Nine times out of ten it's fan-out : you joined two one-to-many tables onto the same parent and every p…

## What’s new and why it matters
A query runs, returns plausible numbers, and revenue is 4× what finance says. No syntax error, no NULLs, no warning. Nine times out of ten it's fan-out : you joined two one-to-many tables onto the same parent and every parent row got multiplied. Here's the smallest reproduction I know, runnable in SQLite. The data CREATE TABLE orders ( order_id INTEGER PRIMARY KEY , customer TEXT , order_total REAL ); CREATE TABLE order_items ( item_id INTEGER PRIMARY KEY , order_id INTEGER , sku TEXT , qty INTEGER ); CREATE TABLE payments ( payment_id INTEGER PRIMARY KEY , order_id INTEGER , amount REAL ); IN…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alapha888/your-sum-isnt-wrong-your-grain-is-debugging-join-fan-out-in-6-rows-5ch5

## Related notes
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
