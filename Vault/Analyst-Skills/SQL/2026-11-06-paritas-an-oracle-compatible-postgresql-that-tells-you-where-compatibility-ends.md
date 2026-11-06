---
title: Paritas, an Oracle-compatible PostgreSQL that tells you where compatibility
  ends
date: '2026-11-06'
source: https://dev.to/ejazarain/paritas-an-oracle-compatible-postgresql-that-tells-you-where-compatibility-ends-o6a
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
status: unread
---

> **TL;DR:** First published on the Tech Style blog . When a company moves off Oracle, most of the effort goes into converting the code. The part that hurts later is quieter. PostgreSQL is not Oracle, and in places it computes a diff…

## What’s new and why it matters
First published on the Tech Style blog . When a company moves off Oracle, most of the effort goes into converting the code. The part that hurts later is quieter. PostgreSQL is not Oracle, and in places it computes a different answer to the same expression. There is no error at build time and none in test. A pricing query returns a slightly wrong number, and a customer is the one who finds it. Paritas is our answer to that. It is PostgreSQL 18 with an Oracle mode that compiles and runs real PL/SQL: packages, triggers, collections and exceptions. It is still in development and not for sale. This…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ejazarain/paritas-an-oracle-compatible-postgresql-that-tells-you-where-compatibility-ends-o6a

## Related notes
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
