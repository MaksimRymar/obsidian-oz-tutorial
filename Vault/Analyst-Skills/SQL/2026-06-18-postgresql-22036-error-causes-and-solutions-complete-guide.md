---
title: 'PostgreSQL 22036 Error: Causes and Solutions Complete Guide'
date: '2026-06-18'
source: https://dev.to/dbmserror/postgresql-22036-error-causes-and-solutions-complete-guide-238c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-14-postgresql-22p02-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-16-postgresql-22031-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-17-postgresql-22032-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-03-postgresql-22000-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-12-postgresql-22003-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-07-postgresql-22007-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** PostgreSQL Error 22036: non numeric sql json item PostgreSQL error code 22036 ( non numeric sql json item ) occurs when a SQL/JSON path expression attempts to perform a numeric operation on a JSON item that is not a numb…

## What’s new and why it matters
PostgreSQL Error 22036: non numeric sql json item PostgreSQL error code 22036 ( non numeric sql json item ) occurs when a SQL/JSON path expression attempts to perform a numeric operation on a JSON item that is not a number — such as a string, boolean, array, or object. This error was introduced alongside the SQL/JSON Path feature in PostgreSQL 12 and typically surfaces in queries using jsonb_path_query , jsonb_path_exists , or the @@ and @? operators. Top 3 Causes 1. Numeric Values Stored as Strings The most common cause is JSON data where numbers are stored as quoted strings (e.g., "price": "…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dbmserror/postgresql-22036-error-causes-and-solutions-complete-guide-238c

## Related notes
- [[2026-06-14-postgresql-22p02-error-causes-and-solutions-complete-guide]]
- [[2026-06-16-postgresql-22031-error-causes-and-solutions-complete-guide]]
- [[2026-06-17-postgresql-22032-error-causes-and-solutions-complete-guide]]
- [[2026-06-03-postgresql-22000-error-causes-and-solutions-complete-guide]]
- [[2026-06-12-postgresql-22003-error-causes-and-solutions-complete-guide]]
- [[2026-06-07-postgresql-22007-error-causes-and-solutions-complete-guide]]
