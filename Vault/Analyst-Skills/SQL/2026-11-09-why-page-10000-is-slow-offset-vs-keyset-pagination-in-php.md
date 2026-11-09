---
title: 'Why Page 10,000 Is Slow: Offset vs Keyset Pagination in PHP'
date: '2026-11-09'
source: https://medium.com/@annxsa/why-page-10-000-is-slow-offset-vs-keyset-pagination-in-php-affbc65faba6?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-05-offset-vs-cursor-pagination-which-one-should-you-use-in-high-performance-apis]]'
- '[[2026-03-16-stop-writing-slow-sql-10-techniques-that-will-make-your-queries-lightning-fast]]'
- '[[2026-09-05-the-index-that-makes-your-query-fast-can-make-your-writes-slow]]'
- '[[2026-04-09-the-day-next-page-took-down-production-why-i-banned-offset-pagination]]'
- '[[2026-07-14-the-14000-nightly-discrepancy-that-turned-out-to-be-a-timezone]]'
- '[[2026-10-06-raw-sql-query-builder-or-eloquent-how-php-should-talk-to-your-database]]'
status: unread
---

> **TL;DR:** Page 1 took 0.1ms; page 25,000 took 50x longer — same query. Why OFFSET rots at scale, and the keyset approach that stays flat. Measured. Continue reading on Medium »

## What’s new and why it matters
Page 1 took 0.1ms; page 25,000 took 50x longer — same query. Why OFFSET rots at scale, and the keyset approach that stays flat. Measured. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@annxsa/why-page-10-000-is-slow-offset-vs-keyset-pagination-in-php-affbc65faba6?source=rss------sql-5

## Related notes
- [[2026-07-05-offset-vs-cursor-pagination-which-one-should-you-use-in-high-performance-apis]]
- [[2026-03-16-stop-writing-slow-sql-10-techniques-that-will-make-your-queries-lightning-fast]]
- [[2026-09-05-the-index-that-makes-your-query-fast-can-make-your-writes-slow]]
- [[2026-04-09-the-day-next-page-took-down-production-why-i-banned-offset-pagination]]
- [[2026-07-14-the-14000-nightly-discrepancy-that-turned-out-to-be-a-timezone]]
- [[2026-10-06-raw-sql-query-builder-or-eloquent-how-php-should-talk-to-your-database]]
