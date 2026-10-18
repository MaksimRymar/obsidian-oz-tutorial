---
title: Logging in PL/SQL that survives ROLLBACK (and 4 mistakes to avoid)
date: '2026-10-17'
source: https://dev.to/sabuhi_khalilov/logging-in-plsql-that-survives-rollback-and-4-mistakes-to-avoid-4jmn
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-09-01-oracle-ora-06545-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** You get a call: last night's batch failed, the transaction rolled back, and now someone asks "what happened?" You open your log table. It's empty. If your logging does a plain INSERT inside the same transaction as your b…

## What’s new and why it matters
You get a call: last night's batch failed, the transaction rolled back, and now someone asks "what happened?" You open your log table. It's empty. If your logging does a plain INSERT inside the same transaction as your business logic, a ROLLBACK removes the log entries together with the data. You lose the information at exactly the moment you need it. The fix is small: write log entries in their own transaction. Here is the pattern, step by step. 1. The log table CREATE TABLE app_log ( log_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY , log_ts TIMESTAMP DEFAULT SYSTIMESTAMP NOT NULL , mod…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sabuhi_khalilov/logging-in-plsql-that-survives-rollback-and-4-mistakes-to-avoid-4jmn

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-09-01-oracle-ora-06545-error-causes-and-solutions-complete-guide]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
