---
title: Speeding Up a Slow PL/SQL Routine with BULK COLLECT and FORALL
date: '2026-09-03'
source: https://dev.to/zahid23saim/speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall-5c0l
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-07-15-samkhya-v11-never-regress-putting-a-model-in-your-query-optimizer-without-letting-it-wreck-the-plan]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** The single most common performance problem I have run into in Oracle PL/SQL is not a missing index or a bad join. It is a loop that processes one row at a time. The code reads fine, it passes review, and then it runs for…

## What’s new and why it matters
The single most common performance problem I have run into in Oracle PL/SQL is not a missing index or a bad join. It is a loop that processes one row at a time. The code reads fine, it passes review, and then it runs for forty minutes on a table that has grown past what anyone tested against. This tutorial walks through why that happens and how BULK COLLECT and FORALL fix it, usually by an order of magnitude, without changing what the routine actually does. The problem: the context switch When a PL/SQL block runs a SQL statement, control passes from the PL/SQL engine to the SQL engine and back…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/zahid23saim/speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall-5c0l

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-07-15-samkhya-v11-never-regress-putting-a-model-in-your-query-optimizer-without-letting-it-wreck-the-plan]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
