---
title: How I built a data quality API that runs at the edge in milliseconds
date: '2026-03-30'
source: https://dev.to/appdeviq/how-i-built-a-data-quality-api-that-runs-at-the-edge-in-milliseconds-514c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-03-28-tinybird-has-a-free-real-time-analytics-api-query-billions-of-rows-in-milliseconds]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-03-24-a-day-in-the-life-of-a-data-engineer-real-talk-no-filter]]'
- '[[2026-03-11-i-built-a-python-csv-cleaner-that-fixes-messy-data-in-one-command]]'
status: unread
---

> **TL;DR:** Bad data is quiet. That's the problem. Your pipeline doesn't crash. Your tests pass. Three weeks later someone notices the revenue dashboard is wrong, you trace it back, and find that one column started arriving as strin…

## What’s new and why it matters
Bad data is quiet. That's the problem. Your pipeline doesn't crash. Your tests pass. Three weeks later someone notices the revenue dashboard is wrong, you trace it back, and find that one column started arriving as strings six weeks ago. The ETL swallowed it. The warehouse stored it. Everything looked fine. I've debugged enough of these to know the pattern. The fix is always obvious in retrospect — validate the data before it enters the system. The hard part is actually doing it without adding another tool, another config file, another YAML-driven framework to maintain. So I built DataScreenIQ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/appdeviq/how-i-built-a-data-quality-api-that-runs-at-the-edge-in-milliseconds-514c

## Related notes
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-03-28-tinybird-has-a-free-real-time-analytics-api-query-billions-of-rows-in-milliseconds]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-03-24-a-day-in-the-life-of-a-data-engineer-real-talk-no-filter]]
- [[2026-03-11-i-built-a-python-csv-cleaner-that-fixes-messy-data-in-one-command]]
