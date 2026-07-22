---
title: Why ERD Tools Draw Your 1:1 Relationship as 1:N
date: '2026-07-22'
source: https://dev.to/tbson87/why-erd-tools-draw-your-11-relationship-as-1n-3oag
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-05-26-schemaspy-vs-schemacrawler---which-database-documentation-tool-is-right-for-you]]'
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A 1:1 relationship in SQL is nothing but a foreign key with a unique constraint, so any tool that reads…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A 1:1 relationship in SQL is nothing but a foreign key with a unique constraint, so any tool that reads the key and ignores the constraint draws it as 1:N - a bug reported against MySQL Workbench in 2009 and against dbdiagram in 2025. Schemity derives cardinality from the constraint itself: toggle the foreign key's uniqueness and the relationship toggles between 1:1 and 1:N, and composite unique sets get named, colored U badges instead of one ambiguous marker. A one-to-one relati…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/why-erd-tools-draw-your-11-relationship-as-1n-3oag

## Related notes
- [[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-05-26-schemaspy-vs-schemacrawler---which-database-documentation-tool-is-right-for-you]]
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
