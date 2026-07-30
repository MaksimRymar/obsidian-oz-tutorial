---
title: ON DELETE CASCADE Is Invisible in Your ERD and in Your Database Logs
date: '2026-07-30'
source: https://dev.to/tbson87/on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs-4pdf
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]'
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A cascading delete can travel through several tables, and neither a typical diagram nor MySQL's binlog w…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A cascading delete can travel through several tables, and neither a typical diagram nor MySQL's binlog will tell you how far it went - InnoDB runs cascades inside the storage engine, so child deletions never reach the SQL layer. Schemity stores ON DELETE and ON UPDATE on every relationship, draws a bold crow's foot at the child end of any relationship set to CASCADE, and surfaces a change to that action in the migration SQL diff before it runs, so the reach of a delete is readabl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs-4pdf

## Related notes
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
