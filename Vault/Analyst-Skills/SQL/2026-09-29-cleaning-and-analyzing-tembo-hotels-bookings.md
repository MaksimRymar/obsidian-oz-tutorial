---
title: Cleaning and Analyzing Tembo Hotel's Bookings
date: '2026-09-29'
source: https://dev.to/david_mwandairo/cleaning-and-analyzing-tembo-hotels-bookings-41o5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tableau'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
- '[[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** One guest at Tembo Hotel & Suites checked out three days before checking in. The spreadsheet says so. It also spells Nairobi as Nairobi and as NAIROBI , files a town called Thikax under guest cities, and writes January d…

## What’s new and why it matters
One guest at Tembo Hotel & Suites checked out three days before checking in. The spreadsheet says so. It also spells Nairobi as Nairobi and as NAIROBI , files a town called Thikax under guest cities, and writes January dates as 10/01/2024 , 01-12-2024 and 28-01-24 , three formats in one column. That spreadsheet is the whole booking history of a mid-range business hotel in Nairobi, open since 2023. The Hotel Director wants to know which rooms earn the most, which months are busiest, how the staff are doing and whether guests are happy. Nobody can answer those questions from a file like this. An…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/david_mwandairo/cleaning-and-analyzing-tembo-hotels-bookings-41o5

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
- [[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
