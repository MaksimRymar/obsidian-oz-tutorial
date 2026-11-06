---
title: A trip to China is 311 trips, not 44,473 — and four of the six line items are
  constants
date: '2026-11-06'
source: https://dev.to/sinostay/a-trip-to-china-is-311-trips-not-44473-and-four-of-the-six-line-items-are-constants-121g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-14-my-migration-generator-shuffled-itself-for-two-days-pythonhashseed-was-the-coin-flip]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** I expected the expensive part of building a travel-cost dataset to be the flights. It turned out to be the opposite: the flights were the only part that needed real modelling, because everything else collapsed into a con…

## What’s new and why it matters
I expected the expensive part of building a travel-cost dataset to be the flights. It turned out to be the opposite: the flights were the only part that needed real modelling, because everything else collapsed into a constant. The table 44,473 priced routes. 88 origin countries. 311 Chinese destinations. Each row itemises six things — flights, accommodation, food, local transport, attractions, fixed costs (visa, insurance, eSIM, card fees) — and the six sum exactly to the stored total. The first thing I did after loading it was check whether that "exactly" was true: SELECT COUNT ( * ) AS bad F…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sinostay/a-trip-to-china-is-311-trips-not-44473-and-four-of-the-six-line-items-are-constants-121g

## Related notes
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-14-my-migration-generator-shuffled-itself-for-two-days-pythonhashseed-was-the-coin-flip]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
