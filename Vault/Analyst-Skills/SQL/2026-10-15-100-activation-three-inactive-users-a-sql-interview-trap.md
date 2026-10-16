---
title: '100% activation, three inactive users: a SQL interview trap'
date: '2026-10-15'
source: https://dev.to/aleks_sqlbrief/100-activation-three-inactive-users-a-sql-interview-trap-5bgo
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** Suppose you're analysing a project-management app. People sign up to organise their work, but some leave without creating a project. You want to know how many new users take that first step within seven days of registeri…

## What’s new and why it matters
Suppose you're analysing a project-management app. People sign up to organise their work, but some leave without creating a project. You want to know how many new users take that first step within seven days of registering. In this example, creating at least one project during those seven days counts as activation . The activation rate is the percentage of registered users who do it. We'll compare people who signed up in two different weeks: Signup week beginning People who signed up People who created a project within seven days 3 August 2026 4 3 10 August 2026 6 4 Among the people who signed…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aleks_sqlbrief/100-activation-three-inactive-users-a-sql-interview-trap-5bgo

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
