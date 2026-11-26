---
title: MERGE never deletes, so our inventory history ran 40% high
date: '2026-11-25'
source: https://dev.to/vijaykumar13/merge-never-deletes-so-our-inventory-history-ran-40-high-2h5m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-11-26-the-migration-found-the-old-dashboard-had-been-counting-everything-twice]]'
- '[[2026-10-05-three-months-of-sales-vanished-and-every-dbt-run-was-green]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]'
status: unread
---

> **TL;DR:** In my last post I wrote about a dbt incremental model that deleted too much: a delete+insert that wiped whole fiscal periods down to a few dozen rows. This time it's the opposite. In this article I'll show you how a dail…

## What’s new and why it matters
In my last post I wrote about a dbt incremental model that deleted too much: a delete+insert that wiped whole fiscal periods down to a few dozen rows. This time it's the opposite. In this article I'll show you how a daily merge kept adding rows that were no longer true, why every dbt run stayed green, how we proved where the problem was, and how we cleaned up 19 months of history without guessing. There's also a second silent failure hiding inside the first one, which I think is the more useful lesson. Some background I'm an analytics engineer at a leading North American housewares company, an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vijaykumar13/merge-never-deletes-so-our-inventory-history-ran-40-high-2h5m

## Related notes
- [[2026-11-26-the-migration-found-the-old-dashboard-had-been-counting-everything-twice]]
- [[2026-10-05-three-months-of-sales-vanished-and-every-dbt-run-was-green]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]
