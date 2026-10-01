---
title: 'A PostgreSQL Role That Reads the Schema but Not the Data: What to Grant'
date: '2026-10-01'
source: https://dev.to/tbson87/a-postgresql-role-that-reads-the-schema-but-not-the-data-what-to-grant-20ep
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Grant CONNECT on the database and USAGE on the schema, and nothing on the tables: the role can then read…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Grant CONNECT on the database and USAGE on the schema, and nothing on the tables: the role can then read the whole structure from pg_catalog while every SELECT on a table fails with permission denied . The catch is that information_schema hides everything the role has no privilege on, so tools built on it show an empty schema, and the catalogue still shows view definitions, function bodies, comments and row estimates. A PostgreSQL role can read a database's entire structure witho…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/a-postgresql-role-that-reads-the-schema-but-not-the-data-what-to-grant-20ep

## Related notes
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
