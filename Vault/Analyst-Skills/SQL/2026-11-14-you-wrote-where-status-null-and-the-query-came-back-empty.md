---
title: You wrote WHERE status = NULL, and the query came back empty
date: '2026-11-14'
source: https://dev.to/talentopsystems/you-wrote-where-status-null-and-the-query-came-back-empty-2bj9
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-15-sql-subqueries-vs-ctes-which-when-and-why]]'
- '[[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** Checked against official sources on November 13, 2026 You have a table of tickets. Some rows have no status yet. You want those rows. You write WHERE status = NULL . The query comes back empty. Nothing is broken. SQL did…

## What’s new and why it matters
Checked against official sources on November 13, 2026 You have a table of tickets. Some rows have no status yet. You want those rows. You write WHERE status = NULL . The query comes back empty. Nothing is broken. SQL did what it was told. NULL is not a value you can compare with = . Everything below was run in SQLite 3.46.1. The bug in a few lines CREATE TABLE tickets ( id INTEGER , status TEXT ) ; INSERT INTO tickets VALUES ( 1 , 'open' ) , ( 2 , 'closed' ) , ( 3 , NULL ) ; SELECT * FROM tickets WHERE status = NULL ; It returns no rows. Ticket 3 is right there, with no status, and the query s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/talentopsystems/you-wrote-where-status-null-and-the-query-came-back-empty-2bj9

## Related notes
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-15-sql-subqueries-vs-ctes-which-when-and-why]]
- [[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
