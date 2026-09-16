---
title: What reversing a D1 composite index changes in the query plan
date: '2026-09-16'
source: https://dev.to/hirodeath/what-reversing-a-d1-composite-index-changes-in-the-query-plan-2gbo
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
status: unread
---

> **TL;DR:** For a notification query using WHERE user_id = ? AND created_at >= ? , indexes on (user_id, created_at) and (created_at, user_id) do not behave identically. In a local D1 comparison, the first plan showed both user and c…

## What’s new and why it matters
For a notification query using WHERE user_id = ? AND created_at >= ? , indexes on (user_id, created_at) and (created_at, user_id) do not behave identically. In a local D1 comparison, the first plan showed both user and creation time as search constraints. The reversed index showed creation time alone. The experiment examines the planned search range. It does not measure response time. Fix the query before comparing indexes The example takes the user and creation-time fields from SquadNote's notification table and keeps only the necessary columns. It does not change an operational database or i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hirodeath/what-reversing-a-d1-composite-index-changes-in-the-query-plan-2gbo

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
