---
title: SQL Subquery and CTEs( Common Table Expressions)
date: '2026-04-21'
source: https://dev.to/nancymikia/sql-subquery-and-ctes-common-table-expressions-45ei
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-20-up-down-or-down-up-understanding-subqueries-and-ctes-in-sql-a-comprehensive-guide]]'
- '[[2026-04-19-understanding-subqueries-and-ctes-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-03-mastering-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** What is a subquery? Subquery is a query nested inside another query statement. It allows the query to be modular which would otherwise require multiple queries to achieve the same result. It runs first and the result is…

## What’s new and why it matters
What is a subquery? Subquery is a query nested inside another query statement. It allows the query to be modular which would otherwise require multiple queries to achieve the same result. It runs first and the result is used as input by another query. When to use it? It is an essential tool when used in the following scenarios: Filtering row data using the results from another query Applying aggregation functions such as SUM or AVG dynamically Simplify queries by breaking them into smaller, readable and maintainable queries instead of using joins or complex external code. Compare data between…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/nancymikia/sql-subquery-and-ctes-common-table-expressions-45ei

## Related notes
- [[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-20-up-down-or-down-up-understanding-subqueries-and-ctes-in-sql-a-comprehensive-guide]]
- [[2026-04-19-understanding-subqueries-and-ctes-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-03-mastering-joins-and-window-functions-in-sql]]
