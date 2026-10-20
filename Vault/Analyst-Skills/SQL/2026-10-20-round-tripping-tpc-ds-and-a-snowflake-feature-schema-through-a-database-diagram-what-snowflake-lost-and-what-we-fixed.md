---
title: 'Round-Tripping TPC-DS and a Snowflake Feature Schema Through a Database Diagram:
  What Snowflake Lost and What We Fixed'
date: '2026-10-20'
source: https://dev.to/tbson87/round-tripping-tpc-ds-and-a-snowflake-feature-schema-through-a-database-diagram-what-snowflake-570a
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: We put two Snowflake schemas through Schemity, TPC-DS as Snowflake ships it and a hand-written schema us…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: We put two Snowflake schemas through Schemity, TPC-DS as Snowflake ships it and a hand-written schema using Snowflake's own features, and rebuilt each in a fresh schema from the SQL Schemity wrote. Before this round of fixes the second script stopped partway, because a table with an expression clustering key could not be read; every clustering key and TRANSIENT was dropped, an identity lost its start and step, and TPC-DS's 17 single-column surrogate keys came back as AUTOINCREMEN…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/round-tripping-tpc-ds-and-a-snowflake-feature-schema-through-a-database-diagram-what-snowflake-570a

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
