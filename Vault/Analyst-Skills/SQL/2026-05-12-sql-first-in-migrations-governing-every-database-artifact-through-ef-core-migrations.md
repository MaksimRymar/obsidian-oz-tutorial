---
title: 'SQL-First-in-Migrations: Governing Every Database Artifact Through EF Core
  Migrations'
date: '2026-05-12'
source: https://dev.to/imzihad21/sql-first-in-migrations-governing-every-database-artifact-through-ef-core-migrations-i7p
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
status: unread
---

> **TL;DR:** SQL-First-in-Migrations: Governing Every Database Artifact Through EF Core Migrations 1. Introduction Entity Framework Core's code-first approach is frequently understood as limited to entity classes and their table mapp…

## What’s new and why it matters
SQL-First-in-Migrations: Governing Every Database Artifact Through EF Core Migrations 1. Introduction Entity Framework Core's code-first approach is frequently understood as limited to entity classes and their table mappings. A production database contains more than tables: views, functions, stored procedures, triggers, indexes that EF Core does not natively model, and baseline operational data. If these artifacts are created or managed outside the migration stream, the project loses the single source of truth that code-first promises. The solution is to treat any SQL object on which the syste…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/imzihad21/sql-first-in-migrations-governing-every-database-artifact-through-ef-core-migrations-i7p

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-10-joins-window-functions]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
