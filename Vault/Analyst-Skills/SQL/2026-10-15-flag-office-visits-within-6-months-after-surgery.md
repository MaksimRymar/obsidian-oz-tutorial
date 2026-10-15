---
title: Flag Office Visits Within 6 Months After Surgery
date: '2026-10-15'
source: https://dev.to/esproc_spl/flag-office-visits-within-6-months-after-surgery-hgg
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-04-16-sql-joins-explained]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
status: unread
---

> **TL;DR:** Problem Description The table tb_healthy records the medical history of patients; each patient has several records, where Visit_code = Surgery means an operation and Visit_code = Office means a consultation. Some patient…

## What’s new and why it matters
Problem Description The table tb_healthy records the medical history of patients; each patient has several records, where Visit_code = Surgery means an operation and Visit_code = Office means a consultation. Some patients have only operations, some have only consultations. Two questions have to be answered: whether the patient ever had a consultation, and whether the patient had a consultation within 6 months after an operation. The first goes into Office_Visit and the second into SX_past_6mo, with 1 for yes and 0 for no. Source Data tb_healthy table: Expected Result Office_Visit means the pat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/flag-office-visits-within-6-months-after-surgery-hgg

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-04-16-sql-joins-explained]]
- [[2026-09-09-sql-joins]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
