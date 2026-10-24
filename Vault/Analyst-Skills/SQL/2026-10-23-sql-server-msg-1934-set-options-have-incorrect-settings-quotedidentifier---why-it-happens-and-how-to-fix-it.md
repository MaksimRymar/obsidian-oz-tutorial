---
title: 'SQL Server Msg 1934: ''SET Options Have Incorrect Settings: QUOTED_IDENTIFIER''
  - Why It Happens and How to Fix It'
date: '2026-10-23'
source: https://dev.to/kausarraza/sql-server-msg-1934-set-options-have-incorrect-settings-quotedidentifier-why-it-happens-and-3490
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** This is the error, exactly as SQL Server printed it to me while I was fixing this site: Msg 1934, Level 16, State 1, Line 1 UPDATE failed because the following SET options have incorrect settings: 'QUOTED_IDENTIFIER'. Ve…

## What’s new and why it matters
This is the error, exactly as SQL Server printed it to me while I was fixing this site: Msg 1934, Level 16, State 1, Line 1 UPDATE failed because the following SET options have incorrect settings: 'QUOTED_IDENTIFIER'. Verify that SET options are correct for use with indexed views and/or indexes on computed columns and/or filtered indexes and/or query notifications and/or XML data type methods and/or spatial index operations. I was fixing a broken profile photo on this site by updating one row in the AspNetUsers table from the command line. The same table is updated every day by the ASP.NET Cor…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kausarraza/sql-server-msg-1934-set-options-have-incorrect-settings-quotedidentifier-why-it-happens-and-3490

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
