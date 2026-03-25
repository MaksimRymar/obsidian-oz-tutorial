---
title: Select Queries from DVD Rental database Pt-1
date: '2026-03-24'
source: https://dev.to/s_a_r_a/select-queries-from-dvd-rental-database-kkh
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-2]]'
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-10-sql-joins-and-window-functions]]'
- '[[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
status: unread
---

> **TL;DR:** first, Download the tar file https://github.com/syedjaferk/postgres_sample_database/blob/main/dvd_rental/dvdrental.tar using the above link then open pgAdmin4 Login to your postgres then upload the downloaded database cr…

## What’s new and why it matters
first, Download the tar file https://github.com/syedjaferk/postgres_sample_database/blob/main/dvd_rental/dvdrental.tar using the above link then open pgAdmin4 Login to your postgres then upload the downloaded database create a new database called dvdrental using the cmd CREATE DATABASE dvdrental; -To check if your database has been uploaded use this cmd \dt SELECT Query Basic SELECT Statement SELECT first_name FROM customer; use the cmd to display all name in database 1) Use column aliases to rename title as "Movie Title" and rental_rate as "Rate" cmd: SELECT title AS "Movie Title", rental_rat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_a_r_a/select-queries-from-dvd-rental-database-kkh

## Related notes
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-2]]
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-10-sql-joins-and-window-functions]]
- [[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
