---
title: To SQL or to Python; there is another problem
date: '2026-10-22'
source: https://dev.to/sudeephazra/to-sql-or-to-python-there-is-another-problem-26gc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** A recent r/dataengineering discussion described a familiar disagreement. A team was moving millions of daily records into Databricks. Python already handled ingestion, but one engineer wanted the silver-layer transformat…

## What’s new and why it matters
A recent r/dataengineering discussion described a familiar disagreement. A team was moving millions of daily records into Databricks. Python already handled ingestion, but one engineer wanted the silver-layer transformations in Python as well. Other team members preferred SQL because more people could read and maintain it. The discussion quickly became a vote for a language. SQL is easier to read. Python is easier to test. SQL is declarative. Python is proper engineering. One will scale; the other will not. Most of those claims are too broad to guide a platform decision. For structured Spark t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sudeephazra/to-sql-or-to-python-there-is-another-problem-26gc

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
