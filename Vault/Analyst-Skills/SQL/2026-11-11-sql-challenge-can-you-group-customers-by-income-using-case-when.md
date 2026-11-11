---
title: 'SQL Challenge: Can You Group Customers by Income Using CASE WHEN?'
date: '2026-11-11'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-can-you-group-customers-by-income-using-case-when-4cei
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]'
- '[[2026-11-08-can-you-find-employees-who-joined-this-month-using-sql-oracle-trunc-addmonths]]'
- '[[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-22-customer-segmentation-in-sql-with-case-when]]'
- '[[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]'
status: unread
---

> **TL;DR:** Here is a practical problem you might face while preparing a customer analysis report. You have a customers table containing customer IDs, names and annual income. The business team wants to understand how many customers…

## What’s new and why it matters
Here is a practical problem you might face while preparing a customer analysis report. You have a customers table containing customer IDs, names and annual income. The business team wants to understand how many customers fall into each income category. The categories are: Low Income: Below ₹3,00,000 Middle Income: ₹3,00,000 to ₹7,00,000 High Income: Above ₹7,00,000 How would you create this report using SQL? customers customer_id | name | annual_income 101 | Rahul | 250000 102 | Priya | 450000 103 | Amit | 850000 104 | Sneha | 300000 105 | Karan | 650000 106 | Neha | 950000 107 | Rohan | 20000…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-can-you-group-customers-by-income-using-case-when-4cei

## Related notes
- [[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]
- [[2026-11-08-can-you-find-employees-who-joined-this-month-using-sql-oracle-trunc-addmonths]]
- [[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-22-customer-segmentation-in-sql-with-case-when]]
- [[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]
