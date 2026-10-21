---
title: 'Window Functions, Joins, CTEs and Subqueries in SQL: A Hospital Dataset Walkthrough.'
date: '2026-10-21'
source: https://dev.to/brian_mugo/window-functions-joins-ctes-and-subqueries-in-sql-a-hospital-dataset-walkthrough-4bnb
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]'
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-10-19-sql-window-functions-joins-ctes-and-subqueries-explained-with-a-hospital-dataset]]'
- '[[2026-10-19-joins-window-functions-ctes-and-subqueries]]'
- '[[2026-10-18-a-practical-guide-to-sql-joins-subqueries-ctes-and-window-functions]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
status: unread
---

> **TL;DR:** Every hospital runs on data: patients, bills, wards, diagnoses and doctors. Answering real questions from that data, like "Which doctor brings the most revenue?" or "Which patients came back for a second visit?", takes m…

## What’s new and why it matters
Every hospital runs on data: patients, bills, wards, diagnoses and doctors. Answering real questions from that data, like "Which doctor brings the most revenue?" or "Which patients came back for a second visit?", takes more than just the basic SELECT . In this article I use a small hospital database to explain four SQL topics Window Functions Joins Common Table Expressions (CTEs) Subqueries The Dataset The database lives in Postgres and has the following core tables: doctors (doctor_id, doctor_name, doctor_gender, doctor_specialty, doctor_experience_years, email, city) patients (patient_id, pa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/brian_mugo/window-functions-joins-ctes-and-subqueries-in-sql-a-hospital-dataset-walkthrough-4bnb

## Related notes
- [[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]
- [[2026-10-17-joins-in-sql]]
- [[2026-10-19-sql-window-functions-joins-ctes-and-subqueries-explained-with-a-hospital-dataset]]
- [[2026-10-19-joins-window-functions-ctes-and-subqueries]]
- [[2026-10-18-a-practical-guide-to-sql-joins-subqueries-ctes-and-window-functions]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
