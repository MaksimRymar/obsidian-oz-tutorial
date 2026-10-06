---
title: Three months of sales vanished, and every dbt run was green
date: '2026-10-05'
source: https://dev.to/vijaykumar13/three-months-of-sales-vanished-and-every-dbt-run-was-green-c9c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-28-your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric]]'
status: unread
---

> **TL;DR:** In this article I'll show you how a dbt incremental model that looked perfectly reasonable wiped out three months of finance data, why none of our checks caught it, and how we fixed it without a full refresh. If you use…

## What’s new and why it matters
In this article I'll show you how a dbt incremental model that looked perfectly reasonable wiped out three months of finance data, why none of our checks caught it, and how we fixed it without a full refresh. If you use delete+insert anywhere in your project, it's worth ten minutes to check you aren't doing the same thing. Some background I'm an analytics engineer at a leading North American housewares company. We are moving our SAP reporting off SAP BW and onto Snowflake and dbt, one report at a time. One of those reports is a gross-to-net finance report built from SAP's general-ledger line i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vijaykumar13/three-months-of-sales-vanished-and-every-dbt-run-was-green-c9c

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-28-your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric]]
