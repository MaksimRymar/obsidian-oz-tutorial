---
title: 'Factless Fact Tables: Modeling Events, Coverage & Eligibility Without Measures'
date: '2026-09-24'
source: https://dev.to/gowthampotureddi/factless-fact-tables-modeling-events-coverage-eligibility-without-measures-2h6h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-23-fact-table-patterns-transaction-periodic-snapshot-accumulating-snapshot-facts]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-09-sql-joins]]'
status: unread
---

> **TL;DR:** factless fact table is the one design pattern that breaks the rule every beginner learns first — that a fact table is where the numbers live. A factless fact table has no numbers. It is a fact table made almost entirely…

## What’s new and why it matters
factless fact table is the one design pattern that breaks the rule every beginner learns first — that a fact table is where the numbers live. A factless fact table has no numbers. It is a fact table made almost entirely of foreign keys pointing at dimensions, with not a single amount, quantity, or price column to sum. And yet it is one of the most useful shapes in a star schema, because the presence of the row is itself the fact. A row exists exactly when a student attended a class, when a product was on promotion, when a user viewed a page — and the metric you want is simply how many such row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/factless-fact-tables-modeling-events-coverage-eligibility-without-measures-2h6h

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-23-fact-table-patterns-transaction-periodic-snapshot-accumulating-snapshot-facts]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-09-sql-joins]]
