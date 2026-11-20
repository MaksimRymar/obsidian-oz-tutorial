---
title: 'SQL Challenge : Compare Today''s Sales With Yesterday''s Sales Using LAG()
  in Oracle SQL'
date: '2026-11-20'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-compare-todays-sales-with-yesterdays-sales-using-lag-in-oracle-sql-jc3
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-11-18-sql-challenge-can-you-find-the-second-purchase-of-every-customer-using-rownumber]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-11-19-sql-running-total-calculate-cumulative-daily-sales-using-sum-over-in-oracle-sql]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** When working with sales data, looking at daily revenue alone doesn't always tell the complete story. Businesses often need to compare today's sales with the previous day's sales to understand whether revenue is increasin…

## What’s new and why it matters
When working with sales data, looking at daily revenue alone doesn't always tell the complete story. Businesses often need to compare today's sales with the previous day's sales to understand whether revenue is increasing or decreasing. For example: Yesterday's sales: 15,000 Today's sales: 12,000 Difference: -3,000 How can you calculate this comparison using SQL without joining the same table with itself? The answer is the LAG() window function. In this SQL tutorial, let's solve a practical daily sales comparison problem using Oracle SQL. Understanding the Problem Suppose you have a "daily_sal…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-compare-todays-sales-with-yesterdays-sales-using-lag-in-oracle-sql-jc3

## Related notes
- [[2026-10-17-joins-in-sql]]
- [[2026-11-18-sql-challenge-can-you-find-the-second-purchase-of-every-customer-using-rownumber]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-11-19-sql-running-total-calculate-cumulative-daily-sales-using-sum-over-in-oracle-sql]]
- [[2026-09-09-sql-joins]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
