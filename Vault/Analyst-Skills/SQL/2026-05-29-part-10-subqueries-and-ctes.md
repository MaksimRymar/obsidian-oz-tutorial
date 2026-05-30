---
title: 'Part 10: Subqueries and CTEs'
date: '2026-05-29'
source: https://dev.to/edriso/part-10-subqueries-and-ctes-lpb
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Part of the "SQL: Zero to Ninja" series, written for junior web developers. Your boss asks: "Show me every user who spent more than the average order." You freeze. To filter by the average, you first need to calculate th…

## What’s new and why it matters
Part of the "SQL: Zero to Ninja" series, written for junior web developers. Your boss asks: "Show me every user who spent more than the average order." You freeze. To filter by the average, you first need to calculate the average. But that is a whole query on its own. Can you put a query inside another query? Yes. That little trick is called a subquery, and it is about to make you dangerous. The idea in one line A subquery is a query inside another query (the inner one runs first and hands its answer to the outer one), and a CTE is just a way to give that inner query a clear name so the whole…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/edriso/part-10-subqueries-and-ctes-lpb

## Related notes
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
