---
title: 'SQL Window Functions, Joins, CTEs and Subqueries: A Hospital Data Guide'
date: '2026-10-19'
source: https://dev.to/kbonymark/sql-window-functions-joins-ctes-and-subqueries-a-hospital-data-guide-27l5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
status: unread
---

> **TL;DR:** Window functions, joins, CTEs and subqueries are the four tools that turn raw hospital tables into answers: who is busiest, who was missed, what each department earns, how patients return. This article explains each one,…

## What’s new and why it matters
Window functions, joins, CTEs and subqueries are the four tools that turn raw hospital tables into answers: who is busiest, who was missed, what each department earns, how patients return. This article explains each one, shows why it exists and runs it on one small hospital database. Every query was run in PostgreSQL and the results shown are the real output. Introduction and the hospital dataset The dataset has five tables. Doctors belong to departments, and a doctor can report to another doctor. Patients book appointments with doctors and are sometimes admitted to a department. Table What a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kbonymark/sql-window-functions-joins-ctes-and-subqueries-a-hospital-data-guide-27l5

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-17-joins-in-sql]]
- [[2026-09-09-sql-joins]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
