---
title: 'PostgreSQL 22036 Error: Causes and Solutions Complete Guide'
date: '2026-08-22'
source: https://dev.to/dbmserror/postgresql-22036-error-causes-and-solutions-complete-guide-1m8c
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-18-postgresql-22036-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-20-postgresql-2203g-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-19-postgresql-2203b-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-20-postgresql-2203f-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-21-postgresql-22034-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-21-postgresql-22033-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** PostgreSQL Error 22036: non numeric sql json item PostgreSQL error code 22036 ( non numeric sql json item ) is thrown when a SQL/JSON path expression attempts to perform a numeric operation — such as arithmetic or numeri…

## What’s new and why it matters
PostgreSQL Error 22036: non numeric sql json item PostgreSQL error code 22036 ( non numeric sql json item ) is thrown when a SQL/JSON path expression attempts to perform a numeric operation — such as arithmetic or numeric methods like .abs() , .floor() , or .ceiling() — on a JSON item that is not actually a number (e.g., a string, boolean, null, array, or object). This error is most commonly encountered when using jsonb_path_query , jsonb_path_exists , or the @@ and @? operators introduced as part of the SQL/JSON standard in PostgreSQL 12+. If your JSON data originates from external APIs or le…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dbmserror/postgresql-22036-error-causes-and-solutions-complete-guide-1m8c

## Related notes
- [[2026-06-18-postgresql-22036-error-causes-and-solutions-complete-guide]]
- [[2026-06-20-postgresql-2203g-error-causes-and-solutions-complete-guide]]
- [[2026-06-19-postgresql-2203b-error-causes-and-solutions-complete-guide]]
- [[2026-06-20-postgresql-2203f-error-causes-and-solutions-complete-guide]]
- [[2026-08-21-postgresql-22034-error-causes-and-solutions-complete-guide]]
- [[2026-08-21-postgresql-22033-error-causes-and-solutions-complete-guide]]
