---
title: I gave my text-to-SQL agent a business glossary. One version helped a lot,
  one did nothing.
date: '2026-10-05'
source: https://dev.to/ashish_sinha_5241c7673d93/i-gave-my-text-to-sql-agent-a-business-glossary-one-version-helped-a-lot-one-did-nothing-2c9o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]'
status: unread
---

> **TL;DR:** A text-to-SQL agent sees table and column names. It does not know that "revenue" in your company means billing_invoice.total_net , only for invoices with status = 'issued' . So it guesses, and the guess runs without erro…

## What’s new and why it matters
A text-to-SQL agent sees table and column names. It does not know that "revenue" in your company means billing_invoice.total_net , only for invoices with status = 'issued' . So it guesses, and the guess runs without errors and returns the wrong number. I added business terms to schemagate 1.2.0 (open source, Apache-2.0) and measured whether they help. Short answer: a complete glossary helps a lot. A glossary learned from other people's questions did not help at all. Here are both results. What a term looks like cat . concept ( " revenue " , synonyms = [ " turnover " , " sales " ], maps = [ " b…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/i-gave-my-text-to-sql-agent-a-business-glossary-one-version-helped-a-lot-one-did-nothing-2c9o

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]
