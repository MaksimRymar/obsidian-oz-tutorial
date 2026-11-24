---
title: How to chart SBA data in Python without calling every match a specialist
date: '2026-11-24'
source: https://dev.to/dataspryva/how-to-chart-sba-data-in-python-without-calling-every-match-a-specialist-4bp1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-10-23-your-creator-count-may-be-a-pagination-ceiling-in-disguise]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-09-09-sql-joins]]'
status: unread
---

> **TL;DR:** Your supplier chart is ready for the manager, until the same firm lands in several industry bars. The uncomfortable question is whether those bars describe its main business or everything it lists. An industry match can…

## What’s new and why it matters
Your supplier chart is ready for the manager, until the same firm lands in several industry bars. The uncomfortable question is whether those bars describe its main business or everything it lists. An industry match can be a secondary classification: naicsPrimaryOnly defaults to false . A matching NAICS code doesn't establish that the industry is the firm's primary classification. Calling every match a specialist gives the chart a stronger claim than the records support. What does an industry match actually mean? For supplier discovery, matching any listed industry can be useful. For a chart a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataspryva/how-to-chart-sba-data-in-python-without-calling-every-match-a-specialist-4bp1

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-10-23-your-creator-count-may-be-a-pagination-ceiling-in-disguise]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-09-09-sql-joins]]
