---
title: I Thought My Rails Query Was Fine — Until NULL Ate My Data
date: '2026-03-11'
source: https://dev.to/pavelmyslik/i-thought-my-rails-query-was-fine-until-null-ate-my-data-13ca
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-02-postgresql-vs-mongodb-in-2026-when-to-choose-sql-over-nosql]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
status: unread
---

> **TL;DR:** I ran into this while working on a task where I needed to process all contracts that were not coming from SAP. At first, the query looked perfectly fine: Contract . where . not ( source: 'sap' ) Then I double-checked the…

## What’s new and why it matters
I ran into this while working on a task where I needed to process all contracts that were not coming from SAP. At first, the query looked perfectly fine: Contract . where . not ( source: 'sap' ) Then I double-checked the result by counting returned objects — and something didn’t add up. You write a Rails query. It looks correct. It runs without errors. But it's quietly hiding records from you. Welcome to one of the most common — and maybe most dangerous — SQL gotchas. The Setup Imagine you have a contracts table with a source column — which is nullable . Some contracts have: source = 'sap' sou…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pavelmyslik/i-thought-my-rails-query-was-fine-until-null-ate-my-data-13ca

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-02-postgresql-vs-mongodb-in-2026-when-to-choose-sql-over-nosql]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
