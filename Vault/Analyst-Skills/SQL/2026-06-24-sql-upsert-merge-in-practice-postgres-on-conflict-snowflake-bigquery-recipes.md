---
title: 'SQL UPSERT / MERGE in Practice: Postgres ON CONFLICT, Snowflake & BigQuery
  Recipes'
date: '2026-06-24'
source: https://dev.to/gowthampotureddi/sql-upsert-merge-in-practice-postgres-on-conflict-snowflake-bigquery-recipes-2kle
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-06-04-sql-if-iif-nullif-null-handling-cheat-sheet-for-data-engineers]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-23-sql-merge-upsert-patterns-postgres-snowflake-bigquery-databricks-compared]]'
status: unread
---

> **TL;DR:** sql upsert is the one DDL pattern every data engineer writes weekly and almost every interview question hides behind — and the one most candidates flunk because they conflate the intent (insert-if-new, update-if-exists)…

## What’s new and why it matters
sql upsert is the one DDL pattern every data engineer writes weekly and almost every interview question hides behind — and the one most candidates flunk because they conflate the intent (insert-if-new, update-if-exists) with the statement ( MERGE INTO … ) and then memorise the wrong dialect's syntax. UPSERT is a concept; MERGE is one of three implementations. Postgres ships INSERT … ON CONFLICT … DO UPDATE . MySQL ships INSERT … ON DUPLICATE KEY UPDATE . Snowflake, BigQuery, Databricks, and now Postgres 15+ all ship the ANSI MERGE INTO … WHEN MATCHED / WHEN NOT MATCHED . The right answer in 20…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowthampotureddi/sql-upsert-merge-in-practice-postgres-on-conflict-snowflake-bigquery-recipes-2kle

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-06-04-sql-if-iif-nullif-null-handling-cheat-sheet-for-data-engineers]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-23-sql-merge-upsert-patterns-postgres-snowflake-bigquery-databricks-compared]]
