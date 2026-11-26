---
title: Your incremental load is quietly losing rows, and the IDENTITY column is why
date: '2026-11-26'
source: https://dev.to/isaactony/your-incremental-load-is-quietly-losing-rows-and-the-identity-column-is-why-4a97
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-11-17-ora-00054-resource-busy-find-the-session-and-know-which-ddl-will-wait]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
status: unread
---

> **TL;DR:** Most incremental loads I've seen are built on one line. WHERE Id > @LastLoadedId It's fast, it's easy to explain, and it passes every test you're likely to write. On a busy database it also drops rows now and then, with…

## What’s new and why it matters
Most incremental loads I've seen are built on one line. WHERE Id > @LastLoadedId It's fast, it's easy to explain, and it passes every test you're likely to write. On a busy database it also drops rows now and then, with no error and no warning. The fact table just ends up slightly short, and nobody notices until finance asks why the warehouse and the ledger disagree by 500.00. I wanted to see this happen rather than take it on faith, so I reproduced it on a double-entry ledger I've been building in SQL Server for a savings and credit co-op. This post walks through the reproduction, explains wh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isaactony/your-incremental-load-is-quietly-losing-rows-and-the-identity-column-is-why-4a97

## Related notes
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-11-17-ora-00054-resource-busy-find-the-session-and-know-which-ddl-will-wait]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
