---
title: Zero-Downtime Schema Changes (You Can Do This)
date: '2026-05-04'
source: https://dev.to/tosh2308/zero-downtime-schema-changes-you-can-do-this-dei
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-14-schema-risk]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-29-ca-40---alter-tables]]'
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
- '[[2026-03-28-modifying-tables-in-sql-using-alter]]'
- '[[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]'
status: unread
---

> **TL;DR:** You need to add a column to a table with 100 million rows. Old approach: Lock the table, add column, wait 30 minutes, production is down. New approach: Add column, backfill data, no downtime. The Pattern Step 1: Add colu…

## What’s new and why it matters
You need to add a column to a table with 100 million rows. Old approach: Lock the table, add column, wait 30 minutes, production is down. New approach: Add column, backfill data, no downtime. The Pattern Step 1: Add column (new, nullable) ALTER TABLE users ADD COLUMN new_field VARCHAR ( 255 ) NULL ; Takes 2 seconds. Table briefly locked. No big deal. Step 2: Backfill in batches UPDATE users SET new_field = computed_value WHERE id >= 0 AND id < 10000 ; UPDATE users SET new_field = computed_value WHERE id >= 10000 AND id < 20000 ; -- ... repeat in batches Takes time but doesn't lock the whole ta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tosh2308/zero-downtime-schema-changes-you-can-do-this-dei

## Related notes
- [[2026-03-14-schema-risk]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-29-ca-40---alter-tables]]
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
- [[2026-03-28-modifying-tables-in-sql-using-alter]]
- [[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]
