---
title: 'Using Claude to Write Postgres Queries: 4 NULL Traps That Return Wrong Answers
  Without an Error'
date: '2026-11-03'
source: https://medium.com/@amb39305/using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error-906b53fe2b23?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-11-01-using-claude-to-write-postgres-window-functions-3-traps-that-return-wrong-answers-without-an-error]]'
- '[[2026-10-29-one-null-made-this-sql-query-return-zero-rows]]'
- '[[2026-09-13-the-sql-queries-that-lie-to-you-with-a-straight-face]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-04-28-how-i-used-my-homebrew-tool-to-diagnose-and-fix-a-customers-database-slowness]]'
- '[[2026-07-20-the-sql-that-lies-to-you-7-bugs-that-corrupt-your-data-without-ever-throwing-an-error]]'
status: unread
---

> **TL;DR:** One NULL in my blocklist turned “4 customers not blocked” into 0, with no error and a normal-looking plan. The same query form later ran… Continue reading on Medium »

## What’s new and why it matters
One NULL in my blocklist turned “4 customers not blocked” into 0, with no error and a normal-looking plan. The same query form later ran… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@amb39305/using-claude-to-write-postgres-queries-4-null-traps-that-return-wrong-answers-without-an-error-906b53fe2b23?source=rss------sql-5

## Related notes
- [[2026-11-01-using-claude-to-write-postgres-window-functions-3-traps-that-return-wrong-answers-without-an-error]]
- [[2026-10-29-one-null-made-this-sql-query-return-zero-rows]]
- [[2026-09-13-the-sql-queries-that-lie-to-you-with-a-straight-face]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-04-28-how-i-used-my-homebrew-tool-to-diagnose-and-fix-a-customers-database-slowness]]
- [[2026-07-20-the-sql-that-lies-to-you-7-bugs-that-corrupt-your-data-without-ever-throwing-an-error]]
