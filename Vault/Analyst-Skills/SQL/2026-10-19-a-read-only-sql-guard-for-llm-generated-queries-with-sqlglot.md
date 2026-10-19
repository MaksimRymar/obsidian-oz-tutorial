---
title: A read-only SQL guard for LLM-generated queries with sqlglot
date: '2026-10-19'
source: https://dev.to/datanestdigital/a-read-only-sql-guard-for-llm-generated-queries-with-sqlglot-418j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** The fastest way to learn that "the model would never do that" is a false statement is to give an LLM a database connection. A text-to-SQL agent will, sooner or later, emit a DROP , a DELETE without a WHERE , or a cartesi…

## What’s new and why it matters
The fastest way to learn that "the model would never do that" is a false statement is to give an LLM a database connection. A text-to-SQL agent will, sooner or later, emit a DROP , a DELETE without a WHERE , or a cartesian join over your biggest table. Sometimes because a user asked for it, sometimes because a prompt injection hid in a column value, and sometimes just because it felt creative. The usual first defence is if sql.strip().lower().startswith("select") . It fails in at least three fun ways: SELECT 1; DROP TABLE orders , a CTE that hides an INSERT , and (in DuckDB) SELECT * FROM read…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datanestdigital/a-read-only-sql-guard-for-llm-generated-queries-with-sqlglot-418j

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-09-15-sql-joins-explained]]
