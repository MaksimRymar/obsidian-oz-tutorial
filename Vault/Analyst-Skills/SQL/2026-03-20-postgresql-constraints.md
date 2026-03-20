---
title: PostgreSQL-constraints
date: '2026-03-20'
source: https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresql-constraints-2bng
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-02-27-joins-and-window-functions-in-sql]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-02-sql-joins-explained-case-example]]'
status: unread
---

> **TL;DR:** Constraints: Constraints are the backbone of reliable database design. They act like safety checks, ensuring that every piece of data stored is valid, consistent, and meaningful. Types of Constraints 1.PRIMARY KEY -Ensur…

## What’s new and why it matters
Constraints: Constraints are the backbone of reliable database design. They act like safety checks, ensuring that every piece of data stored is valid, consistent, and meaningful. Types of Constraints 1.PRIMARY KEY -Ensures each row has a unique identifier. -No duplicates, no NULL values. example: emp_id SERIAL PRIMARY KEY 2.FOREIGN KEY -Creates a relationship between two tables. -Ensures values in one table match values in another. example: dept_id INT REFERENCES Department(dept_id) 3.UNIQUE -Guarantees that all values in a column are distinct. example: email VARCHAR(150) UNIQUE 4. NOT NULL -P…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresql-constraints-2bng

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-02-27-joins-and-window-functions-in-sql]]
- [[2026-03-01-sql-joins]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-02-sql-joins-explained-case-example]]
