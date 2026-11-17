---
title: 'Using Claude to Write Postgres Money and Date Queries: 4 Type Traps That Are
  Off by a Penny or a…'
date: '2026-11-17'
source: https://medium.com/@amb39305/using-claude-to-write-postgres-money-and-date-queries-4-type-traps-that-are-off-by-a-penny-or-a-3ec6999473a5?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-11-06-using-claude-to-write-postgres-transactions-4-concurrency-traps-that-pass-every-single-user-test]]'
- '[[2026-11-08-using-claude-to-write-postgres-recursive-queries-4-traps-including-the-one-that-never-finishes]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-13-using-claude-to-write-a-safe-bulk-delete-for-a-large-postgres-table]]'
- '[[2026-11-03-using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error]]'
- '[[2026-10-19-using-claude-to-find-whats-blocking-your-postgres-queries]]'
status: unread
---

> **TL;DR:** One million rows of 0.10 added up to 99,999.99999938629. A BETWEEN for “all of March” missed 3 of 5 rows from March 31. And round() gave 0… Continue reading on Medium »

## What’s new and why it matters
One million rows of 0.10 added up to 99,999.99999938629. A BETWEEN for “all of March” missed 3 of 5 rows from March 31. And round() gave 0… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@amb39305/using-claude-to-write-postgres-money-and-date-queries-4-type-traps-that-are-off-by-a-penny-or-a-3ec6999473a5?source=rss------sql-5

## Related notes
- [[2026-11-06-using-claude-to-write-postgres-transactions-4-concurrency-traps-that-pass-every-single-user-test]]
- [[2026-11-08-using-claude-to-write-postgres-recursive-queries-4-traps-including-the-one-that-never-finishes]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-13-using-claude-to-write-a-safe-bulk-delete-for-a-large-postgres-table]]
- [[2026-11-03-using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error]]
- [[2026-10-19-using-claude-to-find-whats-blocking-your-postgres-queries]]
