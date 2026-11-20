---
title: How many rounds per day do live casino games run? Measuring 42 games with pandas
date: '2026-11-20'
source: https://dev.to/livecasinoradar/how-many-rounds-per-day-do-live-casino-games-run-measuring-42-games-with-pandas-5cho
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-03-pandas-secret-mini-language]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-16-how-to-check-an-x402-endpoint-yourself-and-what-week-46s-outages-looked-like]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-08-one-cell-many-values-when-a-column-holds-a-list]]'
status: unread
---

> **TL;DR:** Short answer: in the week of 9–15 November 2026, the 42 live casino games tracked by LiveCasinoRadar ran a median of about 1,614 rounds per day each. The fastest was Stake Slide at about 4,018 rounds per day, the slowest…

## What’s new and why it matters
Short answer: in the week of 9–15 November 2026, the 42 live casino games tracked by LiveCasinoRadar ran a median of about 1,614 rounds per day each. The fastest was Stake Slide at about 4,018 rounds per day, the slowest Mega Fire Blaze Lucky Ball at about 745. Crazy Time ran about 1,715 rounds per day, Ice Fishing about 2,261 and Monopoly Big Baller about 983. The numbers come from an open weekly CSV. This post shows the pandas code behind them. Load the data import pandas as pd URL = ( "https://raw.githubusercontent.com/livecasinoradar/" "live-casino-weekly-stats/main/live-casino-weekly-stat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/livecasinoradar/how-many-rounds-per-day-do-live-casino-games-run-measuring-42-games-with-pandas-5cho

## Related notes
- [[2026-05-03-pandas-secret-mini-language]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-16-how-to-check-an-x402-endpoint-yourself-and-what-week-46s-outages-looked-like]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-08-one-cell-many-values-when-a-column-holds-a-list]]
