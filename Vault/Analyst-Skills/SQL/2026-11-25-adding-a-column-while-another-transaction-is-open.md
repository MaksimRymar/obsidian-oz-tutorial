---
title: Adding a column while another transaction is open
date: '2026-11-25'
source: https://dev.to/remdore/adding-a-column-while-another-transaction-is-open-42po
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-25-pgcancelbackend-returned-true-the-queue-didnt-move]]'
status: unread
---

> **TL;DR:** Adding a nullable column is one of the cheapest schema changes there is. In Postgres 18 it only touches the catalog, and in MySQL 8.4 you can ask for ALGORITHM=INSTANT . On an idle table both took a few milliseconds in m…

## What’s new and why it matters
Adding a nullable column is one of the cheapest schema changes there is. In Postgres 18 it only touches the catalog, and in MySQL 8.4 you can ask for ALGORITHM=INSTANT . On an idle table both took a few milliseconds in my tests. What I wanted to know is what happens to everyone else when the table isn't idle, specifically when some other session has an open transaction that read from it and hasn't committed yet. The setup Postgres 18.6 and MySQL 8.4.13 in two throwaway Docker containers on a Mac laptop. Each had one table, items , with 200,000 rows. Three clients ran for 32 seconds: a writer d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/remdore/adding-a-column-while-another-transaction-is-open-42po

## Related notes
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-25-pgcancelbackend-returned-true-the-queue-didnt-move]]
