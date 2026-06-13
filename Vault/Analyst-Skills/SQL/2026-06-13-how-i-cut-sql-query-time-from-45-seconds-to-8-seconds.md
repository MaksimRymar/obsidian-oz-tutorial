---
title: '# How I Cut SQL Query Time from 45 Seconds to 8 Seconds'
date: '2026-06-13'
source: https://dev.to/danielnnadi/-how-i-cut-sql-query-time-from-45-seconds-to-8-seconds-cba
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
- '[[2026-06-12-how-i-cut-sql-query-time-from-45-seconds-to-8-seconds-on-23-million-rows]]'
- '[[2026-05-17-spur-data-engineering-interview-questions-full-de-prep-guide]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
status: unread
---

> **TL;DR:** When I joined the data team at an automotive parts company, the inventory query everyone relied on took 45 seconds to run. Real-time reporting was impossible. This is how I brought that query down to 8 seconds. The Probl…

## What’s new and why it matters
When I joined the data team at an automotive parts company, the inventory query everyone relied on took 45 seconds to run. Real-time reporting was impossible. This is how I brought that query down to 8 seconds. The Problem The database had an inventory table with 2.3M+ rows. The query was doing full table scans on every execution. The Fix 1. Read the execution plan - Found correlated subqueries running 500+ times 2. Replaced subquery with CTE: sql - Before: 45 seconds SELECT * FROM inventory i WHERE (SELECT MAX(date) FROM orders o WHERE o.sku_id = i.sku_id) IS NOT NULL - After: 8 seconds WITH…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danielnnadi/-how-i-cut-sql-query-time-from-45-seconds-to-8-seconds-cba

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
- [[2026-06-12-how-i-cut-sql-query-time-from-45-seconds-to-8-seconds-on-23-million-rows]]
- [[2026-05-17-spur-data-engineering-interview-questions-full-de-prep-guide]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
