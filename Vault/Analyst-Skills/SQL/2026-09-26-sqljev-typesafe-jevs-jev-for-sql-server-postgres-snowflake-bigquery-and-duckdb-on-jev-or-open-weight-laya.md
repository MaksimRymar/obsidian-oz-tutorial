---
title: 'sqljev: TypeSafe Jev''s jev() for SQL Server, Postgres, Snowflake, BigQuery
  and DuckDB, on Jev or Open-Weight Laya'
date: '2026-09-26'
source: https://dev.to/aiexplore369zoho/where-the-customer-is-angry-plain-english-sql-conditions-on-eight-databases-answered-by-an-1fnj
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** There is a whole class of questions SQL cannot ask. Not "tickets created this week"; SQL is good at that. "Tickets where the customer threatens to cancel." "Contracts that mention a price guarantee." "Adverse-event repor…

## What’s new and why it matters
There is a whole class of questions SQL cannot ask. Not "tickets created this week"; SQL is good at that. "Tickets where the customer threatens to cancel." "Contracts that mention a price guarantee." "Adverse-event reports that describe liver injury." You cannot say those with = , LIKE or a regex, so they get exported to a notebook, judged by a model there, and the answers never make it back into the database where the rest of the question lives. sqljev , released today as 0.1.0, puts that judgment back inside the query. It adds jev() , jev_prob() and jev_choice() to SQL Server, PostgreSQL, My…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aiexplore369zoho/where-the-customer-is-angry-plain-english-sql-conditions-on-eight-databases-answered-by-an-1fnj

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-15-sql-joins-explained]]
