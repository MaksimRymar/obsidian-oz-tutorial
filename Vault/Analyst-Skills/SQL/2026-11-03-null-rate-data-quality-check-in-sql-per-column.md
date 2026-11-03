---
title: Null rate data quality check in SQL, per column
date: '2026-11-03'
source: https://dev.to/refaeldakar/null-rate-data-quality-check-in-sql-per-column-394k
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
status: unread
---

> **TL;DR:** A dashboard goes wrong quietly in two ways. The rows stop arriving, which a freshness or row count check catches. Or the rows keep arriving and one column fills with nulls. Nothing errors, the load job is green, and reve…

## What’s new and why it matters
A dashboard goes wrong quietly in two ways. The rows stop arriving, which a freshness or row count check catches. Or the rows keep arriving and one column fills with nulls. Nothing errors, the load job is green, and revenue by coupon quietly drops to zero. A null rate check is the cheap answer to the second one. Plain Postgres SQL below; the full write-up (every column at once, per-role tolerances, backtesting) is on my blog. Null rate for one column SELECT count ( * ) AS total , round ( 100 . 0 * count ( * ) FILTER ( WHERE email IS NULL ) / NULLIF ( count ( * ), 0 ), 2 ) AS email_null_pct FRO…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refaeldakar/null-rate-data-quality-check-in-sql-per-column-394k

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
