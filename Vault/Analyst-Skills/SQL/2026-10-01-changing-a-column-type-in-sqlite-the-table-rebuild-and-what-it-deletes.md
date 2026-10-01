---
title: 'Changing a Column Type in SQLite: The Table Rebuild and What It Deletes'
date: '2026-10-01'
source: https://dev.to/tbson87/changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes-do1
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: SQLite cannot change a column's type in place, so you copy the table into a new one with the right type,…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: SQLite cannot change a column's type in place, so you copy the table into a new one with the right type, drop the old one and rename. Done carelessly, that rebuild deletes child rows through ON DELETE CASCADE when PRAGMA foreign_keys = OFF is run inside the transaction, drops every trigger and index on the table, and leaves values that do not convert stored as text in the new numeric column. SQLite cannot change a column's type with ALTER TABLE . The only way is a table rebuild:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes-do1

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
