---
title: 'SQL Gaps & Islands: Sessionization, Streaks & Run-Length Patterns'
date: '2026-07-10'
source: https://dev.to/gowthampotureddi/sql-gaps-islands-sessionization-streaks-run-length-patterns-3i0c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-06-04-sql-if-iif-nullif-null-handling-cheat-sheet-for-data-engineers]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-05-22-group-by-and-having-in-sql-aggregation-patterns-for-interviews]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** sql gaps and islands is the single most-asked "consecutive rows" family in senior data-engineering interviews — and the single most under-taught one in undergraduate SQL curricula. The same "identify runs of consecutive…

## What’s new and why it matters
sql gaps and islands is the single most-asked "consecutive rows" family in senior data-engineering interviews — and the single most under-taught one in undergraduate SQL curricula. The same "identify runs of consecutive events" ask shows up in five different colours: sessionization ("group events into 30-minute sessions"), login streaks ("longest consecutive-day streak per user"), uptime windows ("longest window with status = 'up'"), price plateaus ("compress the price series into runs of unchanged values"), and CDC state transitions ("emit one row per contiguous state"). Every answer starts f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sql-gaps-islands-sessionization-streaks-run-length-patterns-3i0c

## Related notes
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-06-04-sql-if-iif-nullif-null-handling-cheat-sheet-for-data-engineers]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-05-22-group-by-and-having-in-sql-aggregation-patterns-for-interviews]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
