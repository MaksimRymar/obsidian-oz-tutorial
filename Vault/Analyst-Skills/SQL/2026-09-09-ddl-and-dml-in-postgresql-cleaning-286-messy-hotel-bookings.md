---
title: 'DDL and DML in PostgreSQL: Cleaning 286 Messy Hotel Bookings.'
date: '2026-09-09'
source: https://dev.to/leahkivuti/ddl-and-dml-in-postgresql-cleaning-286-messy-hotel-bookings-3l26
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** SQL commands come in two groups. DDL (Data Definition Language) builds and changes the structure : schemas, tables, columns, types, views. DML (Data Manipulation Language) works on the rows : insert, update, delete, sele…

## What’s new and why it matters
SQL commands come in two groups. DDL (Data Definition Language) builds and changes the structure : schemas, tables, columns, types, views. DML (Data Manipulation Language) works on the rows : insert, update, delete, select. That's the definition. It didn't mean much to me until I had to clean a real file. So this article uses that file: a hotel's booking export, 286 rows, 20 columns, and dirty in almost every one of them. Names in capitals, phone numbers with +254 and dashes, mpesa next to M-Pesa , guest ratings of 0 and 6, one duplicate booking, and dates in four different formats. I'll show…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/leahkivuti/ddl-and-dml-in-postgresql-cleaning-286-messy-hotel-bookings-3l26

## Related notes
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
