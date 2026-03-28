---
title: 🚀 Built a Cross-Database(AI) Recommendation System using FDW + Prisma
date: '2026-03-27'
source: https://dev.to/karanjamadar/built-a-cross-database-recommendation-system-using-fdw-prisma-1dh1
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-02-mastering-joins-and-window-functions-in-sql]]'
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
- '[[2026-03-06-joins-and-window-functions-in-sql]]'
- '[[2026-03-14-demystifying-sql-joins-window-functions]]'
- '[[2026-03-04-learning-how-to-use-windows-sql-functions-and-joins-in-relational-databases]]'
- '[[2026-03-02-understanding-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** Recently worked on an interesting backend problem — sharing the approach in case it helps others working with multi-DB systems 👇 🧩 Problem We had two separate databases: Core DB → transactional data (activities, particip…

## What’s new and why it matters
Recently worked on an interesting backend problem — sharing the approach in case it helps others working with multi-DB systems 👇 🧩 Problem We had two separate databases: Core DB → transactional data (activities, participants, items) Profile DB → user/entity master data + metadata We needed: 👉 A unified dataset for ranking/recommendation 👉 Without duplicating data across databases 💡 Solution: PostgreSQL FDW Used Foreign Data Wrapper (FDW) to query Profile DB directly from Core DB. CREATE EXTENSION postgres_fdw ; CREATE SERVER remote_profile_srv FOREIGN DATA WRAPPER postgres_fdw OPTIONS ( host '…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/karanjamadar/built-a-cross-database-recommendation-system-using-fdw-prisma-1dh1

## Related notes
- [[2026-03-02-mastering-joins-and-window-functions-in-sql]]
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
- [[2026-03-06-joins-and-window-functions-in-sql]]
- [[2026-03-14-demystifying-sql-joins-window-functions]]
- [[2026-03-04-learning-how-to-use-windows-sql-functions-and-joins-in-relational-databases]]
- [[2026-03-02-understanding-joins-and-window-functions-in-sql]]
