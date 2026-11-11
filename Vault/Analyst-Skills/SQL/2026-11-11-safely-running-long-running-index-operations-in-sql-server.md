---
title: Safely Running Long-Running Index Operations in SQL Server
date: '2026-11-11'
source: https://dev.to/gunjitchhatwal/safely-running-long-running-index-operations-in-sql-server-3b40
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-09-01-restore-of-database-failed-because-database-is-in-use-causes-solutions]]'
- '[[2026-09-25-zero-updated-rows-do-not-fail-a-d1-batch-testing-the-rollback-boundary]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** Creating or rebuilding an index on a large, actively used table is not merely a schema change. It is a production operation that can consume significant CPU, I/O, transaction log, and storage resources, and it can introd…

## What’s new and why it matters
Creating or rebuilding an index on a large, actively used table is not merely a schema change. It is a production operation that can consume significant CPU, I/O, transaction log, and storage resources, and it can introduce unexpected blocking even when the operation uses ONLINE = ON . This article explains a particularly subtle failure mode: an online index operation holds a schema-stability lock while an automatic statistics update waits for a schema-modification lock. SQL Server's lock queue can then place otherwise compatible application queries behind the waiting schema-modification reque…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gunjitchhatwal/safely-running-long-running-index-operations-in-sql-server-3b40

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-09-01-restore-of-database-failed-because-database-is-in-use-causes-solutions]]
- [[2026-09-25-zero-updated-rows-do-not-fail-a-d1-batch-testing-the-rollback-boundary]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
