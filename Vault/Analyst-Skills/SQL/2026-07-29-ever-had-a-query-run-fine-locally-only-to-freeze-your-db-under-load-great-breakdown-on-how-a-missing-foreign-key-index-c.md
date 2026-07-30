---
title: Ever had a query run fine locally, only to freeze your DB under load? 😱 Great
  breakdown on how a missing foreign key index caused 100% CPU usage—and how a simple
  composite index fixed it! 🚀
date: '2026-07-29'
source: https://dev.to/zahab_khan_65da25883c066c/ever-had-a-query-run-fine-locally-only-to-freeze-your-db-under-load-great-breakdown-on-how-a-3p5n
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tableau'
related:
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
- '[[2026-05-11-beyond-basic-indexes-mastering-partial-composite-and-covering-indexes-in-sql]]'
- '[[2026-05-25-the-n1-query-that-killed-our-database-and-how-i-fixed-it]]'
- '[[2026-05-22-the-dark-secret-of-scale-how-our-company-hit-a-tricky-problem-with-treasure-hunt-engine-at-10000-users]]'
- '[[2026-07-26-after-3-years-of-redis-i-finally-learned-how-to-test-cache-consistency]]'
- '[[2026-04-29-database-migrations-zero-downtime-sql-alembic-amp-schema-evolution-2026]]'
status: unread
---

> **TL;DR:** How an Unindexed Column Silently Killed Our Database under Load (and the 5-Minute Fix) Mia Keller Mia Keller Mia Keller Follow Jul 29 How an Unindexed Column Silently Killed Our Database under Load (and the 5-Minute Fix)…

## What’s new and why it matters
How an Unindexed Column Silently Killed Our Database under Load (and the 5-Minute Fix) Mia Keller Mia Keller Mia Keller Follow Jul 29 How an Unindexed Column Silently Killed Our Database under Load (and the 5-Minute Fix) # webdev # database # javascript # performance 26 reactions 9 comments 3 min read

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zahab_khan_65da25883c066c/ever-had-a-query-run-fine-locally-only-to-freeze-your-db-under-load-great-breakdown-on-how-a-3p5n

## Related notes
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
- [[2026-05-11-beyond-basic-indexes-mastering-partial-composite-and-covering-indexes-in-sql]]
- [[2026-05-25-the-n1-query-that-killed-our-database-and-how-i-fixed-it]]
- [[2026-05-22-the-dark-secret-of-scale-how-our-company-hit-a-tricky-problem-with-treasure-hunt-engine-at-10000-users]]
- [[2026-07-26-after-3-years-of-redis-i-finally-learned-how-to-test-cache-consistency]]
- [[2026-04-29-database-migrations-zero-downtime-sql-alembic-amp-schema-evolution-2026]]
