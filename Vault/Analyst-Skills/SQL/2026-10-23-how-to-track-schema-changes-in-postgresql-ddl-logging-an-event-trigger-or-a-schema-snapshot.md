---
title: 'How to Track Schema Changes in PostgreSQL: DDL Logging, an Event Trigger or
  a Schema Snapshot'
date: '2026-10-23'
source: https://dev.to/tbson87/how-to-track-schema-changes-in-postgresql-ddl-logging-an-event-trigger-or-a-schema-snapshot-5g91
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Pick by the question you need answered. log_statement = 'ddl' records what was attempted, rolled-back st…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Pick by the question you need answered. log_statement = 'ddl' records what was attempted, rolled-back statements included, and misses DDL run inside a DO block or function. An event trigger records committed changes with the login that made them, but only a superuser can install it, and a superuser can switch it off without leaving a trace in it. A schema snapshot compared with the live database shows what is different now, however it got there, but not who did it. There are thre…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/how-to-track-schema-changes-in-postgresql-ddl-logging-an-event-trigger-or-a-schema-snapshot-5g91

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
