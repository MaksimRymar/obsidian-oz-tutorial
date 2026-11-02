---
title: GORM counted 11 rows. PostgreSQL found 7 distinct pairs.
date: '2026-11-01'
source: https://dev.to/blucca/gorm-counted-11-rows-postgresql-found-7-distinct-pairs-1h0g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-08-20-beyond-sql-accuracy-building-evidence-chains-for-ai-data-agents]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** A count can execute successfully and still answer the wrong question. In a native Go + PostgreSQL reproduction, this GORM query returned 11 : var count int64 err := db . Table ( "fixture_pairs" ) . Distinct ( "a" , "b" )…

## What’s new and why it matters
A count can execute successfully and still answer the wrong question. In a native Go + PostgreSQL reproduction, this GORM query returned 11 : var count int64 err := db . Table ( "fixture_pairs" ) . Distinct ( "a" , "b" ) . Count ( & count ) . Error The database contained 7 distinct (a, b) pairs . err was nil. The emitted SQL was: SELECT count ( * ) FROM "fixture_pairs" ; This reproduces the public GORM issue #6798 . The measured version is commit ead4e04ba7c6a49654649131e587133b1d9f3eca , with gorm.io/driver/postgres@v1.6.0 and PostgreSQL 16.15. Name the thing you are counting Physical rows an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/blucca/gorm-counted-11-rows-postgresql-found-7-distinct-pairs-1h0g

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-08-20-beyond-sql-accuracy-building-evidence-chains-for-ai-data-agents]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
