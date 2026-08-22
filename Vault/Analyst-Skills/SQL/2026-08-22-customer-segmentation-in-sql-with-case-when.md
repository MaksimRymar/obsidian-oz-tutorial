---
title: Customer Segmentation in SQL With CASE WHEN
date: '2026-08-22'
source: https://dev.to/michaelnocito/customer-segmentation-in-sql-with-case-when-4j20
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you can turn a table of transactions into named customer groups, count and total each group, cross two segmentations into a matrix, choo…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you can turn a table of transactions into named customer groups, count and total each group, cross two segmentations into a matrix, choose between cut-offs you picked and cut-offs the data picked, and prove that every customer landed in exactly one group. It is about twenty-five minutes, and every query and result below was run. Here is what to do today, on the segmentation you already have. Count the customers in each segment and add them up. If the total is less than your customer count, some rows fell throug…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/customer-segmentation-in-sql-with-case-when-4j20

## Related notes
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
