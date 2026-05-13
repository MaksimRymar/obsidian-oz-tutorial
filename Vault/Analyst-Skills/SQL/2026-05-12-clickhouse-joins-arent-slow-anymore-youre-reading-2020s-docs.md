---
title: ClickHouse JOINs Aren't Slow Anymore (You're Reading 2020's Docs)
date: '2026-05-12'
source: https://dev.to/aman_puri_115f49d5ad3612d/clickhouse-joins-arent-slow-anymore-youre-reading-2020s-docs-15fe
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-28-postgresql-join-optimization-nested-loop-hash-and-merge]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
- '[[2026-03-02-postgresql-vs-mongodb-in-2026-when-to-choose-sql-over-nosql]]'
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-03-01-sql-joins]]'
status: unread
---

> **TL;DR:** ClickHouse JOIN performance was rebuilt between 2022 and 2026. The "avoid JOINs in ClickHouse" advice from 2020 is still circulating: "ClickHouse can't do JOINs." "Denormalize everything." "Only hash join is supported."…

## What’s new and why it matters
ClickHouse JOIN performance was rebuilt between 2022 and 2026. The "avoid JOINs in ClickHouse" advice from 2020 is still circulating: "ClickHouse can't do JOINs." "Denormalize everything." "Only hash join is supported." "JOINs OOM on anything bigger than RAM." All four were accurate in 2020. None of them are accurate today. In 2020, ClickHouse had one join algorithm, no disk spilling, no cost-based optimizer, and join order followed query syntax. If the right table did not fit in memory, the query crashed. Between 2022 and early 2026, the join subsystem was rebuilt. Six algorithms ship by defa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aman_puri_115f49d5ad3612d/clickhouse-joins-arent-slow-anymore-youre-reading-2020s-docs-15fe

## Related notes
- [[2026-04-28-postgresql-join-optimization-nested-loop-hash-and-merge]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
- [[2026-03-02-postgresql-vs-mongodb-in-2026-when-to-choose-sql-over-nosql]]
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-03-01-sql-joins]]
