---
title: Confused by UNBOUNDED PRECEDING and CURRENT ROW in SQL window functions? I
  was too. This guide breaks down exactly how window frames work and uses LeetCode
  1204 to show how they create a running total step by step.
date: '2026-08-23'
source: https://dev.to/saamiabbaskhan/confused-by-unbounded-preceding-and-current-row-in-sql-window-functions-i-was-too-this-guide-5528
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tableau'
- '#tutorial'
related:
- '[[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]'
- '[[2026-08-13-need-to-calculate-running-totals-or-rank-rows-without-group-by-headaches-enter-sql-window-functions-lets-break-down-how-]]'
- '[[2026-04-09-late-night-chronicles-5-your-first-mysql-commands]]'
- '[[2026-02-21-why-your-sql-window-functions-betray-you-in-cloud-ssms-vs-snowflake]]'
- '[[2026-03-11-why-sum-over-order-by-sometimes-feels-wrong-a-practical-guide-to-sql-window-frames]]'
- '[[2026-05-30-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
status: unread
---

> **TL;DR:** SQL Window Frames Explained: How UNBOUNDED PRECEDING Creates a Running Total Saami abbas Khan Saami abbas Khan Saami abbas Khan Follow Aug 23 SQL Window Frames Explained: How UNBOUNDED PRECEDING Creates a Running Total #…

## What’s new and why it matters
SQL Window Frames Explained: How UNBOUNDED PRECEDING Creates a Running Total Saami abbas Khan Saami abbas Khan Saami abbas Khan Follow Aug 23 SQL Window Frames Explained: How UNBOUNDED PRECEDING Creates a Running Total # sql # database # beginners # mysql 6 reactions Add Comment 9 min read

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saamiabbaskhan/confused-by-unbounded-preceding-and-current-row-in-sql-window-functions-i-was-too-this-guide-5528

## Related notes
- [[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]
- [[2026-08-13-need-to-calculate-running-totals-or-rank-rows-without-group-by-headaches-enter-sql-window-functions-lets-break-down-how-]]
- [[2026-04-09-late-night-chronicles-5-your-first-mysql-commands]]
- [[2026-02-21-why-your-sql-window-functions-betray-you-in-cloud-ssms-vs-snowflake]]
- [[2026-03-11-why-sum-over-order-by-sometimes-feels-wrong-a-practical-guide-to-sql-window-frames]]
- [[2026-05-30-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
