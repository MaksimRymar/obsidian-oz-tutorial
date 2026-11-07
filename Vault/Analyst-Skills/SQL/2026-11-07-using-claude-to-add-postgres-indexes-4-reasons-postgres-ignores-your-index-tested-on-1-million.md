---
title: 'Using Claude to Add Postgres Indexes: 4 Reasons Postgres Ignores Your Index,
  Tested on 1 Million…'
date: '2026-11-07'
source: https://medium.com/@amb39305/using-claude-to-add-postgres-indexes-4-reasons-postgres-ignores-your-index-tested-on-1-million-eab31d5968e6?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
related:
- '[[2026-11-01-using-claude-to-write-postgres-window-functions-3-traps-that-return-wrong-answers-without-an-error]]'
- '[[2026-11-03-using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error]]'
- '[[2026-10-23-using-claude-to-plan-a-fast-and-safe-bulk-load-with-postgres-copy]]'
- '[[2026-09-11-i-thought-duckdbs-variant-would-be-slow-then-i-tested-3-million-rows]]'
- '[[2026-08-06-the-region-that-sold-well-and-still-lost-money]]'
- '[[2026-10-13-using-claude-to-write-a-safe-bulk-delete-for-a-large-postgres-table]]'
status: unread
---

> **TL;DR:** The index existed, the query was correct, and it still read all 1,000,000 rows. A Python float parameter turned a 0.4 ms lookup into a 54… Continue reading on Medium »

## What’s new and why it matters
The index existed, the query was correct, and it still read all 1,000,000 rows. A Python float parameter turned a 0.4 ms lookup into a 54… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@amb39305/using-claude-to-add-postgres-indexes-4-reasons-postgres-ignores-your-index-tested-on-1-million-eab31d5968e6?source=rss------sql-5

## Related notes
- [[2026-11-01-using-claude-to-write-postgres-window-functions-3-traps-that-return-wrong-answers-without-an-error]]
- [[2026-11-03-using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error]]
- [[2026-10-23-using-claude-to-plan-a-fast-and-safe-bulk-load-with-postgres-copy]]
- [[2026-09-11-i-thought-duckdbs-variant-would-be-slow-then-i-tested-3-million-rows]]
- [[2026-08-06-the-region-that-sold-well-and-still-lost-money]]
- [[2026-10-13-using-claude-to-write-a-safe-bulk-delete-for-a-large-postgres-table]]
