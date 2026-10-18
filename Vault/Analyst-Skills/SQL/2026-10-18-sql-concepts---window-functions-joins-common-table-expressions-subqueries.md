---
title: SQL CONCEPTS - Window Functions, Joins, Common Table Expressions & Subqueries
date: '2026-10-18'
source: https://dev.to/thegichanga/sql-concepts-window-functions-joins-common-table-expressions-subqueries-n7m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
status: unread
---

> **TL;DR:** 1. SQL Window Functions These are functions that are used to perform calculations. They return one output row per one input row. Examples of Window functions include: ROW_NUMBER (), RANK (), DENSE_RANK (), NTILE (), LAG…

## What’s new and why it matters
1. SQL Window Functions These are functions that are used to perform calculations. They return one output row per one input row. Examples of Window functions include: ROW_NUMBER (), RANK (), DENSE_RANK (), NTILE (), LAG (), LEAD (), FIRST_VALUE (), LAST_VALUE (), SUM (), AVG (), COUNT (), MIN (), and MAX (). ROW NUMBER() It assigns a unique sequential number to each row within an ordered partition, starting at 1. Example:- Row number () over ( [ Partition by column1 , ..] Order by column2 ,...) RANK() It assigns a rank to each row within a result set based on a specified order. When used toget…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thegichanga/sql-concepts-window-functions-joins-common-table-expressions-subqueries-n7m

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-sql-joins]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-03-01-sql-joins]]
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
