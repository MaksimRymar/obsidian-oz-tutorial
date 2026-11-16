---
title: Why SELECT Before INSERT Causes Duplicate Records
date: '2026-11-16'
source: https://dev.to/doogal/why-select-before-insert-causes-duplicate-records-3bna
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-09-database-indexing-101-how-to-stop-slow-sql-queries-before-they-kill-your-app]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-05-15-avoiding-range-overlaps-in-postgresql-with-exclude-constraint-beats-serializable-or-assertions]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
- '[[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]'
status: unread
---

> **TL;DR:** Quick Answer: Checking whether a record exists with a SELECT query before executing an INSERT fails under concurrent traffic. When two requests arrive simultaneously, both queries see zero records and proceed to insert d…

## What’s new and why it matters
Quick Answer: Checking whether a record exists with a SELECT query before executing an INSERT fails under concurrent traffic. When two requests arrive simultaneously, both queries see zero records and proceed to insert duplicates. To reliably prevent duplicate entries, enforce a database-level unique constraint and handle the resulting violation error gracefully in your application layer. We have all seen this pattern in codebases: you have a table where a column like email must stay unique. The most intuitive approach is to query the database first. If the row does not exist, your application…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/doogal/why-select-before-insert-causes-duplicate-records-3bna

## Related notes
- [[2026-11-09-database-indexing-101-how-to-stop-slow-sql-queries-before-they-kill-your-app]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-05-15-avoiding-range-overlaps-in-postgresql-with-exclude-constraint-beats-serializable-or-assertions]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
- [[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]
