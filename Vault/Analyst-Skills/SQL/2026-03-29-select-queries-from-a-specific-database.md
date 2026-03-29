---
title: SELECT QUERIES FROM A SPECIFIC DATABASE
date: '2026-03-29'
source: https://dev.to/christina_sharons_2b3205/select-queries-from-a-specific-database-37j
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-29-select-queries-from-dvd-rental-database]]'
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-2]]'
- '[[2026-03-29-filtering-a-db-using-sql-queries]]'
status: unread
---

> **TL;DR:** The SELECT statement is one of the most fundamental SQL commands and is used to retrieve data from a PostgreSQL database. Syntax: SELECT column_name FROM table_name ; I was given a few tasks to strengthen my sql basics s…

## What’s new and why it matters
The SELECT statement is one of the most fundamental SQL commands and is used to retrieve data from a PostgreSQL database. Syntax: SELECT column_name FROM table_name ; I was given a few tasks to strengthen my sql basics so this blog will contain the queries that i performed after connecting my dvdrental database to PostgreSQL. 1.Retrieve film titles and their rental rates. Use column aliases to rename title as "Movie Title" and rental_rate as "Rate". SELECT title AS "Movie_title" , rental_rate AS "Rate" FROM film ; 2.List customer names and their email addresses. Alias first_name and last_name…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/christina_sharons_2b3205/select-queries-from-a-specific-database-37j

## Related notes
- [[2026-03-29-select-queries-from-dvd-rental-database]]
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-2]]
- [[2026-03-29-filtering-a-db-using-sql-queries]]
