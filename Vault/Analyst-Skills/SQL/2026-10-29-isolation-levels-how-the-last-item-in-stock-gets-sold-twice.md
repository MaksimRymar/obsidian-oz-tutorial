---
title: 'Isolation Levels: How the Last Item in Stock Gets Sold Twice'
date: '2026-10-29'
source: https://dev.to/vladut02/isolation-levels-how-the-last-item-in-stock-gets-sold-twice-319f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-24-sql-database-projects-and-ai-a-match-made-in-heaven]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
status: unread
---

> **TL;DR:** Two customers buy the last item in stock at the same second. Both orders go through. Every line of your code ran inside a transaction, and SQL Server did exactly what its default setting promises. That setting is the iso…

## What’s new and why it matters
Two customers buy the last item in stock at the same second. Both orders go through. Every line of your code ran inside a transaction, and SQL Server did exactly what its default setting promises. That setting is the isolation level . There are four of them. This post walks through each one, the anomaly it stops, and the .NET class that quietly picks the strictest one for you. A transaction isn't a freeze A transaction promises all or nothing : your changes land together, or not at all. What it doesn't promise is that the world stops while you work. Other transactions keep reading and writing…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vladut02/isolation-levels-how-the-last-item-in-stock-gets-sold-twice-319f

## Related notes
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-24-sql-database-projects-and-ai-a-match-made-in-heaven]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
