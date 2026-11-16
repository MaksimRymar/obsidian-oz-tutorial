---
title: 'How to Use pandas resample().ohlc() on Data With a Lunch Break: 30-Minute
  Bars, Session-Aligned Hourly Bars and Correct Daily Candles'
date: '2026-11-16'
source: https://dev.to/dustinliang/how-to-use-pandas-resampleohlc-on-data-with-a-lunch-break-30-minute-bars-session-aligned-1fl0
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
status: unread
---

> **TL;DR:** df.resample("30min").ohlc() looks like a one-liner, and on round-the-clock data it is. On anything that follows a trading calendar it quietly produces empty bars, hourly bars that straddle the open, half-length bars afte…

## What’s new and why it matters
df.resample("30min").ohlc() looks like a one-liner, and on round-the-clock data it is. On anything that follows a trading calendar it quietly produces empty bars, hourly bars that straddle the open, half-length bars after lunch, and daily candles with the wrong high and low. This post walks through pandas resample ohlc on minute-level data that follows the A-share session layout (09:30–11:30 and 13:00–15:00), and shows how to get bars that line up with the sessions. The series being resampled is a synthetic per-minute "heat" score for one unnamed stock, plus a per-minute mention count. The sam…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dustinliang/how-to-use-pandas-resampleohlc-on-data-with-a-lunch-break-30-minute-bars-session-aligned-1fl0

## Related notes
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
