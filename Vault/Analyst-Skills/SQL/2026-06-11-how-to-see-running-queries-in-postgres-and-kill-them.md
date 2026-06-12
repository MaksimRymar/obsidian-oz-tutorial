---
title: How to see running queries in Postgres and kill them
date: '2026-06-11'
source: https://dev.to/dsplce-co/how-to-see-running-queries-in-postgres-and-kill-them-j5i
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-08-how-to-find-and-kill-long-running-queries-in-sql-server]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
status: unread
---

> **TL;DR:** Something is slow. Maybe a page takes forever to load, maybe a migration is hanging, maybe your Supabase dashboard just spins. You suspect a query is stuck somewhere in your database, but you can't see what's happening —…

## What’s new and why it matters
Something is slow. Maybe a page takes forever to load, maybe a migration is hanging, maybe your Supabase dashboard just spins. You suspect a query is stuck somewhere in your database, but you can't see what's happening — Postgres doesn't exactly surface this on its own. Turns out it does. You just need to ask. Seeing what's running Postgres keeps track of every active connection and what it's doing in a system view called pg_stat_activity . You can query it like any table: SELECT pid , state , query , age ( clock_timestamp (), query_start ) AS duration FROM pg_stat_activity WHERE state != 'idl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dsplce-co/how-to-see-running-queries-in-postgres-and-kill-them-j5i

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-08-how-to-find-and-kill-long-running-queries-in-sql-server]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
