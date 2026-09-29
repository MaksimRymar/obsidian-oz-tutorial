---
title: One long SELECT, one ALTER TABLE, and every query behind them
date: '2026-09-29'
source: https://dev.to/remdore/one-long-select-one-alter-table-and-every-query-behind-them-3l6i
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]'
- '[[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]'
status: unread
---

> **TL;DR:** The version of this I keep meeting goes something like: a migration ran at ten past two, it added a nullable column, the change itself is instant because Postgres has stored those as metadata since version 11, and yet fo…

## What’s new and why it matters
The version of this I keep meeting goes something like: a migration ran at ten past two, it added a nullable column, the change itself is instant because Postgres has stored those as metadata since version 11, and yet for about four seconds every request to the site timed out. Nobody can find a slow query, because there wasn't one. The migration shows up in the logs having taken a millisecond or two. I wanted to watch that happen under conditions I controlled, so I built the smallest version of it I could: four sessions, one table, and a stopwatch on each. Four sessions and a stopwatch The tab…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/remdore/one-long-select-one-alter-table-and-every-query-behind-them-3l6i

## Related notes
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]
- [[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]
