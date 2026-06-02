---
title: 5 SQL queries developers always have to look up (with copy-paste answers)
date: '2026-06-02'
source: https://dev.to/forglydev/5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers-2ea2
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** Be honest — how many times have you Googled "SQL find duplicate rows" this year? Some queries just never stick in my head. Here are 5 I re-look-up constantly, with working answers you can copy. Syntax is PostgreSQL, with…

## What’s new and why it matters
Be honest — how many times have you Googled "SQL find duplicate rows" this year? Some queries just never stick in my head. Here are 5 I re-look-up constantly, with working answers you can copy. Syntax is PostgreSQL, with notes where other databases differ. 1. Find duplicate rows SELECT email , COUNT ( * ) AS count FROM users GROUP BY email HAVING COUNT ( * ) > 1 ; That gives you the duplicated values . To pull the full duplicate rows , use a window function: SELECT * FROM ( SELECT * , COUNT ( * ) OVER ( PARTITION BY email ) AS dup_count FROM users ) t WHERE dup_count > 1 ; 2. Get the second-hi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/forglydev/5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers-2ea2

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-03-08-understanding-group-by-in-sql]]
