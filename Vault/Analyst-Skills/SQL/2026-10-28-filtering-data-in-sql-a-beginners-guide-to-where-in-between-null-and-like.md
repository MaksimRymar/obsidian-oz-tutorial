---
title: 'Filtering Data in SQL: A Beginner''s Guide to WHERE, IN, BETWEEN, NULL, and
  LIKE'
date: '2026-10-28'
source: https://dev.to/elizabeth_kimani_bca65d6e/filtering-data-in-sql-a-beginners-guide-to-where-in-between-null-and-like-3iod
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-10-25-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-other-operators]]'
status: unread
---

> **TL;DR:** Hi everyone! I am learning SQL, and this week we studied operators. Operators are the words and symbols we write after WHERE to tell SQL which rows we want. I practised on a practice hospital table called patients in Pos…

## What’s new and why it matters
Hi everyone! I am learning SQL, and this week we studied operators. Operators are the words and symbols we write after WHERE to tell SQL which rows we want. I practised on a practice hospital table called patients in PostgreSQL. It has columns like county , department , age , bill_amount , insurance and `email. In this post, I explain what I learned, using queries I wrote myself. 1. Comparison operators Comparison operators compare a column with a value. They are = , != (or <> ), > , < , >= and <= . sql SELECT first_name, last_name, department, bill_amount FROM patients WHERE bill_amount > 100…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/elizabeth_kimani_bca65d6e/filtering-data-in-sql-a-beginners-guide-to-where-in-between-null-and-like-3iod

## Related notes
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-10-25-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-other-operators]]
