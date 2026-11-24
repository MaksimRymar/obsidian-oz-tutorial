---
title: 'SQL Server DATETIME vs DATETIME2: Which to Use, and What Converting an Existing
  Column Costs'
date: '2026-11-24'
source: https://dev.to/tbson87/sql-server-datetime-vs-datetime2-which-to-use-and-what-converting-an-existing-column-costs-5h6o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]'
- '[[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]'
- '[[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]'
- '[[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use DATETIME2(3) for new columns: it keeps exact milliseconds in 7 bytes, while DATETIME rounds to steps…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use DATETIME2(3) for new columns: it keeps exact milliseconds in 7 bytes, while DATETIME rounds to steps of 1/300 second in 8. Converting an existing column means dropping its default and indexes first, then a rewrite of every row under a schema lock, about 1.4 seconds and 106 MB of log on one million rows in our test. Pick a precision of 3 or more, or the conversion rounds stored values without an error. For a new SQL Server column, use DATETIME2(3) : it keeps exact milliseconds…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/sql-server-datetime-vs-datetime2-which-to-use-and-what-converting-an-existing-column-costs-5h6o

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]
- [[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]
- [[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]
- [[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]
