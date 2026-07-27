---
title: Following ROWIDs Through an Oracle Unique Index Update
date: '2026-07-26'
source: https://dev.to/franckpachot/following-rowids-through-an-oracle-unique-index-update-2lc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]'
- '[[2026-06-15-cross-row-validation-risk-in-postgresql-check-constraints]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]'
- '[[2026-07-16-oracle-ora-01452-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** I've always been amazed by how Oracle Database handles updates to a unique column—performing set-based operations that don't violate the unique constraint, yet when executed row by row, it temporarily permits duplicates.…

## What’s new and why it matters
I've always been amazed by how Oracle Database handles updates to a unique column—performing set-based operations that don't violate the unique constraint, yet when executed row by row, it temporarily permits duplicates. SQL > create table franck ( val int unique ); Table created . SQL > insert into franck values ( - 1 ) , ( 1 ) ; 2 rows created . SQL > select val from franck ; VAL ---------- - 1 1 SQL > update franck set val =- val ; 2 rows updated . SQL > select val from franck ; VAL ---------- 1 - 1 From a SQL perspective, this is expected behavior, but not all databases support it without…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/following-rowids-through-an-oracle-unique-index-update-2lc

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]
- [[2026-06-15-cross-row-validation-risk-in-postgresql-check-constraints]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]
- [[2026-07-16-oracle-ora-01452-error-causes-and-solutions-complete-guide]]
