---
title: 'Using Claude to Write Postgres Upserts: 4 ON CONFLICT Traps That Lose Data
  Without an Error'
date: '2026-11-04'
source: https://medium.com/@amb39305/using-claude-to-write-postgres-upserts-4-on-conflict-traps-that-lose-data-without-an-error-3ee1c52fb448?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-11-03-using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error]]'
- '[[2026-11-01-using-claude-to-write-postgres-window-functions-3-traps-that-return-wrong-answers-without-an-error]]'
- '[[2026-07-20-the-sql-that-lies-to-you-7-bugs-that-corrupt-your-data-without-ever-throwing-an-error]]'
- '[[2026-07-22-building-an-idempotent-etl-pipeline-with-apache-nifi-and-postgresql]]'
- '[[2026-08-01-five-oracle-sql-bugs-that-never-throw-an-error-message]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
status: unread
---

> **TL;DR:** A late-arriving message overwrote newer data, a batch silently kept the older row, and after 1,000 rejected inserts my next new row got ID… Continue reading on Medium »

## What’s new and why it matters
A late-arriving message overwrote newer data, a batch silently kept the older row, and after 1,000 rejected inserts my next new row got ID… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@amb39305/using-claude-to-write-postgres-upserts-4-on-conflict-traps-that-lose-data-without-an-error-3ee1c52fb448?source=rss------sql-5

## Related notes
- [[2026-11-03-using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error]]
- [[2026-11-01-using-claude-to-write-postgres-window-functions-3-traps-that-return-wrong-answers-without-an-error]]
- [[2026-07-20-the-sql-that-lies-to-you-7-bugs-that-corrupt-your-data-without-ever-throwing-an-error]]
- [[2026-07-22-building-an-idempotent-etl-pipeline-with-apache-nifi-and-postgresql]]
- [[2026-08-01-five-oracle-sql-bugs-that-never-throw-an-error-message]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
