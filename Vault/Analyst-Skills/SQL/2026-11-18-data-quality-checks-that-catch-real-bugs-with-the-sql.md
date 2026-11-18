---
title: Data quality checks that catch real bugs, with the SQL
date: '2026-11-18'
source: https://dev.to/mohammed_arshadansari_f2/data-quality-checks-that-catch-real-bugs-with-the-sql-24m4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-25-what-is-a-data-quality-check-types-where-to-run-them-and-examples]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-09-03-dbt-incremental-models-duplicate-rows-when-uniquekey-is-null-and-the-fix-is-off-by-default]]'
- '[[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]'
status: unread
---

> **TL;DR:** Data quality checks are small queries that fail when data breaks a rule you know must hold. Most lists of them start with not-null and uniqueness. Those are worth having. In my experience they are also the checks that al…

## What’s new and why it matters
Data quality checks are small queries that fail when data breaks a rule you know must hold. Most lists of them start with not-null and uniqueness. Those are worth having. In my experience they are also the checks that almost never fire, because the source system already enforces them. The checks that caught real bugs in my pipelines were different: a row count that was too low, a date that was not really new, a number that was NaN instead of NULL. This post gives you the common checks as runnable SQL, then the ones that earned their place, with the numbers. The examples run as-is in DuckDB and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammed_arshadansari_f2/data-quality-checks-that-catch-real-bugs-with-the-sql-24m4

## Related notes
- [[2026-10-25-what-is-a-data-quality-check-types-where-to-run-them-and-examples]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-09-03-dbt-incremental-models-duplicate-rows-when-uniquekey-is-null-and-the-fix-is-off-by-default]]
- [[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]
