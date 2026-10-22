---
title: WINDOW FUNCTIONS,JOINS,SUBQUERIES AND CTEs
date: '2026-10-21'
source: https://dev.to/ndinda515/window-functionsjoinssubqueries-and-ctes-2ngh
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-sql-joins]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
status: unread
---

> **TL;DR:** WINDOW FUNCTION What is a window Function It is a function that performs calculations across a set of rows related to the current one and returns the result of its computation for each row. Unlike GROUP BY, Window functi…

## What’s new and why it matters
WINDOW FUNCTION What is a window Function It is a function that performs calculations across a set of rows related to the current one and returns the result of its computation for each row. Unlike GROUP BY, Window functions in PostgreSQL do not aggregate values and therefore do not reduce the number of rows in the output dataset. All rows from the input table are present in the output, and computations are attached to the corresponding rows. In other words, you can think of a window function as a computation that for each row requests a value that is the result of some calculation applied to a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ndinda515/window-functionsjoinssubqueries-and-ctes-2ngh

## Related notes
- [[2026-09-09-sql-joins]]
- [[2026-03-01-sql-joins]]
- [[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
