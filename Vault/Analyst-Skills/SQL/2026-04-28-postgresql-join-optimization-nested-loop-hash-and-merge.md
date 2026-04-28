---
title: 'PostgreSQL Join Optimization: Nested Loop, Hash, and Merge'
date: '2026-04-28'
source: https://dev.to/philip_mcclarence_2ef9475/postgresql-join-optimization-nested-loop-hash-and-merge-1cn9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** PostgreSQL has three join algorithms. The planner picks between them for every join in every query, driven by several things at once: the estimated sizes of the two inputs, whether they arrive already sorted on the join…

## What’s new and why it matters
PostgreSQL has three join algorithms. The planner picks between them for every join in every query, driven by several things at once: the estimated sizes of the two inputs, whether they arrive already sorted on the join key, the type of join (inner vs left/semi/anti), which operators are mergejoinable or hashjoinable , whether a hash table will fit in work_mem , and the cost parameters that weigh I/O against CPU. Get the decision right and a three-way join across millions of rows runs in tens of milliseconds. Get it wrong — usually by encouraging a Nested Loop on two large unsorted inputs — an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/postgresql-join-optimization-nested-loop-hash-and-merge-1cn9

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
