---
title: SQL Joins & Window Functions
date: '2026-03-11'
source: https://dev.to/philip_weit_e7b1cffd983b2/sql-joins-window-functions-1428
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-09-understanding-sqljoins-window-functions]]'
- '[[2026-03-06-joins-and-window-functions-in-sql]]'
- '[[2026-03-06-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** JOINS They allow us to work with multiple tables and allows us to join data in different tables. Joins happen when there's is a primary and foreign keys-they allow us to reference from our tables uniquely. There are diff…

## What’s new and why it matters
JOINS They allow us to work with multiple tables and allows us to join data in different tables. Joins happen when there's is a primary and foreign keys-they allow us to reference from our tables uniquely. There are diff types of joins. Below briefly explains the most common ones. Inner Join -Returns only the rows that have matching values in both tables. select * from sales s inner join products p on s.product_id = p.product_id That's generally the syntax for joins across the diff types of joins. The first tables(sales) is the left table and the other the right - this part will be important w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_weit_e7b1cffd983b2/sql-joins-window-functions-1428

## Related notes
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-01-sql-joins]]
- [[2026-03-09-understanding-sqljoins-window-functions]]
- [[2026-03-06-joins-and-window-functions-in-sql]]
- [[2026-03-06-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
