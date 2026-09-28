---
title: 'Set-Based vs. Row by Row: PostgreSQL Refresh from 114 to 12 Seconds'
date: '2026-09-28'
source: https://dev.to/marcus1968/set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds-p7p
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
status: unread
---

> **TL;DR:** One click on "Refresh schema", and after 60 seconds the browser shows the error message 504 Gateway Timeout, because the web server in front of the application will not wait any longer for a response. On the server, the…

## What’s new and why it matters
One click on "Refresh schema", and after 60 seconds the browser shows the error message 504 Gateway Timeout, because the web server in front of the application will not wait any longer for a response. On the server, the work continues undisturbed, only nobody can see it. So a second click follows, then a third, and shortly afterwards four runs are computing at the same time. A single run across 1,000 tables took a measured 114 seconds. The requirement was less than three seconds. The cause was not a slow query but a loop that asked the source database for each table individually and stored the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marcus1968/set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds-p7p

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
