---
title: Exploring a week of live game show results with pandas (500,510 rounds, 42
  games)
date: '2026-11-20'
source: https://dev.to/livecasinoradar/exploring-a-week-of-live-game-show-results-with-pandas-500510-rounds-42-games-30pg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-11-20-how-many-rounds-per-day-do-live-casino-games-run-measuring-42-games-with-pandas]]'
- '[[2026-05-03-pandas-secret-mini-language]]'
- '[[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
status: unread
---

> **TL;DR:** LiveCasinoRadar publishes a small open dataset: one CSV per week with round counts, bonus round shares and top multipliers for 42 live casino games. It is a nice size for practising pandas: 42 rows, 11 columns, real miss…

## What’s new and why it matters
LiveCasinoRadar publishes a small open dataset: one CSV per week with round counts, bonus round shares and top multipliers for 42 live casino games. It is a nice size for practising pandas: 42 rows, 11 columns, real missing values. This post loads the week of 9–15 November 2026 and answers three questions. 1. Load the data import pandas as pd URL = ( "https://raw.githubusercontent.com/livecasinoradar/" "live-casino-weekly-stats/main/live-casino-weekly-stats-2026-W46.csv" ) df = pd . read_csv ( URL ) print ( df . shape ) # (42, 11) print ( df [ "rounds_recorded" ] . sum ( ) ) # 500510 Each row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/livecasinoradar/exploring-a-week-of-live-game-show-results-with-pandas-500510-rounds-42-games-30pg

## Related notes
- [[2026-11-20-how-many-rounds-per-day-do-live-casino-games-run-measuring-42-games-with-pandas]]
- [[2026-05-03-pandas-secret-mini-language]]
- [[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
