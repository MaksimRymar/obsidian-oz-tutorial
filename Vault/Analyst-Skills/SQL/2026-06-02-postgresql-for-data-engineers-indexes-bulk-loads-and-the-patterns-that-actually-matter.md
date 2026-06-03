---
title: 'PostgreSQL for Data Engineers: Indexes, Bulk Loads, and the Patterns That
  Actually Matter'
date: '2026-06-02'
source: https://dev.to/de_clerke/postgresql-for-data-engineers-indexes-bulk-loads-and-the-patterns-that-actually-matter-25fl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-26-filtering-rows-and-selecting-columns-the-right-way]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-06-02-debugging-postgresql-performance]]'
status: unread
---

> **TL;DR:** The LedgerSync pipeline was inserting 1.5 million rows into PostgreSQL using pandas.to_sql() . It took four minutes per run. I switched to psycopg2's COPY command and it dropped to 18 seconds. Same data, same schema, sam…

## What’s new and why it matters
The LedgerSync pipeline was inserting 1.5 million rows into PostgreSQL using pandas.to_sql() . It took four minutes per run. I switched to psycopg2's COPY command and it dropped to 18 seconds. Same data, same schema, same machine. That is not an optimization tip. It is the difference between a pipeline that fits in an Airflow schedule and one that does not. This article is about patterns like that: the ones that matter when you are building pipelines that run on a schedule, not when you are writing ad-hoc queries. Loading Data: to_sql vs execute_values vs COPY There are three ways to write row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/de_clerke/postgresql-for-data-engineers-indexes-bulk-loads-and-the-patterns-that-actually-matter-25fl

## Related notes
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-26-filtering-rows-and-selecting-columns-the-right-way]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-06-02-debugging-postgresql-performance]]
