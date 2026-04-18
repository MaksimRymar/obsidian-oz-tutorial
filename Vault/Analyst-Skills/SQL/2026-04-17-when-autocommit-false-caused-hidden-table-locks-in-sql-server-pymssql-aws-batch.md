---
title: 🚨 When autocommit = false Caused Hidden Table Locks in SQL Server (pymssql
  + AWS Batch)
date: '2026-04-17'
source: https://dev.to/lokesh_vangari_a671430724/when-autocommit-false-caused-hidden-table-locks-in-sql-server-pymssql-aws-batch-81e
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-getting-started-with-seal-report-applying-custom-joins]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
status: unread
---

> **TL;DR:** While moving a workload from server to AWS Batch (Python), we hit a strange issue: Some SQL jobs started taking 2x longer Parallel jobs were getting blocked / waiting No code changes in SQL After debugging, the root caus…

## What’s new and why it matters
While moving a workload from server to AWS Batch (Python), we hit a strange issue: Some SQL jobs started taking 2x longer Parallel jobs were getting blocked / waiting No code changes in SQL After debugging, the root cause turned out to be: 👉 autocommit = false in pymssql 🧩 The Setup From Python, we were executing a group of SQL statements in one go (sample): DECLARE @ jobId INT ; EXEC @ jobId = dbo . ProcessJob @ input = 123 ; IF ( @ jobId > 0 ) PRINT 'Job processed' ; ELSE PRINT 'Job failed' ; Inside the stored procedure (sample): CREATE PROCEDURE dbo . ProcessJob @ input INT AS BEGIN BEGIN T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/lokesh_vangari_a671430724/when-autocommit-false-caused-hidden-table-locks-in-sql-server-pymssql-aws-batch-81e

## Related notes
- [[2026-04-02-getting-started-with-seal-report-applying-custom-joins]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
