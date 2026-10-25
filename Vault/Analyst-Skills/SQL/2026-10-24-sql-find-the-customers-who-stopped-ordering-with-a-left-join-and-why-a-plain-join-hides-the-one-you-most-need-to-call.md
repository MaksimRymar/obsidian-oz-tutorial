---
title: 'SQL: Find the Customers Who Stopped Ordering With a LEFT JOIN (and Why a Plain
  JOIN Hides the One You Most Need to Call)'
date: '2026-10-24'
source: https://dev.to/robert_breen_d96e41ecd765/sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-17l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]'
status: unread
---

> **TL;DR:** Most small businesses don't lose customers in one dramatic phone call. They lose them quietly. A dental practice that ordered every month just stops, and nobody notices until the year-end review. The fix is a list every…

## What’s new and why it matters
Most small businesses don't lose customers in one dramatic phone call. They lose them quietly. A dental practice that ordered every month just stops, and nobody notices until the year-end review. The fix is a list every Monday: customers with no order since a given date, with their account manager next to each name so someone can call. That list is one query. But there's a trap in it, and the trap hides the customer you most need to call. Here's the query, and the trap, from my free lesson. You can paste everything into DB Fiddle (free, no account, pick MySQL). Two tables Lakeside Office Suppl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/robert_breen_d96e41ecd765/sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-17l

## Related notes
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]
