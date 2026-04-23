---
title: 'Subqueries vs CTEs: When, Why, How.'
date: '2026-04-22'
source: https://dev.to/abdiomari/subqueries-vs-ctes-when-why-how-jj
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-04-21-sql-subqueries-vs-ctes-a-guide-to-writing-better-queries]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-04-22-subqueries-vs-ctes-in-sql-a-practical-guide-for-data-analysts]]'
status: unread
---

> **TL;DR:** With a background in Python programming, Learning SQL started feeling like a step back, every line is independent of the next and so far nothing seemed interconnected or Programming-like, until I hit a wall: Picture this…

## What’s new and why it matters
With a background in Python programming, Learning SQL started feeling like a step back, every line is independent of the next and so far nothing seemed interconnected or Programming-like, until I hit a wall: Picture this : You have a table employees and you need to find employees who earn more than the average salary of their own department, not the company average. This Problem requires two queries, one to get the average salary of each department and another to find the employee whose salary is above that average. Such a problem requires thinking like a programmer and the solution is either…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/abdiomari/subqueries-vs-ctes-when-why-how-jj

## Related notes
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-04-21-sql-subqueries-vs-ctes-a-guide-to-writing-better-queries]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-04-22-subqueries-vs-ctes-in-sql-a-practical-guide-for-data-analysts]]
