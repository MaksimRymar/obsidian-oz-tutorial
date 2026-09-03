---
title: Ranking a Two-Dimensional Catalog With One SQL Expression
date: '2026-09-03'
source: https://dev.to/citationbuilder/ranking-a-two-dimensional-catalog-with-one-sql-expression-5akb
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
status: unread
---

> **TL;DR:** Every marketplace, catalog or directory app eventually hits the same question: given two independent dimensions, which rows do I show first? For us the dimensions are country and industry, and the rows are 1,300+ local b…

## What’s new and why it matters
Every marketplace, catalog or directory app eventually hits the same question: given two independent dimensions, which rows do I show first? For us the dimensions are country and industry, and the rows are 1,300+ local business directories. A plumber in Munich and a law firm in Toronto need overlapping-but-different lists out of the same table. The naive answers are all bad. Two dimensions of relevance is exactly the shape where "just add a WHERE clause" produces empty results and "just order by popularity" produces a list that ignores the user. This is the scoring expression we landed on, why…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/citationbuilder/ranking-a-two-dimensional-catalog-with-one-sql-expression-5akb

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
