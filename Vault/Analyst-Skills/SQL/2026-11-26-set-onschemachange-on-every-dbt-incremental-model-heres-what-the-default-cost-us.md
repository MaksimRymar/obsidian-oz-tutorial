---
title: Set on_schema_change on every dbt incremental model. Here's what the default
  cost us.
date: '2026-11-26'
source: https://dev.to/vijaykumar13/the-dbt-default-that-dropped-18-columns-for-six-weeks-4no2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-05-three-months-of-sales-vanished-and-every-dbt-run-was-green]]'
- '[[2026-11-25-merge-never-deletes-so-our-inventory-history-ran-40-high]]'
- '[[2026-11-26-the-migration-found-the-old-dashboard-had-been-counting-everything-twice]]'
- '[[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** As part of our SAP migration I've been auditing the dbt incremental models I inherited, and one setting keeps coming up: on_schema_change . Most projects never set it. On one of the inherited models, the default had been…

## What’s new and why it matters
As part of our SAP migration I've been auditing the dbt incremental models I inherited, and one setting keeps coming up: on_schema_change . Most projects never set it. On one of the inherited models, the default had been dropping 18 new columns for six weeks, without a single error, before I found it. In this article I'll show you what the default does, how I found the missing columns, how I fixed it, and the rule I'd now apply to every incremental model. (It's also the post I promised at the end of my last two.) The short version What happened: 18 new columns were added to an inherited increm…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vijaykumar13/the-dbt-default-that-dropped-18-columns-for-six-weeks-4no2

## Related notes
- [[2026-10-05-three-months-of-sales-vanished-and-every-dbt-run-was-green]]
- [[2026-11-25-merge-never-deletes-so-our-inventory-history-ran-40-high]]
- [[2026-11-26-the-migration-found-the-old-dashboard-had-been-counting-everything-twice]]
- [[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
