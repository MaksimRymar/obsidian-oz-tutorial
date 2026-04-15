---
title: Stop Pasting \timing — Run Your SQL 100 Times and Get p99
date: '2026-04-15'
source: https://dev.to/gillarohith/stop-pasting-timing-run-your-sql-100-times-and-get-p99-1g37
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]'
- '[[2026-03-16-surrealdb-how-i-deleted-70-of-my-backend-code-part-2]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** Here is a trap I have fallen into more times than I can count. I write a query. I run it. It takes 48ms. I nod, satisfied, and deploy it. In production it p99s at 1.8 seconds during peak traffic, the on-call engineer pag…

## What’s new and why it matters
Here is a trap I have fallen into more times than I can count. I write a query. I run it. It takes 48ms. I nod, satisfied, and deploy it. In production it p99s at 1.8 seconds during peak traffic, the on-call engineer pages me, and I spend the next hour explaining how "on my machine it was fine." A single EXPLAIN ANALYZE run is not a benchmark. It is an anecdote. The first run pays the cost of cold caches, parse, plan, and whatever else the database had queued. The second run is suspiciously fast because everything is now in the buffer cache. Somewhere between "ran it once in psql" and "ran it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gillarohith/stop-pasting-timing-run-your-sql-100-times-and-get-p99-1g37

## Related notes
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]
- [[2026-03-16-surrealdb-how-i-deleted-70-of-my-backend-code-part-2]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
