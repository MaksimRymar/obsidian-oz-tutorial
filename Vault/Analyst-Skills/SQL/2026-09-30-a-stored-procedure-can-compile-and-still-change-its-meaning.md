---
title: A stored procedure can compile and still change its meaning
date: '2026-09-30'
source: https://dev.to/nidasahar/a-stored-procedure-can-compile-and-still-change-its-meaning-5ecf
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-07-09-how-do-i-answer-what-did-my-data-look-like-last-month-in-postgres]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
status: unread
---

> **TL;DR:** The syntax errors are the visible part of moving a stored procedure between databases. The quieter problem is a query that compiles in both places but answers a different question. Take a procedure that looks up a case a…

## What’s new and why it matters
The syntax errors are the visible part of moving a stored procedure between databases. The quieter problem is a query that compiles in both places but answers a different question. Take a procedure that looks up a case and returns a flag. The normal test has one matching row. It passes. That doesn't tell us what happens when the query finds nothing, or when the data contains two matches. In PL/pgSQL, SELECT ... INTO without STRICT assigns the first returned row to the target. With no rows, the target is set to nulls. FOUND lets the procedure check whether a row was assigned. If several rows ma…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nidasahar/a-stored-procedure-can-compile-and-still-change-its-meaning-5ecf

## Related notes
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-07-09-how-do-i-answer-what-did-my-data-look-like-last-month-in-postgres]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
