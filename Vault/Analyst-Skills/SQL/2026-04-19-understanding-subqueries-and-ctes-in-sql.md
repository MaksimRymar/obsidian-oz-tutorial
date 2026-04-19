---
title: Understanding Subqueries and CTEs in SQL
date: '2026-04-19'
source: https://dev.to/tom_chege/understanding-subqueries-and-ctes-in-sql-12c5
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-10-write-your-sql-like-a-pro-mastering-common-table-expressions-ctes]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-11-sql-joins-window-functions]]'
status: unread
---

> **TL;DR:** After getting comfortable with joins and window functions, I’m now diving into more advanced query structuring techniques. Subqueries felt like a natural extension of filtering and aggregation. CTEs, on the other hand, i…

## What’s new and why it matters
After getting comfortable with joins and window functions, I’m now diving into more advanced query structuring techniques. Subqueries felt like a natural extension of filtering and aggregation. CTEs, on the other hand, introduced a cleaner way of breaking down complex logic into readable, step-by-step components. This guide provides a practical comparison of both concepts using a simple student exam results dataset, highlighting when and why to choose one over the other. What is a Subquery? A subquery is a query nested inside another query. It runs first, and its result is used by the outer (m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tom_chege/understanding-subqueries-and-ctes-in-sql-12c5

## Related notes
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-10-write-your-sql-like-a-pro-mastering-common-table-expressions-ctes]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-11-sql-joins-window-functions]]
