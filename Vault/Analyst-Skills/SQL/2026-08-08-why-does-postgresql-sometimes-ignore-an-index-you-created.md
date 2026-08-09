---
title: Why does PostgreSQL sometimes ignore an index you created?
date: '2026-08-08'
source: https://dev.to/codewithmaz/why-does-postgresql-sometimes-ignore-an-index-you-created-6pa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** Why does PostgreSQL sometimes ignore an index you created? A common assumption is: “If a column has an index, PostgreSQL should use it.” But PostgreSQL does not work that way. An index is only one possible access path. B…

## What’s new and why it matters
Why does PostgreSQL sometimes ignore an index you created? A common assumption is: “If a column has an index, PostgreSQL should use it.” But PostgreSQL does not work that way. An index is only one possible access path. Before executing a query, PostgreSQL's query planner estimates the cost of different plans and chooses the one it believes will be cheapest. That might be: • Sequential Scan • Index Scan • Index Only Scan • Bitmap Index Scan • Parallel Sequential Scan So sometimes PostgreSQL sees your perfectly valid index and deliberately decides: “Scanning the table is cheaper.” Consider this…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codewithmaz/why-does-postgresql-sometimes-ignore-an-index-you-created-6pa

## Related notes
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-26-alter-table]]
- [[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]
- [[2026-03-08-understanding-group-by-in-sql]]
