---
title: PostgreSQL Subquery and CTE Optimization
date: '2026-04-29'
source: https://dev.to/philip_mcclarence_2ef9475/postgresql-subquery-and-cte-optimization-53f4
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Every SELECT in PostgreSQL is made of smaller SELECT s, even when it doesn't look that way. WHERE col IN (SELECT ...) , WHERE EXISTS (SELECT ...) , (SELECT count(*) FROM ... WHERE ...) in the column list, WITH x AS (SELE…

## What’s new and why it matters
Every SELECT in PostgreSQL is made of smaller SELECT s, even when it doesn't look that way. WHERE col IN (SELECT ...) , WHERE EXISTS (SELECT ...) , (SELECT count(*) FROM ... WHERE ...) in the column list, WITH x AS (SELECT ...) — these look syntactically different but all get rewritten into plan nodes at plan time. Which plan node the planner chooses determines whether your query runs in three milliseconds or three seconds, and the rules are different for each pattern. This is part of the Complete Guide to PostgreSQL SQL Query Analysis & Optimization . Assumes you can read EXPLAIN output and a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/postgresql-subquery-and-cte-optimization-53f4

## Related notes
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
