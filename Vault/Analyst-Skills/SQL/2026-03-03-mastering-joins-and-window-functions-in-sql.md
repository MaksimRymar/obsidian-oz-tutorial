---
title: Mastering Joins and Window Functions in SQL
date: '2026-03-03'
source: https://dev.to/rachel_muriuki_c5062dd89a/mastering-joins-and-window-functions-in-sql-e5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-02-joins-and-window-functions-in-sql]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-03-02-expanding-the-dataset-a-comprehensive-guide-to-sql-joins-and-window-functions]]'
- '[[2026-03-01-a-simple-guide-to-joins-and-window-functions]]'
status: unread
---

> **TL;DR:** Joins in SQL Joins allow one to combine rows from two or more tables based a related column. This is important when data is stored across multiple tables. There are several types of joins: a.INNER JOIN -Returns only the…

## What’s new and why it matters
Joins in SQL Joins allow one to combine rows from two or more tables based a related column. This is important when data is stored across multiple tables. There are several types of joins: a.INNER JOIN -Returns only the matching rows from both tables. Syntax SELECT columns FROM table1 INNER JOIN table2 ON table1.common_column = table2.common_column; Example SELECT c.customer_id, c.first_name, o.order_id,o.quantity FROM customers AS C INNER JOIN orders AS O ON c.customer_id = o.customer_id; This displays only customers who have placed an order. b.LEFT JOIN (LEFT OUTER JOIN) -Returns all rows fr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rachel_muriuki_c5062dd89a/mastering-joins-and-window-functions-in-sql-e5

## Related notes
- [[2026-03-01-sql-joins]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-02-joins-and-window-functions-in-sql]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-03-02-expanding-the-dataset-a-comprehensive-guide-to-sql-joins-and-window-functions]]
- [[2026-03-01-a-simple-guide-to-joins-and-window-functions]]
