---
title: 'Column Comments in PostgreSQL and MySQL: How to Document Columns Without a
  Migration'
date: '2026-08-21'
source: https://dev.to/tbson87/column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration-2no0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-17-export-a-database-data-dictionary-html-markdown-and-excel-from-your-erd]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-02-ssms-database-diagrams-your-erd-is-trapped-inside-the-database-it-documents]]'
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The database has a built-in place to document a column - COMMENT ON COLUMN in PostgreSQL, the COMMENT at…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The database has a built-in place to document a column - COMMENT ON COLUMN in PostgreSQL, the COMMENT attribute in MySQL - and almost nobody fills it in, because a sentence of prose has to travel the same path as a schema change: a migration file, a review, a deploy. Schemity keeps field descriptions in the diagram instead, where editing one generates no SQL, reads existing database comments in on import, and exports the result as a data dictionary. You can document a database co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration-2no0

## Related notes
- [[2026-08-17-export-a-database-data-dictionary-html-markdown-and-excel-from-your-erd]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-02-ssms-database-diagrams-your-erd-is-trapped-inside-the-database-it-documents]]
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
