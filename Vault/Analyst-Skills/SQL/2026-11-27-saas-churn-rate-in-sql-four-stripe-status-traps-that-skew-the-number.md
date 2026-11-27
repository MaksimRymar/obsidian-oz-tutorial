---
title: 'SaaS churn rate in SQL: four Stripe status traps that skew the number'
date: '2026-11-27'
source: https://dev.to/vasyl_popovych_37a71efb3d/saas-churn-rate-in-sql-four-stripe-status-traps-that-skew-the-number-2k36
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-24-sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-you-most-need-to-call]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
status: unread
---

> **TL;DR:** Customer churn rate is one division: customers you lost during a period, divided by customers you had at the start of it. It takes ten seconds to write on a whiteboard. Getting the same number out of a Stripe subscriptio…

## What’s new and why it matters
Customer churn rate is one division: customers you lost during a period, divided by customers you had at the start of it. It takes ten seconds to write on a whiteboard. Getting the same number out of a Stripe subscriptions table takes longer. The table has no "customer left on this date" column. It has statuses, and a few of them look like churn without being churn. If your query groups canceled subscriptions by canceled_at , it is probably counting some customers in the wrong month and some who never left. Below is a PostgreSQL query that handles those cases, plus a small dataset you can run…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vasyl_popovych_37a71efb3d/saas-churn-rate-in-sql-four-stripe-status-traps-that-skew-the-number-2k36

## Related notes
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-24-sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-you-most-need-to-call]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
