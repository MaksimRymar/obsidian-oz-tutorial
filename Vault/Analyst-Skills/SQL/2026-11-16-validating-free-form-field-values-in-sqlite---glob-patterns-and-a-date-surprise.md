---
title: Validating free-form field values in SQLite - GLOB patterns and a date() surprise
date: '2026-11-16'
source: https://dev.to/f345345dfg/validating-free-form-field-values-in-sqlite-glob-patterns-and-a-date-surprise-jng
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-16-customer-hierarchies-with-with-recursive---finding-cycles-and-group-totals-in-a-uniface-service]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
status: unread
---

> **TL;DR:** A customer app built in Uniface 10 has custom fields: an administrator defines a key, a label and a type ( NUMBER , DATE , BOOL , TEXT ), users enter values. The values are stored as text in one table. The input form val…

## What’s new and why it matters
A customer app built in Uniface 10 has custom fields: an administrator defines a key, a label and a type ( NUMBER , DATE , BOOL , TEXT ), users enter values. The values are stored as text in one table. The input form validates them, but data also arrives through imports and older versions. A check module lists values that do not match their type. Tested with Rocket Uniface 10.4.03 Community Edition (10.4.03.021) on Windows, November 2026. The app uses SQLite through the SLE driver (SQLite 3.50.2). The rules NUMBER : at least one digit, only digits, comma, dot and minus, and the minus only at t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/f345345dfg/validating-free-form-field-values-in-sqlite-glob-patterns-and-a-date-surprise-jng

## Related notes
- [[2026-11-16-customer-hierarchies-with-with-recursive---finding-cycles-and-group-totals-in-a-uniface-service]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
