---
title: Can ClickHouse DELETE Data? A 2026 PR-by-PR Analysis
date: '2026-05-19'
source: https://dev.to/manveer_chawla_64a7283d5a/can-clickhouse-delete-data-a-2026-pr-by-pr-analysis-58in
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-30-does-clickhouse-support-updates-a-2026-data-analysis]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-12-clickhouse-joins-arent-slow-anymore-youre-reading-2020s-docs]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
- '[[2026-05-04-sql-date-time-functions-a-practical-guide-for-real-world-queries]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
status: unread
---

> **TL;DR:** TL;DR ClickHouse has supported DELETE operations since 2018. As of 2026, it ships four production-grade deletion paths: heavyweight ALTER TABLE DELETE , lightweight DELETE FROM (default since v23.3), patch-part DELETEs (…

## What’s new and why it matters
TL;DR ClickHouse has supported DELETE operations since 2018. As of 2026, it ships four production-grade deletion paths: heavyweight ALTER TABLE DELETE , lightweight DELETE FROM (default since v23.3), patch-part DELETEs (v25.7), and ALTER TABLE DROP PARTITION for bulk operations. The "ClickHouse is immutable / append-only" narrative is outdated by eight years and 80+ merged PRs spanning five architectural eras, and the evidence is in the commit history. We analyzed 80+ GitHub pull requests, official ClickHouse changelogs, and release blogs to trace the full evolution of DELETE support from 2018…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/manveer_chawla_64a7283d5a/can-clickhouse-delete-data-a-2026-pr-by-pr-analysis-58in

## Related notes
- [[2026-04-30-does-clickhouse-support-updates-a-2026-data-analysis]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-12-clickhouse-joins-arent-slow-anymore-youre-reading-2020s-docs]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
- [[2026-05-04-sql-date-time-functions-a-practical-guide-for-real-world-queries]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
