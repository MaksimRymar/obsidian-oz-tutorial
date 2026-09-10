---
title: I Backtested 'Volume Confirmation' on 15,900 Real A-Share Stock-Days. It Flipped
  Sign Between Two Consecutive Months.
date: '2026-09-10'
source: https://dev.to/felixwang007/i-backtested-volume-confirmation-on-15900-real-a-share-stock-days-it-flipped-sign-between-two-977
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** Every popular rule in Chinese retail trading has a cousin in English: a big up day on strong volume continues; a big up day on weak volume fails. In A-shares it is usually phrased as 量价配合 — price and volume must agree. I…

## What’s new and why it matters
Every popular rule in Chinese retail trading has a cousin in English: a big up day on strong volume continues; a big up day on weak volume fails. In A-shares it is usually phrased as 量价配合 — price and volume must agree. I wanted to know if it survives contact with real data. So I pulled daily bars for 584 liquid Shanghai/Shenzhen names from free public endpoints (no API key, no paid vendor), built 15,900 stock-days , and conditioned the next day's return on today's move and today's volume ratio. Then I split every bucket by calendar month. The rule works beautifully — until you split it by mont…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/felixwang007/i-backtested-volume-confirmation-on-15900-real-a-share-stock-days-it-flipped-sign-between-two-977

## Related notes
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
