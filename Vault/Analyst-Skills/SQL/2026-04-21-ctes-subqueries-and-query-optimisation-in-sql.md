---
title: CTEs, Subqueries, and Query Optimisation in SQL
date: '2026-04-21'
source: https://dev.to/wambuijoan/ctes-subqueries-and-query-optimisation-in-sql-3fin
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-04-21-subqueries-and-ctes-in-sql]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** If you have been writing SQL for a while, you have almost certainly run into a moment where a query starts to feel unwieldy. You need to filter based on an aggregation, or you need to reference a result you just computed…

## What’s new and why it matters
If you have been writing SQL for a while, you have almost certainly run into a moment where a query starts to feel unwieldy. You need to filter based on an aggregation, or you need to reference a result you just computed, and suddenly your query is nested three levels deep and impossible to read. That is where CTEs and subqueries come in. Both solve the same core problem: referencing intermediate results within a larger query. But they do it differently, and knowing when to reach for each one will make you a sharper, more deliberate SQL writer. Subqueries A subquery is a query written inside a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wambuijoan/ctes-subqueries-and-query-optimisation-in-sql-3fin

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-04-21-subqueries-and-ctes-in-sql]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-08-understanding-group-by-in-sql]]
