---
title: SQL Cheatsheet
date: '2026-03-04'
source: https://dev.to/krutidb/sql-cheatsheet-4aii
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
- '[[2026-03-01-understanding-joins-and-window-functions-in-sql]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-02-21-sql-masterclass]]'
status: unread
---

> **TL;DR:** Here's a cheat sheet to quickly review all SQL queries before an interview. TABLE Queries CREATE TABLE table_name (column1 datatype, column2 datatype, ... ); DROP TABLE table_name; ALTER TABLE table_name ADD column_name…

## What’s new and why it matters
Here's a cheat sheet to quickly review all SQL queries before an interview. TABLE Queries CREATE TABLE table_name (column1 datatype, column2 datatype, ... ); DROP TABLE table_name; ALTER TABLE table_name ADD column_name datatype; INSERT INTO table_name (column1, column2) VALUES (value_or_expr1, value_or_expr2); SELECT Queries SELECT * FROM table_name; SELECT DISTINCT column_name1, column_name2 FROM table_name; SELECT column_name1 FROM table_name ORDER BY column_name2 ASC / DESC; /* (by default it is ascending if you don't write DESC) */ SELECT column_name1 FROM table_name WHERE column_name2 BE…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/krutidb/sql-cheatsheet-4aii

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
- [[2026-03-01-understanding-joins-and-window-functions-in-sql]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-02-21-sql-masterclass]]
