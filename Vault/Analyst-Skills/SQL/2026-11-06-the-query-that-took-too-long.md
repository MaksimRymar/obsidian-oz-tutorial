---
title: The query that took too long
date: '2026-11-06'
source: https://dev.to/crtdrops/the-query-that-took-too-long-gnp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]'
status: unread
---

> **TL;DR:** The query endpoints of a transactional platform were returning HTTP 504: timeouts, with pagination and without it. The table was large—more than eight million rows in 2026 alone—and the first temptation was to think that…

## What’s new and why it matters
The query endpoints of a transactional platform were returning HTTP 504: timeouts, with pagination and without it. The table was large—more than eight million rows in 2026 alone—and the first temptation was to think that explained everything: more rows, more time, more server. It did not. The problem was not reading a large table, but how MySQL joined, filtered and sorted the data to answer that query. That is what this note is about. The figures in the examples are illustrative: the plans in the plan reader are reconstructed, and the growth model is a model, not a measurement. From the case c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/crtdrops/the-query-that-took-too-long-gnp

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]
