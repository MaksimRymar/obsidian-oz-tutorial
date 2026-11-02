---
title: 5 rules we used to turn 164,963 daily follower readings into one honest growth
  number
date: '2026-11-02'
source: https://dev.to/outfame/5-rules-we-used-to-turn-164963-daily-follower-readings-into-one-honest-growth-number-3kpa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]'
status: unread
---

> **TL;DR:** We publish an Instagram growth statistics page built from our own customer data: 164,963 daily follower-count readings from 7,271 Instagram accounts. The headline result is a median gain of +346 followers in the first 30…

## What’s new and why it matters
We publish an Instagram growth statistics page built from our own customer data: 164,963 daily follower-count readings from 7,271 Instagram accounts. The headline result is a median gain of +346 followers in the first 30 days across 981 accounts, with 86% of them growing. Below are the five cleaning rules that produced that number, why each one exists, and a SQL sketch of the core query. 1. Measure at "the reading closest to day N", within a window Daily readings are not perfectly daily. A job fails, an account is private for a day, a request times out. So the gain at day 30 is the reading clo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/outfame/5-rules-we-used-to-turn-164963-daily-follower-readings-into-one-honest-growth-number-3kpa

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]
