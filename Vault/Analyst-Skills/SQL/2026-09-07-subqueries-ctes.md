---
title: Subqueries & CTEs
date: '2026-09-07'
source: https://dev.to/emilio_ochieng_632030149c/subqueries-ctes-3jc7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-04-28-understanding-subquery-and-common-table-expressionsctes]]'
- '[[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** What are subqueries? A subquery is a query nested inside another query - it runs first, and its result is used by the outer query, whether that's as a filter condition, a computed value, or a virtual table to select from…

## What’s new and why it matters
What are subqueries? A subquery is a query nested inside another query - it runs first, and its result is used by the outer query, whether that's as a filter condition, a computed value, or a virtual table to select from. Subqueries can appear almost anywhere: inside a WHERE clause, a SELECT list, or a FROM clause. There are a few flavors worth knowing: Scalar subquery - returns a single value, usable anywhere a single value is expected. Row/column subquery - returns a set of values, often used with IN or ANY / ALL . Correlated subquery - references a column from the outer query, so it re-runs…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emilio_ochieng_632030149c/subqueries-ctes-3jc7

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-04-28-understanding-subquery-and-common-table-expressionsctes]]
- [[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
