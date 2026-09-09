---
title: 'SQL Joins in PostgreSQL: Patients, Doctors, and the Rows That Go Missing'
date: '2026-09-09'
source: https://dev.to/leahkivuti/sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing-67n
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-09-sql-joins]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-04-16-sql-joins-explained]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** A join is how you ask one question across two tables. The database keeps patients in one table and appointments in another, because storing the patient's name on every appointment row would mean fixing it in ten places w…

## What’s new and why it matters
A join is how you ask one question across two tables. The database keeps patients in one table and appointments in another, because storing the patient's name on every appointment row would mean fixing it in ten places when it's misspelled. A join puts them back together for the length of one query. That's the whole idea. The part that takes practice is that there are several kinds of joins, and they disagree about what to do with rows that have no partner on the other side. Pick the wrong one and rows quietly disappear from your result, and nothing warns you. This article uses a small hospita…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/leahkivuti/sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing-67n

## Related notes
- [[2026-09-09-sql-joins]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-04-16-sql-joins-explained]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
