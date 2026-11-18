---
title: Query a CSV file with SQL without setting up a database
date: '2026-11-18'
source: https://dev.to/aztechtools/query-a-csv-file-with-sql-without-setting-up-a-database-4db0
domain: Python
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-09-10-database-scaling-explained-by-breaking-things-indexing-replication-caching]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
status: unread
---

> **TL;DR:** A spreadsheet gets slow and awkward once a CSV has many thousands of rows and you want totals, filters or joins. SQL is made for those questions, and you do not need to install and configure a database server to use it.…

## What’s new and why it matters
A spreadsheet gets slow and awkward once a CSV has many thousands of rows and you want totals, filters or joins. SQL is made for those questions, and you do not need to install and configure a database server to use it. Here are three simple ways, using an example file called orders.csv with the columns order_id, customer, category, amount and order_date. Option 1: SQLite command line SQLite can import a CSV into a temporary database in a few commands. sqlite3 :memory: .mode csv .import orders.csv orders .headers on SELECT category, SUM ( amount ) AS total FROM orders GROUP BY category ORDER B…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aztechtools/query-a-csv-file-with-sql-without-setting-up-a-database-4db0

## Related notes
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-09-10-database-scaling-explained-by-breaking-things-indexing-replication-caching]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
