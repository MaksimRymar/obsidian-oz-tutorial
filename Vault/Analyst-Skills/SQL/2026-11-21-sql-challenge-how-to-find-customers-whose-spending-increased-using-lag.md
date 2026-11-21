---
title: 'SQL Challenge : How to Find Customers Whose Spending Increased Using LAG()'
date: '2026-11-21'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-how-to-find-customers-whose-spending-increased-using-lag-1m5n
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-20-sql-challenge-compare-todays-sales-with-yesterdays-sales-using-lag-in-oracle-sql]]'
- '[[2026-11-18-sql-challenge-can-you-find-the-second-purchase-of-every-customer-using-rownumber]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-11-18-query-a-csv-file-with-sql-without-setting-up-a-database]]'
- '[[2026-10-17-joins-in-sql]]'
status: unread
---

> **TL;DR:** When working with customer purchase data, looking at individual orders doesn't always tell us the full story. Sometimes, we need to compare a customer's current purchase with their previous purchase to understand whether…

## What’s new and why it matters
When working with customer purchase data, looking at individual orders doesn't always tell us the full story. Sometimes, we need to compare a customer's current purchase with their previous purchase to understand whether their spending is increasing or decreasing. For example: Did the customer spend more on their latest order? Has their purchase amount increased compared to the previous order? Which customers are spending more over time? We can solve this using the SQL window function "LAG()". In this tutorial, let's see how to use "LAG()" with "PARTITION BY" and "ORDER BY" to compare customer…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-how-to-find-customers-whose-spending-increased-using-lag-1m5n

## Related notes
- [[2026-11-20-sql-challenge-compare-todays-sales-with-yesterdays-sales-using-lag-in-oracle-sql]]
- [[2026-11-18-sql-challenge-can-you-find-the-second-purchase-of-every-customer-using-rownumber]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-11-18-query-a-csv-file-with-sql-without-setting-up-a-database]]
- [[2026-10-17-joins-in-sql]]
