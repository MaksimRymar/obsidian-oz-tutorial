---
title: 'SQL Challenge: Can You Build a Customer Report Using JOIN, GROUP BY and CASE
  WHEN?'
date: '2026-11-12'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-can-you-build-a-customer-report-using-join-group-by-and-case-when-2pp4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-sql-challenge-can-you-group-customers-by-income-using-case-when]]'
- '[[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]'
- '[[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-11-08-can-you-find-employees-who-joined-this-month-using-sql-oracle-trunc-addmonths]]'
- '[[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]'
status: unread
---

> **TL;DR:** Here is a practical problem you might face as a data analyst. You have two tables: customers and orders. The business team wants a report showing each customer's order count, total spending, latest order date and custome…

## What’s new and why it matters
Here is a practical problem you might face as a data analyst. You have two tables: customers and orders. The business team wants a report showing each customer's order count, total spending, latest order date and customer category. Customer categories: High Value: ₹1,00,000 or above Medium Value: ₹50,000 to below ₹1,00,000 Low Value: Below ₹50,000 customers customer_id | customer_name 101 | Rahul 102 | Priya 103 | Amit 104 | Neha orders order_id | customer_id | order_date | amount 1 | 101 | 2026-01-10 | 40000 2 | 101 | 2026-02-15 | 35000 3 | 101 | 2026-03-20 | 30000 4 | 102 | 2026-01-18 | 2500…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-can-you-build-a-customer-report-using-join-group-by-and-case-when-2pp4

## Related notes
- [[2026-11-11-sql-challenge-can-you-group-customers-by-income-using-case-when]]
- [[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]
- [[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-11-08-can-you-find-employees-who-joined-this-month-using-sql-oracle-trunc-addmonths]]
- [[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]
