---
title: 'SQL Functions: Cleaning Text and Rounding Numbers the Right Way'
date: '2026-07-20'
source: https://dev.to/navas_herbert/sql-functions-cleaning-text-and-rounding-numbers-the-right-way-fij
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-05-06-sql-string-functions-clean-transform-and-tame-messy-data-like-a-pro]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-07-12-sql-week-we-deleted-products-dropped-tables-and-found-out-which-supplier-was-sitting-on-the-most-stock]]'
status: unread
---

> **TL;DR:** Data arrives messy. Names in ALL CAPS. Cities spelled differently in different rows. Exam marks with five decimal places nobody asked for. Teachers listed as "Mr. Njoroge" when the report needs "Prof. Njoroge". First and…

## What’s new and why it matters
Data arrives messy. Names in ALL CAPS. Cities spelled differently in different rows. Exam marks with five decimal places nobody asked for. Teachers listed as "Mr. Njoroge" when the report needs "Prof. Njoroge". First and last names in separate columns when the output needs a single full name. Every analyst has sat with a spreadsheet full of this kind of thing and spent hours fixing it manually. Today we taught the class how to fix it in SQL - once, in a query, automatically, for every row in the table. Two categories. String functions for text. Number functions for numeric values. One dataset:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/navas_herbert/sql-functions-cleaning-text-and-rounding-numbers-the-right-way-fij

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-05-06-sql-string-functions-clean-transform-and-tame-messy-data-like-a-pro]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-07-12-sql-week-we-deleted-products-dropped-tables-and-found-out-which-supplier-was-sitting-on-the-most-stock]]
