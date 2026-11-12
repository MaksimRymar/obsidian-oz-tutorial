---
title: 4 SQL NULL Traps That Silently Break Your Queries (NOT IN Returns 0 Rows!)
date: '2026-11-12'
source: https://dev.to/refactorly/4-sql-null-traps-that-silently-break-your-queries-not-in-returns-0-rows-32oo
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-07-12-sql-null-semantics-three-valued-logic-the-traps-that-break-every-report]]'
- '[[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]'
- '[[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]'
- '[[2026-04-21-two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing]]'
status: unread
---

> **TL;DR:** This query should return three users. It returns zero . No error, no warning: SELECT * FROM users WHERE id NOT IN ( SELECT user_id FROM banned ) ; -- 0 rows The cause is a single NULL . Here are four NULL traps, each wit…

## What’s new and why it matters
This query should return three users. It returns zero . No error, no warning: SELECT * FROM users WHERE id NOT IN ( SELECT user_id FROM banned ) ; -- 0 rows The cause is a single NULL . Here are four NULL traps, each with a fix. I ran every query below in PostgreSQL 17 and SQLite 3.51 , and both gave the same results. Video version: The setup CREATE TABLE users ( id int , name text , country text ) ; INSERT INTO users VALUES ( 1 , 'Ann' , 'US' ) , ( 2 , 'Bob' , 'UK' ) , ( 3 , 'Cat' , NULL ) , -- 👈 this row ( 4 , 'Dan' , 'US' ) ; CREATE TABLE banned ( user_id int ) ; INSERT INTO banned VALUES (…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/4-sql-null-traps-that-silently-break-your-queries-not-in-returns-0-rows-32oo

## Related notes
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-07-12-sql-null-semantics-three-valued-logic-the-traps-that-break-every-report]]
- [[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]
- [[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]
- [[2026-04-21-two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing]]
