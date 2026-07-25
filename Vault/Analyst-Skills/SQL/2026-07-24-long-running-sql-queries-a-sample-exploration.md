---
title: 'Long Running SQL Queries: a sample exploration'
date: '2026-07-24'
source: https://dev.to/intersystems/long-running-sql-queries-a-sample-exploration-34b4
domain: SQL
relevance: 🟡
tags:
- '#presentations'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-05-19-doubling-the-speed-of-an-already-fast-sql-parser-using-ai]]'
status: unread
---

> **TL;DR:** Here at InterSystems, we often deal with massive datasets of structured data. It’s not uncommon to see customers with tables spanning >100 fields and >1 billion rows, each table totaling hundred of GB of data. Now imagin…

## What’s new and why it matters
Here at InterSystems, we often deal with massive datasets of structured data. It’s not uncommon to see customers with tables spanning >100 fields and >1 billion rows, each table totaling hundred of GB of data. Now imagine joining two or three of these tables together, with a schema that wasn’t optimized for this specific use case. Just for fun, let’s say you have 10 years worth of EMR data from 20 different hospitals across your state, and you’ve been tasked with finding…. every clinician within your network who has administered a specific drug between the years of 2017-2019 to patients who re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/intersystems/long-running-sql-queries-a-sample-exploration-34b4

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-05-19-doubling-the-speed-of-an-already-fast-sql-parser-using-ai]]
