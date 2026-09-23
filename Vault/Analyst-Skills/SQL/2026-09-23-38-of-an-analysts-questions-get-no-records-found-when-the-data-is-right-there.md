---
title: 38% of an analyst's questions get "no records found" when the data is right
  there
date: '2026-09-23'
source: https://dev.to/ashish_sinha_5241c7673d93/38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there-5edm
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-09-15-vanna-is-archived-the-failure-mode-none-of-the-replacements-fix]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Your text-to-SQL agent has a failure mode that logs nothing, alerts nothing, and returns a confidently wrong answer. I finally put a number on how often it can happen, and on a small schema with an ordinary role split th…

## What’s new and why it matters
Your text-to-SQL agent has a failure mode that logs nothing, alerts nothing, and returns a confidently wrong answer. I finally put a number on how often it can happen, and on a small schema with an ordinary role split the number is 38.5%. The failure Someone asks a question whose answer lives in a table they are not allowed to read. The model is handed the whole schema, because that is what nearly every text-to-SQL stack does. It writes a perfectly correct query against that table. The query executes. Row-level security removes every row. The application receives an empty result set and report…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there-5edm

## Related notes
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-09-15-vanna-is-archived-the-failure-mode-none-of-the-replacements-fix]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
