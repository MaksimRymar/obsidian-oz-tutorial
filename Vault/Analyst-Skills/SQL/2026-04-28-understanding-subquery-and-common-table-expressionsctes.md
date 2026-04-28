---
title: Understanding Subquery and Common Table Expressions(CTEs)
date: '2026-04-28'
source: https://dev.to/gabriel_njoroge_5be6652c3/understanding-subquery-and-common-table-expressionsctes-391j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]'
- '[[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]'
- '[[2026-04-21-subqueries-and-ctes]]'
status: unread
---

> **TL;DR:** What is a Subquery? A subquery is simply a select statement written inside another select statement. The inside query runs first and results is handed to outer query for use. Example: Explanation i)First it finds the Ave…

## What’s new and why it matters
What is a Subquery? A subquery is simply a select statement written inside another select statement. The inside query runs first and results is handed to outer query for use. Example: Explanation i)First it finds the Average Score ii)It finds all rows which are greater than the Average score. Types of Subqueries 1. Scalar Subquery It returns a single value It will output the single highest score recorded. 2. List Subquery It returns a column of values. e.g List of IDs. It is used with IN or NOT IN. It will output the names of members who scored above 80. 3. Subquery IN FROM You can place subqu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gabriel_njoroge_5be6652c3/understanding-subquery-and-common-table-expressionsctes-391j

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]
- [[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]
- [[2026-04-21-subqueries-and-ctes]]
