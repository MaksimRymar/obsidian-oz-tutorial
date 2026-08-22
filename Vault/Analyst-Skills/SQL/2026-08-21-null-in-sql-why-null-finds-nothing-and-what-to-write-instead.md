---
title: 'NULL in SQL: Why = NULL Finds Nothing and What to Write Instead'
date: '2026-08-21'
source: https://dev.to/michaelnocito/null-in-sql-why-null-finds-nothing-and-what-to-write-instead-4b64
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
- '[[2026-08-12-group-by-and-having-how-to-summarize-rows-without-getting-a-fake-answer]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 7, 2026 By the end of this page you can predict what any query does when it meets a missing value, which is the skill that separates "my query returned nothing and I do…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 7, 2026 By the end of this page you can predict what any query does when it meets a missing value, which is the skill that separates "my query returned nothing and I don't know why" from a two-second fix. You will know why = NULL matches zero rows, why one NULL can empty an entire NOT IN , and how NULLs quietly move averages, counts, groups, and sort orders. It is about twenty minutes. Here is what to actually do with it. Next time a filter returns fewer rows than you expected, ask one question first: does the column I am comparing have NULLs…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/null-in-sql-why-null-finds-nothing-and-what-to-write-instead-4b64

## Related notes
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
- [[2026-08-12-group-by-and-having-how-to-summarize-rows-without-getting-a-fake-answer]]
