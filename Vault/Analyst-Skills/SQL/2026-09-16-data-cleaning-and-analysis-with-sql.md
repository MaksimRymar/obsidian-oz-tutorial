---
title: Data Cleaning and Analysis with SQL
date: '2026-09-16'
source: https://dev.to/alex_murithi/data-cleaning-and-analysis-with-sql-2f4c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]'
- '[[2026-09-08-sql-a-messy-csv-and-a-ceo-waiting-for-answers-the-safariconnect-project]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
status: unread
---

> **TL;DR:** 1. Problem Statement SafariConnect is a transport booking platform handling thousands of trips across Kenya. The raw CSV data was messy: Dates in multiple formats ( 2024-01-08 , 17/01/2024 , 01-18-2024 ) Phone numbers wi…

## What’s new and why it matters
1. Problem Statement SafariConnect is a transport booking platform handling thousands of trips across Kenya. The raw CSV data was messy: Dates in multiple formats ( 2024-01-08 , 17/01/2024 , 01-18-2024 ) Phone numbers with different prefixes ( +2547… , 07… , 0745-… ) Mixed casing in names and cities Multiple variants of seat classes ( Economy , eco , BUSINESS CLASS ) Payment methods ( M-Pesa , mpesa , Cash , CARD ) Invalid ratings ( 0 , 6 ) The challenge: clean the data, design a proper database, and run SQL analyses to answer six core business questions . 2. Data & Database Structure Staging…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alex_murithi/data-cleaning-and-analysis-with-sql-2f4c

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]
- [[2026-09-08-sql-a-messy-csv-and-a-ceo-waiting-for-answers-the-safariconnect-project]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
