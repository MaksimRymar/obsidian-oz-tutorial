---
title: Formatting SQL Statements (Part 1) — Identifiers, Delimiters, Commas, Aliases
date: '2026-08-27'
source: https://dev.to/marcus1968/formatting-sql-statements-part-1-identifiers-delimiters-commas-aliases-4mi0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-07-24-long-running-sql-queries-a-sample-exploration]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
status: unread
---

> **TL;DR:** Anyone who has ever had to debug a badly or completely unformatted SELECT with 30 columns and half a dozen joins knows the feeling: it isn't the SQL that eats up your day — it's hunting down what the statement is actuall…

## What’s new and why it matters
Anyone who has ever had to debug a badly or completely unformatted SELECT with 30 columns and half a dozen joins knows the feeling: it isn't the SQL that eats up your day — it's hunting down what the statement is actually trying to do. SQL formatting isn't a matter of taste; it's a maintenance tool — and it starts with a naming convention. → Part of a series. This is part 1 and covers identifiers, delimiters, commas, and aliases. For the layout of longer statements, continue with Part 2 — Structure and Formatting . What this article covers: Identifiers and delimiters — when to use square brack…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marcus1968/formatting-sql-statements-part-1-identifiers-delimiters-commas-aliases-4mi0

## Related notes
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-07-24-long-running-sql-queries-a-sample-exploration]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
