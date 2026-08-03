---
title: '9,104 rows in, 5,000 out: the silent cap that made my dashboard lie'
date: '2026-08-02'
source: https://dev.to/liam-dev/9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie-2hbk
domain: SQL
relevance: 🟡
tags:
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-06-06-i-built-a-data-contract-validator-in-pure-python-no-pandas-no-pyyaml-and-it-caught-a-30-revenue-ghost]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** I sat down to add a small thing to an internal dashboard: a NEW badge on a search-rank table, so you could tell "this keyword just broke into the rankings" from "this keyword didn't move." An afternoon of work. Then I we…

## What’s new and why it matters
I sat down to add a small thing to an internal dashboard: a NEW badge on a search-rank table, so you could tell "this keyword just broke into the rankings" from "this keyword didn't move." An afternoon of work. Then I went looking for the data to base it on, and found that the table had been reading 55% of its own rows for the last four days, without saying so. What was actually happening The page pulled raw daily rows through a generic query endpoint and folded them in the browser. The request asked for 8,000 rows. The server had this: _MAX_LIMIT = 5000 ... limit = max ( 1 , min ( limit , _MA…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/liam-dev/9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie-2hbk

## Related notes
- [[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-06-06-i-built-a-data-contract-validator-in-pure-python-no-pandas-no-pyyaml-and-it-caught-a-30-revenue-ghost]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
