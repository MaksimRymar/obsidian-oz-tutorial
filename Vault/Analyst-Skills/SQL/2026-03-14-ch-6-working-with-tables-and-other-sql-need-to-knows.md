---
title: 'Ch 6: Working With Tables and Other SQL Need-To-Knows'
date: '2026-03-14'
source: https://dev.to/essym_19/ch-6-working-with-tables-and-other-sql-need-to-knows-jep
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
- '[[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-02-sql-joins-and-window-functions--what-i-learned-catching-up-after-missing-class]]'
- '[[2026-03-06-joins-and-window-functions-in-sql]]'
- '[[2026-03-11-sql-joins-window-functions]]'
status: unread
---

> **TL;DR:** Creating SQL tables When creating tables, you need to define the columns and their data types. CREATE TABLE table_name ( column1 datatype , column2 datatype , column3 datatype , ) We are going to call our table customer_…

## What’s new and why it matters
Creating SQL tables When creating tables, you need to define the columns and their data types. CREATE TABLE table_name ( column1 datatype , column2 datatype , column3 datatype , ) We are going to call our table customer_data, and it will have the columns customer_id, customer_name, and dob. CREATE TABLE customer_data ( customer_id INT PRIMARY KEY , customer_name VARCHAR ( 50 ), dob datatype DATETIME ); Inserting data into the table This is the syntax for inserting multiple rows into a table: INSERT INTO table_name ( column1 , column2 , column3 ) VALUES ( value1 , value2 , value3 ), ( value1 ,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/essym_19/ch-6-working-with-tables-and-other-sql-need-to-knows-jep

## Related notes
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
- [[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-02-sql-joins-and-window-functions--what-i-learned-catching-up-after-missing-class]]
- [[2026-03-06-joins-and-window-functions-in-sql]]
- [[2026-03-11-sql-joins-window-functions]]
