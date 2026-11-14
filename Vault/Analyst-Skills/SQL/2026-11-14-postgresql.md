---
title: PostgreSQL
date: '2026-11-14'
source: https://dev.to/vasanthakumari_n/postgresql-c9n
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-09-14-ddl-and-dml-what-are-they]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-26-create-tables]]'
status: unread
---

> **TL;DR:** Auto Generate? In PostgreSQL, Auto Generate usually means automatically generating values for a column, such as an ID. You can use SERIAL or GENERATED AS IDENTITY. Example: Using SERIAL CREATE TABLE student ( id SERIAL P…

## What’s new and why it matters
Auto Generate? In PostgreSQL, Auto Generate usually means automatically generating values for a column, such as an ID. You can use SERIAL or GENERATED AS IDENTITY. Example: Using SERIAL CREATE TABLE student ( id SERIAL PRIMARY KEY , name VARCHAR ( 50 ) , age INT ) ; Two ways to auto-generate IDs SERIAL --> id SERIAL Identity --> id INT GENERATED ALWAYS AS IDENTITY Primary Keys A primary key constraint indicates that a column, or group of columns, can be used as a unique identifier for rows in the table. This requires that the values be both unique and not null. So, the following two table defi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vasanthakumari_n/postgresql-c9n

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-09-14-ddl-and-dml-what-are-they]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-sql-joins]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-26-create-tables]]
