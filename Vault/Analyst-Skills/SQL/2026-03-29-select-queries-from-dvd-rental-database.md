---
title: Select Queries from DVD Rental database
date: '2026-03-29'
source: https://dev.to/jeyaprasadr/select-queries-from-dvd-rental-database-3cni
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]'
- '[[2026-03-26-select-queries]]'
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-2]]'
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-1]]'
- '[[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
status: unread
---

> **TL;DR:** Film titles and rental rates (Aliased) SELECT title AS "Movie Title" , rental_rate AS "Rate" FROM film ; Customer names and emails (Aliased) SELECT first_name AS "First Name" , last_name AS "Last Name" , email FROM custo…

## What’s new and why it matters
Film titles and rental rates (Aliased) SELECT title AS "Movie Title" , rental_rate AS "Rate" FROM film ; Customer names and emails (Aliased) SELECT first_name AS "First Name" , last_name AS "Last Name" , email FROM customer ; Films sorted by rental rate (DESC) and title (ASC) SELECT * FROM film ORDER BY rental_rate DESC , title ASC ; Actor names sorted by last name, then first name SELECT first_name , last_name FROM actor ORDER BY last_name , first_name ; Unique replacement costs SELECT DISTINCT replacement_cost FROM film ; Film title and length (Aliased) SELECT title , length AS "Duration (mi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jeyaprasadr/select-queries-from-dvd-rental-database-3cni

## Related notes
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]
- [[2026-03-26-select-queries]]
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-2]]
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-1]]
- [[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
