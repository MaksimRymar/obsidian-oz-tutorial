---
title: NOT IN can be executed as an Anti-Join (NOT EXISTS) in PG19
date: '2026-09-24'
source: https://dev.to/franckpachot/not-in-executed-as-an-anti-join-not-exists-in-pg19-3gga
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-03-boost-postgresql-query-performance-proven-tips-indexing-strategies]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-09-sql-joins]]'
status: unread
---

> **TL;DR:** Most databases transform a NOT IN query to NOT EXISTS when possible, because the semantic is the same with NOT NULL resultsets (if they are not, see NOT IN vs. NOT EXISTS: often a data modeling issue ). PostgreSQL doesn'…

## What’s new and why it matters
Most databases transform a NOT IN query to NOT EXISTS when possible, because the semantic is the same with NOT NULL resultsets (if they are not, see NOT IN vs. NOT EXISTS: often a data modeling issue ). PostgreSQL doesn't and this leads to performance issues (see Recovering TPS After a Cross-Database Migration by Vinay Kumar Dumpa). PostgreSQL 19 will fix that and transform NOT IN to NOT EXISTS, when NOT NULL is guaranteed, so that a SubPlan or hashed SubPlan becomes an anti-join that can benefit from all join methods: Nested Loop, Merge Join or Hash Join. I'll demonstrate that at PostgreSQL C…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/franckpachot/not-in-executed-as-an-anti-join-not-exists-in-pg19-3gga

## Related notes
- [[2026-09-03-boost-postgresql-query-performance-proven-tips-indexing-strategies]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-09-sql-joins]]
