---
title: Five SQL Patterns AI Agents Get Wrong (And How to Fix Them)
date: '2026-05-11'
source: https://dev.to/clawgear/five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them-4053
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
status: unread
---

> **TL;DR:** When AI agents write SQL, they usually write something that works. The problem is "works" is a low bar when you're querying a table with 10 million rows. Here are the patterns we've built into our SQL skill at ClawGear —…

## What’s new and why it matters
When AI agents write SQL, they usually write something that works. The problem is "works" is a low bar when you're querying a table with 10 million rows. Here are the patterns we've built into our SQL skill at ClawGear — the ones that separate queries that work from queries that perform. 1. CTEs over nested subqueries The most common readability problem in agent-written SQL is nesting. Four levels deep, no names, impossible to debug. Instead of: SELECT * FROM ( SELECT u . id , u . email , COALESCE ( o . cnt , 0 ) FROM ( SELECT id , email FROM users WHERE deleted_at IS NULL ) u LEFT JOIN ( SELE…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/clawgear/five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them-4053

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
