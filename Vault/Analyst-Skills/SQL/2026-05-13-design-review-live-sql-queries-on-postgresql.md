---
title: 'Design review: Live SQL queries on PostgreSQL'
date: '2026-05-13'
source: https://dev.to/oxharris/design-review-live-sql-queries-on-postgresql-jo0
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
status: unread
---

> **TL;DR:** I’ve been experimenting with something I’ve wanted for a long time: "live mode" in SQL. Today, this is now possible on PostgreSQL: const result = await db . query ( `SELECT * FROM users` , { live : true } ); With { live:…

## What’s new and why it matters
I’ve been experimenting with something I’ve wanted for a long time: "live mode" in SQL. Today, this is now possible on PostgreSQL: const result = await db . query ( `SELECT * FROM users` , { live : true } ); With { live: true } , you get back a live result set that reflects the state of the DB in real time. If rows are inserted, updated, or deleted in the underlying table(s), result.rows reflects those changes automatically — without polling, manually wiring subscriptions, or pushing synchronization logic into application code. This work is part of a broader "universal query engine" effort for…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/oxharris/design-review-live-sql-queries-on-postgresql-jo0

## Related notes
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-04-21-sql-window-functions-and-ctes]]
