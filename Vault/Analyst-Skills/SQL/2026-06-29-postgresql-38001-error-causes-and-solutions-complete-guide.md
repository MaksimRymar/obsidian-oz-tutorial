---
title: 'PostgreSQL 38001 Error: Causes and Solutions Complete Guide'
date: '2026-06-29'
source: https://dev.to/dbmserror/postgresql-38001-error-causes-and-solutions-complete-guide-2m94
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-28-postgresql-2f004-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-29-postgresql-38002-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-19-oracle-ora-00933-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-28-postgresql-2f002-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-21-postgresql-23001-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-14-postgresql-22p02-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** PostgreSQL Error 38001: containing_sql_not_permitted PostgreSQL error code 38001 ( containing_sql_not_permitted ) occurs when a function declared with NO SQL or an incompatible SQL data access level attempts to execute S…

## What’s new and why it matters
PostgreSQL Error 38001: containing_sql_not_permitted PostgreSQL error code 38001 ( containing_sql_not_permitted ) occurs when a function declared with NO SQL or an incompatible SQL data access level attempts to execute SQL statements internally. This typically surfaces in procedural language functions (PL/pgSQL, PL/Python, PL/Perl) or external routine contexts where the declared SQL access level conflicts with the actual function body behavior. Top 3 Causes 1. Function Declared with NO SQL But Executes SQL Internally This is the most common cause. When you declare a function with NO SQL , Post…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dbmserror/postgresql-38001-error-causes-and-solutions-complete-guide-2m94

## Related notes
- [[2026-06-28-postgresql-2f004-error-causes-and-solutions-complete-guide]]
- [[2026-06-29-postgresql-38002-error-causes-and-solutions-complete-guide]]
- [[2026-06-19-oracle-ora-00933-error-causes-and-solutions-complete-guide]]
- [[2026-06-28-postgresql-2f002-error-causes-and-solutions-complete-guide]]
- [[2026-06-21-postgresql-23001-error-causes-and-solutions-complete-guide]]
- [[2026-06-14-postgresql-22p02-error-causes-and-solutions-complete-guide]]
