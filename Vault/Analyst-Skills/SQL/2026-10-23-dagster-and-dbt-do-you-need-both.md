---
title: 'Dagster and dbt: do you need both?'
date: '2026-10-23'
source: https://dev.to/mohammed_arshadansari_f2/dagster-and-dbt-do-you-need-both-27l7
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-27-bruin-sql-python-pipelines-in-one-framework-with-built-in-quality-checks]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-09-27-prophecy-visual-git-backed-low-code-spark-sql-pipelines-for-the-enterprise]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
status: unread
---

> **TL;DR:** "Why use dbt if I have Dagster?" is the number-two Google result for this topic, and it's a Reddit thread. That tells you the question is real. People see two tools that both draw a lineage graph, both run on a schedule,…

## What’s new and why it matters
"Why use dbt if I have Dagster?" is the number-two Google result for this topic, and it's a Reddit thread. That tells you the question is real. People see two tools that both draw a lineage graph, both run on a schedule, and both run tests, and they wonder if they are paying twice. They aren't, quite. dbt is a SQL transformation framework . Dagster is an orchestrator . They overlap in the middle, and the overlap is where the confusion lives. My own production pipeline runs on Dagster with no dbt at all, so I'll also say when skipping dbt is the right call. What each tool actually does dbt take…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammed_arshadansari_f2/dagster-and-dbt-do-you-need-both-27l7

## Related notes
- [[2026-09-27-bruin-sql-python-pipelines-in-one-framework-with-built-in-quality-checks]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-09-27-prophecy-visual-git-backed-low-code-spark-sql-pipelines-for-the-enterprise]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
