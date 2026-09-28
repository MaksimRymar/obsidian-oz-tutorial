---
title: 'Your dashboard is green and the number is wrong: the SQL checks I schedule
  next to every metric'
date: '2026-09-28'
source: https://dev.to/refaeldakar/your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric-2bka
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-13-time-series-charts-in-sql-bucketing-gap-filling-and-time-zones-that-dont-lie]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** Most broken dashboards don't look broken. The chart renders, the numbers are plausible, the pipeline says success. Then someone in finance asks why last month's revenue changed after the fact, and you find out a join has…

## What’s new and why it matters
Most broken dashboards don't look broken. The chart renders, the numbers are plausible, the pipeline says success. Then someone in finance asks why last month's revenue changed after the fact, and you find out a join has been double-counting refunds since a schema change three weeks ago. Pipeline monitoring doesn't catch this. The job ran fine. It just produced the wrong number. What does catch it is a handful of boring SQL queries that run on a schedule and complain when the data stops looking like itself. Here's the set I start with. The examples are Postgres, but they translate to any wareh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refaeldakar/your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric-2bka

## Related notes
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-13-time-series-charts-in-sql-bucketing-gap-filling-and-time-zones-that-dont-lie]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
