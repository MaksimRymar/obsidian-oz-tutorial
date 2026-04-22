---
title: Understanding Subqueries vs CTEs in SQL (With Examples)
date: '2026-04-22'
source: https://dev.to/wahuelizabeth/understanding-subqueries-vs-ctes-in-sql-with-examples-4pg0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]'
- '[[2026-04-21-subqueries-and-ctes]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-21-sql-subqueries-vs-ctes-a-guide-to-writing-better-queries]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
status: unread
---

> **TL;DR:** When working with SQL, especially in data analysis, you’ll often need to break down complex queries into manageable pieces. Two powerful tools that help with this are subqueries and Common Table Expressions (CTEs). This…

## What’s new and why it matters
When working with SQL, especially in data analysis, you’ll often need to break down complex queries into manageable pieces. Two powerful tools that help with this are subqueries and Common Table Expressions (CTEs). This article explains what they are, how they differ, and when to use each—using clear examples. What is a Subquery? A subquery is simply a query nested inside another SQL query. It runs first and passes its result to the outer query. Example: SELECT name FROM employees WHERE salary > ( SELECT AVG(salary) FROM employees ); What’s happening here? The inner query calculates the averag…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wahuelizabeth/understanding-subqueries-vs-ctes-in-sql-with-examples-4pg0

## Related notes
- [[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]
- [[2026-04-21-subqueries-and-ctes]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-21-sql-subqueries-vs-ctes-a-guide-to-writing-better-queries]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
