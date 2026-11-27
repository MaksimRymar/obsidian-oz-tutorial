---
title: how did the export get order 2 and miss order 1?
date: '2026-11-27'
source: https://dev.to/rider_lee/how-did-the-export-get-order-2-and-miss-order-1-jdc
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-11-26-one-database-one-reading-of-sql-why-paritas-now-runs-in-oracle-mode-only]]'
status: unread
---

> **TL;DR:** If I saw this query in a pull request, my first question would be “When do we save the checkpoint?” SELECT id , order_ref FROM order_events WHERE id > $1 ORDER BY id LIMIT 100 ; The worker sends a batch of orders to a re…

## What’s new and why it matters
If I saw this query in a pull request, my first question would be “When do we save the checkpoint?” SELECT id , order_ref FROM order_events WHERE id > $1 ORDER BY id LIMIT 100 ; The worker sends a batch of orders to a reporting database, waits for the write to succeed, then saves the last ID it sent. Next time around, it picks up from there. “After the write succeeds” sounds like a good answer. I could easily move on to the next file. But there’s another question worth asking. When we save ID 2, how do we know we’ve already seen ID 1? Two terminals are enough to see it Open two psql sessions a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rider_lee/how-did-the-export-get-order-2-and-miss-order-1-jdc

## Related notes
- [[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-11-26-one-database-one-reading-of-sql-why-paritas-now-runs-in-oracle-mode-only]]
