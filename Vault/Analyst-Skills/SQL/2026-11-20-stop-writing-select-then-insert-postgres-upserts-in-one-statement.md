---
title: Stop Writing SELECT-Then-INSERT. Postgres Upserts in One Statement
date: '2026-11-20'
source: https://martin128.medium.com/stop-writing-select-then-insert-postgres-upserts-in-one-statement-ad13ec29a457?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-11-13-power-bi-mcp-servers-for-building-reports-with-an-llm-what-each-one-actually-does-2026]]'
- '[[2026-09-06-your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement]]'
- '[[2026-11-16-postgres-merge-vs-insert-on-conflict-merge-failed-3-of-4-concurrent-batches]]'
- '[[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]'
- '[[2026-06-24-sql-upsert-merge-in-practice-postgres-on-conflict-snowflake-bigquery-recipes]]'
- '[[2026-10-24-your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it]]'
status: unread
---

> **TL;DR:** INSERT ON CONFLICT does insert-or-update atomically. Here is DO NOTHING, DO UPDATE with EXCLUDED, telling insert from update, and the two… Continue reading on Medium »

## What’s new and why it matters
INSERT ON CONFLICT does insert-or-update atomically. Here is DO NOTHING, DO UPDATE with EXCLUDED, telling insert from update, and the two… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://martin128.medium.com/stop-writing-select-then-insert-postgres-upserts-in-one-statement-ad13ec29a457?source=rss------sql-5

## Related notes
- [[2026-11-13-power-bi-mcp-servers-for-building-reports-with-an-llm-what-each-one-actually-does-2026]]
- [[2026-09-06-your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement]]
- [[2026-11-16-postgres-merge-vs-insert-on-conflict-merge-failed-3-of-4-concurrent-batches]]
- [[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]
- [[2026-06-24-sql-upsert-merge-in-practice-postgres-on-conflict-snowflake-bigquery-recipes]]
- [[2026-10-24-your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it]]
