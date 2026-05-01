---
title: Does ClickHouse Support UPDATEs? A 2026 Data Analysis
date: '2026-04-30'
source: https://dev.to/manveer_chawla_64a7283d5a/does-clickhouse-support-updates-a-2026-data-analysis-4m75
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
- '[[2026-03-02-postgresql-vs-mongodb-in-2026-when-to-choose-sql-over-nosql]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
status: unread
---

> **TL;DR:** TL;DR Yes, ClickHouse fully supports UPDATEs. As of April 2026, ClickHouse ships standard SQL UPDATE ... SET ... WHERE syntax that runs in milliseconds, alongside four other update mechanisms: ALTER TABLE … UPDATE mutati…

## What’s new and why it matters
TL;DR Yes, ClickHouse fully supports UPDATEs. As of April 2026, ClickHouse ships standard SQL UPDATE ... SET ... WHERE syntax that runs in milliseconds, alongside four other update mechanisms: ALTER TABLE … UPDATE mutations for bulk operations, lightweight DELETE, on-the-fly mutation visibility, and ReplacingMergeTree for high-volume upserts and CDC. The "ClickHouse is append-only" claim is outdated by eight years and 100+ merged pull requests. Key facts: Standard SQL UPDATE shipped in ClickHouse 25.7 (July 2025) via PR #82004 , backed by a new "patch part" architecture. It was promoted to Bet…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/manveer_chawla_64a7283d5a/does-clickhouse-support-updates-a-2026-data-analysis-4m75

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
- [[2026-03-02-postgresql-vs-mongodb-in-2026-when-to-choose-sql-over-nosql]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
