---
title: Select Queries from DVD Rental database Pt-3
date: '2026-03-24'
source: https://dev.to/s_a_r_a/select-queries-from-dvd-rental-database-pt-3-5852
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#sql'
related:
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-03-08-sql-queries-asked-in-interview]]'
- '[[2026-03-10-sql-joins-and-window-functions]]'
- '[[2026-03-07-a-beginners-guide-to-sql-joins-and-window-functions]]'
- '[[2026-03-20-sql-triggers-for-blocking]]'
status: unread
---

> **TL;DR:** 13) Retrieve the first unique customer ID based on active status. Include the customer_id and active columns, and order by customer_id. cmd: SELECT DISTINCT customer_id, active FROM customer ORDER BY customer_id; SAMPLE…

## What’s new and why it matters
13) Retrieve the first unique customer ID based on active status. Include the customer_id and active columns, and order by customer_id. cmd: SELECT DISTINCT customer_id, active FROM customer ORDER BY customer_id; SAMPLE OP: customer_id | active -------------+-------- 1 | 1 2 | 1 3 | 1 4 | 1 5 | 1 6 | 1 7 | 1 14) List the earliest rental date for each customer. Include customer_id and rental_date, and order by customer_id. cmd: SELECT customer_id, MIN(rental_date) AS rental_date FROM rental GROUP BY customer_id ORDER BY customer_id; SAMPLE OP: customer_id | rental_date -------------+-----------…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_a_r_a/select-queries-from-dvd-rental-database-pt-3-5852

## Related notes
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-03-08-sql-queries-asked-in-interview]]
- [[2026-03-10-sql-joins-and-window-functions]]
- [[2026-03-07-a-beginners-guide-to-sql-joins-and-window-functions]]
- [[2026-03-20-sql-triggers-for-blocking]]
