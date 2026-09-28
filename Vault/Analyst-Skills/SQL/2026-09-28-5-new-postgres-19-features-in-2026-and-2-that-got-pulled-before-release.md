---
title: 5 New Postgres 19 Features in 2026 (And 2 That Got Pulled Before Release)
date: '2026-09-28'
source: https://dev.to/astraedus/5-new-postgres-19-features-in-2026-and-2-that-got-pulled-before-release-5c18
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-16-writing-a-postgres-seed-script-that-survives-the-next-migration]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-14-why-the-index-i-added-made-my-query-slower]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** If you read a "what's new in Postgres 19" post this summer, two of its headline features are gone. SQL/PGQ graph queries and FOR PORTION OF temporal updates were both reverted in September, weeks before release. Beta 4 s…

## What’s new and why it matters
If you read a "what's new in Postgres 19" post this summer, two of its headline features are gone. SQL/PGQ graph queries and FOR PORTION OF temporal updates were both reverted in September, weeks before release. Beta 4 shipped on September 24, the release candidate is due in early October, and GA may follow the same month. Here's what actually made it, the five I'd use in an app: INSERT ... ON CONFLICT DO SELECT , IGNORE NULLS in window functions, WAIT FOR LSN , REPACK CONCURRENTLY , and pg_plan_advice . I run a handful of consumer apps on hosted Postgres. Every supabase/config.toml I own stil…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/astraedus/5-new-postgres-19-features-in-2026-and-2-that-got-pulled-before-release-5c18

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-16-writing-a-postgres-seed-script-that-survives-the-next-migration]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-14-why-the-index-i-added-made-my-query-slower]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
