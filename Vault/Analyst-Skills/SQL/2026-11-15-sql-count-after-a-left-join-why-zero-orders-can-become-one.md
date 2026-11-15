---
title: 'SQL COUNT After a LEFT JOIN: Why Zero Orders Can Become One'
date: '2026-11-15'
source: https://dev.to/saravanan_techx/sql-count-after-a-left-join-why-zero-orders-can-become-one-2pg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-03-how-to-run-generative-ai-on-sql-tables-with-snowflake-cortex]]'
- '[[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
status: unread
---

> **TL;DR:** A customer with no orders can accidentally receive an order count of one. The SQL runs successfully; the error is in what is being counted. A minimal PostgreSQL example WITH customers ( customer_id ) AS ( VALUES ( 1 ) ,…

## What’s new and why it matters
A customer with no orders can accidentally receive an order count of one. The SQL runs successfully; the error is in what is being counted. A minimal PostgreSQL example WITH customers ( customer_id ) AS ( VALUES ( 1 ) , ( 2 ) ) , orders ( order_id , customer_id , status ) AS ( VALUES ( 101 , 1 , 'paid' ) , ( 102 , 1 , 'pending' ) ) SELECT c . customer_id , COUNT (*) AS joined_rows, COUNT(o.order_id) AS order_count, COUNT(o.order_id) FILTER (WHERE o.status = 'paid') AS paid_order_count FROM customers AS c LEFT JOIN orders AS o ON o.customer_id = c.customer_id GROUP BY c.customer_id ORDER BY c.c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saravanan_techx/sql-count-after-a-left-join-why-zero-orders-can-become-one-2pg

## Related notes
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-03-how-to-run-generative-ai-on-sql-tables-with-snowflake-cortex]]
- [[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
