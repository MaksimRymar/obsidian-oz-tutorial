---
title: '1 Ticket, 20 Orders: The SQL Race Condition Hiding in Your Code'
date: '2026-11-21'
source: https://dev.to/refactorly/1-ticket-20-orders-the-sql-race-condition-hiding-in-your-code-pkd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-10-29-two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql]]'
- '[[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]'
- '[[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
status: unread
---

> **TL;DR:** One concert ticket left. Twenty people click "Buy" at the same time. My code sold it twenty times , and the stock still said 0 , so nothing looked wrong. Here's the bug, the measurements, and two ways to fix it. Everythi…

## What’s new and why it matters
One concert ticket left. Twenty people click "Buy" at the same time. My code sold it twenty times , and the stock still said 0 , so nothing looked wrong. Here's the bug, the measurements, and two ways to fix it. Everything below ran on PostgreSQL 17 with Node.js 22 and node-postgres ( pg ), on a local throwaway database. Video version: The code: looks correct, right? async function buy ( customer ) { const { rows } = await db . query ( "SELECT stock FROM products WHERE id = 1" ) ; if ( rows [ 0 ] . stock > 0 ) { await db . query ( "UPDATE products SET stock = $1 WHERE id = 1" , [ rows [ 0 ] .…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/1-ticket-20-orders-the-sql-race-condition-hiding-in-your-code-pkd

## Related notes
- [[2026-10-29-two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql]]
- [[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]
- [[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
