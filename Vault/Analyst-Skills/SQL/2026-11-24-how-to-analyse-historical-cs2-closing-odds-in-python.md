---
title: How to analyse historical CS2 closing odds in Python
date: '2026-11-24'
source: https://dev.to/oddlylikely_f1d8633a4ef73/analyse-historical-cs2-odds-in-python-with-two-csvs-3180
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-10-20-sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-11-18-build-an-arbitrage-betting-scanner-in-python]]'
status: unread
---

> **TL;DR:** CS2 closing odds are the last pre-match prices I recorded for a selection. Once a match is over, they let you compare what the market expected with the result. I started saving them in CS2Odds, a free passion project of…

## What’s new and why it matters
CS2 closing odds are the last pre-match prices I recorded for a selection. Once a match is over, they let you compare what the market expected with the result. I started saving them in CS2Odds, a free passion project of mine. This Python walkthrough uses historical odds from 125 finished matches and 1,468 bookmaker-side quotes to count favourite wins and check how one finalist’s price moved before kickoff. Start with the match as the unit of analysis Download matches.csv and series-winner-quotes.csv to the same directory. The first table has one row per finished match. The second has a row per…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/oddlylikely_f1d8633a4ef73/analyse-historical-cs2-odds-in-python-with-two-csvs-3180

## Related notes
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-10-20-sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-11-18-build-an-arbitrage-betting-scanner-in-python]]
