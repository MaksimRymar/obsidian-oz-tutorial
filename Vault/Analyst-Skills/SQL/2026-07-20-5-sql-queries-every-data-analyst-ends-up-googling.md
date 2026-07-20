---
title: 5 SQL queries every data analyst ends up googling
date: '2026-07-20'
source: https://dev.to/sofrito/5-sql-queries-every-data-analyst-ends-up-googling-10hm
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
related:
- '[[2026-06-02-5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
status: unread
---

> **TL;DR:** You know the pattern. A stakeholder asks a simple-sounding question, you open your editor confident, and thirty seconds later you are back on Google typing "sql running total" for the hundredth time. Here are five of the…

## What’s new and why it matters
You know the pattern. A stakeholder asks a simple-sounding question, you open your editor confident, and thirty seconds later you are back on Google typing "sql running total" for the hundredth time. Here are five of the queries analysts re-google the most, written so you can actually run them. All examples use a small e-commerce schema ( customers , orders , order_items , products ) and PostgreSQL syntax, with notes where other dialects differ. 1. Running total (cumulative sum) The classic "revenue to date" line on every dashboard. SELECT order_date , daily_revenue , SUM ( daily_revenue ) OVE…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sofrito/5-sql-queries-every-data-analyst-ends-up-googling-10hm

## Related notes
- [[2026-06-02-5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
