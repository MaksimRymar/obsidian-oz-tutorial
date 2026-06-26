---
title: A 1000x Speedup From One Index — and Why It Sometimes Does Nothing
date: '2026-06-25'
source: https://dev.to/danewu/a-1000x-speedup-from-one-index-and-why-it-sometimes-does-nothing-6if
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** Rails Performance: Lessons from Production — #2 "Slow query? Add an index" is something everyone has heard. But I once hit a more embarrassing situation: I added the index, and the query didn't get any faster. Debugging…

## What’s new and why it matters
Rails Performance: Lessons from Production — #2 "Slow query? Add an index" is something everyone has heard. But I once hit a more embarrassing situation: I added the index, and the query didn't get any faster. Debugging that forced me to actually understand how indexes work — when they're lightning fast, and when they simply won't be used. This post walks through it with one example: a shipments table with a few million rows. 🐌 I added an index and the query was still slow The shipments table has 3 million rows. The front end looks up one row by tracking number: Shipment.where(tracking_no: "AB…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danewu/a-1000x-speedup-from-one-index-and-why-it-sometimes-does-nothing-6if

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
