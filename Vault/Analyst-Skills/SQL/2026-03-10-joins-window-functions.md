---
title: JOINS & WINDOW FUNCTIONS.
date: '2026-03-10'
source: https://dev.to/joseph_nganga_9143225ac6c/joins-window-functions-4k7b
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-03-02-joins-and-window-functions-in-sql]]'
- '[[2026-03-04-learning-how-to-use-windows-sql-functions-and-joins-in-relational-databases]]'
- '[[2026-03-03-mastering-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** Joins are sql clauses that combine two or more tables using a related column that exists between the tables. That way, data that is stored in different tables but is related is retrieved and can be processed and analysed…

## What’s new and why it matters
Joins are sql clauses that combine two or more tables using a related column that exists between the tables. That way, data that is stored in different tables but is related is retrieved and can be processed and analysed to give meaningful results. There are several types of joins as follows: 1. Inner join An inner join returns only rows where there is a match in both tables based on a condition. Consider the following example; consider a transaction table and a customer table. we use; select * from transaction inner join customers on transaction.customer_id = customers.customer_id the custome…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/joseph_nganga_9143225ac6c/joins-window-functions-4k7b

## Related notes
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-01-sql-joins]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-03-02-joins-and-window-functions-in-sql]]
- [[2026-03-04-learning-how-to-use-windows-sql-functions-and-joins-in-relational-databases]]
- [[2026-03-03-mastering-joins-and-window-functions-in-sql]]
