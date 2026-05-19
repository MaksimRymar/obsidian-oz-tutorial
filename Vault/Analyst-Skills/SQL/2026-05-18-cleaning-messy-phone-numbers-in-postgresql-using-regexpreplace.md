---
title: Cleaning Messy Phone Numbers in PostgreSQL Using REGEXP_REPLACE
date: '2026-05-18'
source: https://dev.to/sharonnyabuto/cleaning-messy-phone-numbers-in-postgresql-using-regexp-replace-3n83
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** Introduction The first thing anyone that has worked with real world data will tell you is that rarely does data come in the clean, uniform format you expect. Phone numbers are one of the biggest culprits. One person ente…

## What’s new and why it matters
Introduction The first thing anyone that has worked with real world data will tell you is that rarely does data come in the clean, uniform format you expect. Phone numbers are one of the biggest culprits. One person enters +254712345678 , another writes 0712345678 , someone else throws in 254-712-345-678 , another (254)-712345678 and another 254 712 345 678 . Before you know it, your database has a different version of phone numbers in every row. In this article, we will explore how to fix that, using a powerful PostgreSQL function called regexp_replace . By the end, you will understand what i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sharonnyabuto/cleaning-messy-phone-numbers-in-postgresql-using-regexp-replace-3n83

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-03-08-understanding-group-by-in-sql]]
