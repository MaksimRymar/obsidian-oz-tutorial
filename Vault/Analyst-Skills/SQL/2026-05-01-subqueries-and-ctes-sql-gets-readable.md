---
title: 'Subqueries and CTEs: SQL Gets Readable'
date: '2026-05-01'
source: https://dev.to/yakhilesh/subqueries-and-ctes-sql-gets-readable-3hc7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** You learned joins. You can connect tables. Now you have a problem that requires multiple steps. First find the average salary per department. Then find employees who earn above their department average. One query cannot…

## What’s new and why it matters
You learned joins. You can connect tables. Now you have a problem that requires multiple steps. First find the average salary per department. Then find employees who earn above their department average. One query cannot do this directly because you need the result of one calculation as input to another. Two solutions exist. Subqueries nest one query inside another. CTEs give each step a name and build them sequentially. Both solve the same problem. CTEs do it without making you want to delete your laptop. Subqueries: A Query Inside a Query A subquery is a SELECT statement wrapped in parenthese…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yakhilesh/subqueries-and-ctes-sql-gets-readable-3hc7

## Related notes
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
