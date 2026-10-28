---
title: 'MySQL Workbench Alternative: ER Diagrams Past 250 Tables'
date: '2026-10-28'
source: https://dev.to/tbson87/mysql-workbench-alternative-er-diagrams-past-250-tables-1bk8
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-06-drawsql-alternative-an-offline-desktop-erd-tool-with-no-table-limits]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: MySQL Workbench 26, Oracle's rebuild, has no ER diagram: modeling lives on only in Workbench 8.0, which…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: MySQL Workbench 26, Oracle's rebuild, has no ER diagram: modeling lives on only in Workbench 8.0, which is no longer maintained. And that diagram struggles in two places: at 250 or more objects it may refuse to place them on a diagram, and it draws a relationship only where MySQL stored a foreign key, so schemas from apps that never declared their keys open with no lines. Schemity places every table it reads, infers the missing relations from column names as dashed virtual relati…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/mysql-workbench-alternative-er-diagrams-past-250-tables-1bk8

## Related notes
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-06-drawsql-alternative-an-offline-desktop-erd-tool-with-no-table-limits]]
