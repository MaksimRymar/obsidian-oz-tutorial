---
title: 'The NOT IN trap: why your SQL query returns zero rows'
date: '2026-09-29'
source: https://dev.to/sharefun2023/the-not-in-trap-why-your-sql-query-returns-zero-rows-2b56
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-06-when-sql-has-nothing-to-say-understanding-nulls]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
status: unread
---

> **TL;DR:** A query that returns an empty result is usually a wrong WHERE clause. But there is one class of empty result that confuses even experienced people, because every row it filters on looks correct: NOT IN with a NULL in the…

## What’s new and why it matters
A query that returns an empty result is usually a wrong WHERE clause. But there is one class of empty result that confuses even experienced people, because every row it filters on looks correct: NOT IN with a NULL in the subquery. The failure Two tables. Customers, and the orders they placed: CREATE TABLE customers ( id int , name text ); CREATE TABLE orders ( customer_id int ); INSERT INTO customers VALUES ( 1 , 'Ada' ), ( 2 , 'Grace' ), ( 3 , 'Linus' ); INSERT INTO orders VALUES ( 1 ), ( NULL ); Customer 3 has never ordered. So this should return Linus: SELECT name FROM customers WHERE id NO…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sharefun2023/the-not-in-trap-why-your-sql-query-returns-zero-rows-2b56

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-06-when-sql-has-nothing-to-say-understanding-nulls]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
