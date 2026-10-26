---
title: SQL for Beginners
date: '2026-10-26'
source: https://dev.to/mwaidesu/sql-for-beginners-2ii4
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-10-19-joins-window-functions-ctes-and-subqueries]]'
status: unread
---

> **TL;DR:** We'll walk through the operators you actually need as a beginner—comparison, logical, range and list, NULL handling, and pattern matching—all in PostgreSQL, with queries I actually ran against a patients table. Compariso…

## What’s new and why it matters
We'll walk through the operators you actually need as a beginner—comparison, logical, range and list, NULL handling, and pattern matching—all in PostgreSQL, with queries I actually ran against a patients table. Comparison Operators Comparison operators are the ones you'll use every single day. They return a boolean for every row, and WHERE keeps only the rows where the result is true . The core set is = , <> (or != ), < , > , <= , and >= . Here's a query for a patients table: SELECT patient_id , patient_name , bill_amount FROM patients WHERE bill_amount > 10000 ; Simple enough. The trouble sta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mwaidesu/sql-for-beginners-2ii4

## Related notes
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-10-19-joins-window-functions-ctes-and-subqueries]]
