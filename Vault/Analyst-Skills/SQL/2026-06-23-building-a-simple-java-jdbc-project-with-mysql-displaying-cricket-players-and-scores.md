---
title: 'Building a Simple Java JDBC Project with MySQL: Displaying Cricket Players
  and Scores'
date: '2026-06-23'
source: https://dev.to/jayashree_a84b6eff7bc414e/building-a-simple-java-jdbc-project-with-mysql-displaying-cricket-players-and-scores-5gf6
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
- '[[2026-04-12-understanding-sql-basics-ddl-dml-filtering-and-data-transformation]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-04-13-introduction-to-databases-with-sql]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
status: unread
---

> **TL;DR:** While learning Java, I wanted to understand how Java connects with a database and retrieves data . Instead of using a random example, I created a small cricket project. The idea was simple: store Indian and Afghanistan p…

## What’s new and why it matters
While learning Java, I wanted to understand how Java connects with a database and retrieves data . Instead of using a random example, I created a small cricket project. The idea was simple: store Indian and Afghanistan players' scores in MySQL and display them through Java . Step 1: Creating the Database First, I created a database named cricket. CREATE DATABASE cricket ; USE cricket ; Then, I created two tables: CREATE TABLE india ( player_name VARCHAR ( 50 ), score INT ); CREATE TABLE afghanistan ( player_name VARCHAR ( 50 ), score INT ); After that, I inserted player data into both tables.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jayashree_a84b6eff7bc414e/building-a-simple-java-jdbc-project-with-mysql-displaying-cricket-players-and-scores-5gf6

## Related notes
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
- [[2026-04-12-understanding-sql-basics-ddl-dml-filtering-and-data-transformation]]
- [[2026-03-01-sql-joins]]
- [[2026-04-13-introduction-to-databases-with-sql]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
