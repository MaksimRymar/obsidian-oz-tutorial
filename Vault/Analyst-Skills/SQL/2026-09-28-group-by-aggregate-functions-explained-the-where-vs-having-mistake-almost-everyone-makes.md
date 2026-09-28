---
title: GROUP BY & Aggregate Functions Explained (the WHERE vs HAVING mistake almost
  everyone makes)
date: '2026-09-28'
source: https://dev.to/neha_christina_1ac8651819/group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes-1nfg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-09-23-sql--window-functions]]'
status: unread
---

> **TL;DR:** If you've written more than a handful of SQL queries, you've used GROUP BY . But there's a difference between writing a GROUP BY that happens to run and actually understanding what it's doing — and that gap is exactly wh…

## What’s new and why it matters
If you've written more than a handful of SQL queries, you've used GROUP BY . But there's a difference between writing a GROUP BY that happens to run and actually understanding what it's doing — and that gap is exactly where a lot of junior developers get tripped up in interviews and in code review. This post walks through GROUP BY and the five core aggregate functions from the ground up, then covers the mistake that catches almost everyone at least once: mixing up WHERE and HAVING . The problem GROUP BY solves Say you've got an orders table with one row per order: order _ id | region | product…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/neha_christina_1ac8651819/group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes-1nfg

## Related notes
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-09-23-sql--window-functions]]
