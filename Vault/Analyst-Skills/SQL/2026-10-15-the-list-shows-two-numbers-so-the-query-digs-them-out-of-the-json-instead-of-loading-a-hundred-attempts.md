---
title: The list shows two numbers, so the query digs them out of the JSON instead
  of loading a hundred attempts
date: '2026-10-15'
source: https://dev.to/daniel_pertu/the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-248j
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
status: unread
---

> **TL;DR:** We added a "Past attempts" list to the assessment centre dashboard. Each row is a title, a date, one number and a one-word caption. There is a /dashboard/exercises/report/<id> page behind it, so the list itself is pure n…

## What’s new and why it matters
We added a "Past attempts" list to the assessment centre dashboard. Each row is a title, a date, one number and a one-word caption. There is a /dashboard/exercises/report/<id> page behind it, so the list itself is pure navigation. The table it reads is not small per row. One attempt holds the candidate's answers and, where the exercise has written items, the full AI review of them, both as jsonb . Those columns are the point of the table and they are also the reason you cannot write the obvious query. select * ... where user_id = $1 limit 100 to render a hundred one-line rows means moving ever…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-248j

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
