---
title: Where Should the Foreign Key Go?
date: '2026-07-23'
source: https://dev.to/hugodcarmo/where-should-the-foreign-key-go-20id
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]'
- '[[2026-03-11-sql-joins-window-functions]]'
status: unread
---

> **TL;DR:** This is Part II of a series about vertical partitioning for large text columns. Part I explains why we separated the large text from the main table. In Part I , we split one books table into two tables: CREATE TABLE book…

## What’s new and why it matters
This is Part II of a series about vertical partitioning for large text columns. Part I explains why we separated the large text from the main table. In Part I , we split one books table into two tables: CREATE TABLE books ( id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY , title VARCHAR ( 255 ) NOT NULL , author VARCHAR ( 255 ) NOT NULL , isbn VARCHAR ( 20 ) NOT NULL , published_year SMALLINT UNSIGNED NOT NULL ); CREATE TABLE book_contents ( book_id BIGINT UNSIGNED PRIMARY KEY , resume TEXT NOT NULL , FOREIGN KEY ( book_id ) REFERENCES books ( id ) ON DELETE CASCADE ); The foreign key is in book…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hugodcarmo/where-should-the-foreign-key-go-20id

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-26-create-tables]]
- [[2026-03-26-alter-table]]
- [[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]
- [[2026-03-11-sql-joins-window-functions]]
