---
title: Stop Hand-Rolling Full Outer Joins in LINQ. .NET 11 Has FullJoin
date: '2026-10-23'
source: https://dev.to/iamprincejkc/stop-hand-rolling-full-outer-joins-in-linq-net-11-has-fulljoin-d6i
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** TL;DR: In .NET 11, a.FullJoin(b, x => x.Key, y => y.Key) returns every matched pair plus the unmatched rows from both sides, as (Outer, Inner) tuples. Join , LeftJoin , RightJoin , and GroupJoin also get overloads with n…

## What’s new and why it matters
TL;DR: In .NET 11, a.FullJoin(b, x => x.Key, y => y.Key) returns every matched pair plus the unmatched rows from both sides, as (Outer, Inner) tuples. Join , LeftJoin , RightJoin , and GroupJoin also get overloads with no result selector. .NET 11 is at Release Candidate 2 right now: go-live licensed, but not final yet. The join you Google every time You have two lists that should agree and never do. What the system thinks is in stock, and what the stocktake actually counted. You want three answers: what matches, what only the left side has, and what only the right side has. SQL calls that a fu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/iamprincejkc/stop-hand-rolling-full-outer-joins-in-linq-net-11-has-fulljoin-d6i

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
