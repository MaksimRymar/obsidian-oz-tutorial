---
title: One Null in the Subquery and Your NOT IN Returned Nothing
date: '2026-10-16'
source: https://dev.to/sergueyasaelshinder/one-null-in-the-subquery-and-your-not-in-returned-nothing-lih
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-20-not-in-returned-zero-rows-it-wasnt-your-data-it-was-one-null]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** Marketing wanted a list. Every customer who had never placed an order. The query was short and read like English. Select from customers where id is not in the customer ids from orders. It had worked for two years. On Mon…

## What’s new and why it matters
Marketing wanted a list. Every customer who had never placed an order. The query was short and read like English. Select from customers where id is not in the customer ids from orders. It had worked for two years. On Monday it returned zero rows. Not fewer. Zero. Nobody had deleted a customer. Nobody had touched the query. What changed was one row in orders. The week before, the shop started taking guest checkouts, and a guest order has no customer id. The column holds a null. That was enough. Here is the mechanism. NOT IN is shorthand for a chain of comparisons. The id is not one, and it is n…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sergueyasaelshinder/one-null-in-the-subquery-and-your-not-in-returned-nothing-lih

## Related notes
- [[2026-07-20-not-in-returned-zero-rows-it-wasnt-your-data-it-was-one-null]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
