---
title: How to change a primary key that foreign keys already point at
date: '2026-10-13'
source: https://dev.to/woodfiresam/how-to-change-a-primary-key-that-foreign-keys-already-point-at-4p8i
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** You try to move a table's primary key onto a different column and get: Msg 3725, Level 16, State 1 The constraint 'PK_Customer' is being referenced by table 'Order', foreign key constraint 'FK_Order_Customer'. Msg 3727,…

## What’s new and why it matters
You try to move a table's primary key onto a different column and get: Msg 3725, Level 16, State 1 The constraint 'PK_Customer' is being referenced by table 'Order', foreign key constraint 'FK_Order_Customer'. Msg 3727, Level 16, State 1 Could not drop constraint. See previous errors. A foreign key is a promise that every value in the child column exists exactly once in the parent, and the primary key is what makes that true. Drop the key and the promise has nothing holding it up, so SQL Server refuses while any foreign key still points at it. The message names one constraint. If three tables…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/woodfiresam/how-to-change-a-primary-key-that-foreign-keys-already-point-at-4p8i

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
