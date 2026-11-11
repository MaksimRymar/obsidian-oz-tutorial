---
title: I built GenerateRealData, a test data generator where keys, totals and rules
  hold across tables
date: '2026-11-11'
source: https://dev.to/generaterealdata/i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables-4g7e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** GenerateRealData makes test data for whole databases, not single tables. You give it your schema, and it gives back related tables where every foreign key points at a real row, totals add up across tables, dates come in…

## What’s new and why it matters
GenerateRealData makes test data for whole databases, not single tables. You give it your schema, and it gives back related tables where every foreign key points at a real row, totals add up across tables, dates come in order and your business rules hold on every row. Up to 500,000 rows in one run, as SQL, CSV, Excel or JSON. I built it because every other way I tried broke the moment the data spanned more than a couple of tables. Here's what it does, how it works, and where it still falls short. What it does, on a real schema Take an ordinary shop: CREATE TABLE customers ( id INT PRIMARY KEY…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/generaterealdata/i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables-4g7e

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
