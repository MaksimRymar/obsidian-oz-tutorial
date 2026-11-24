---
title: Analyzing doctors data using SQL
date: '2026-11-24'
source: https://dev.to/denoh/analyzing-doctors-data-using-sql-2jnk
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-21-writing-sql-basic-queries]]'
- '[[2026-10-25-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-other-operators]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-10-16-sql-for-data-analysis-window-functions-joins-ctes-and-subqueries]]'
- '[[2026-10-20-mastering-sql-window-functions-joins-common-table-expressions-ctes-and-subqueries-using-a-hospital-database]]'
- '[[2026-07-22-i-completed-hackerrank-sql-basic-select-heres-what-i-learned]]'
status: unread
---

> **TL;DR:** Today, I focused on analyzing hospital records from a doctor's perspective. Instead of writing queries just to retrieve rows, I started asking meaningful questions that someone in hospital management might actually ask.…

## What’s new and why it matters
Today, I focused on analyzing hospital records from a doctor's perspective. Instead of writing queries just to retrieve rows, I started asking meaningful questions that someone in hospital management might actually ask. I explored questions such as: How many doctors are available in the hospital? select pr.doctor_name from patient_records pr group by doctor_name order by doctor_name asc; How many patients has each doctor treated? select pr.doctor_name, count(*) as n_patients from patient_records pr group by doctor_name order by doctor_name asc; Which patients were treated by a specific doctor?…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/denoh/analyzing-doctors-data-using-sql-2jnk

## Related notes
- [[2026-11-21-writing-sql-basic-queries]]
- [[2026-10-25-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-other-operators]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-10-16-sql-for-data-analysis-window-functions-joins-ctes-and-subqueries]]
- [[2026-10-20-mastering-sql-window-functions-joins-common-table-expressions-ctes-and-subqueries-using-a-hospital-database]]
- [[2026-07-22-i-completed-hackerrank-sql-basic-select-heres-what-i-learned]]
