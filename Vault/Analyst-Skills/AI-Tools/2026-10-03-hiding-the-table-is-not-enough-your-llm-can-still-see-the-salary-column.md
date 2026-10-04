---
title: Hiding the table is not enough. Your LLM can still see the salary column.
date: '2026-10-03'
source: https://dev.to/ashish_sinha_5241c7673d93/hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column-12ne
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-08-29-how-to-set-up-duckdb-run-sql-on-a-csv-with-no-import-step]]'
status: unread
---

> **TL;DR:** Most text-to-SQL setups protect data at the table level. The analyst cannot read hr_compensation , so that table never goes into the prompt. Good. But a lot of sensitive data does not live in its own table. It lives in o…

## What’s new and why it matters
Most text-to-SQL setups protect data at the table level. The analyst cannot read hr_compensation , so that table never goes into the prompt. Good. But a lot of sensitive data does not live in its own table. It lives in one column of a table everyone uses. employees.salary . customers.national_id . patients.diagnosis . If the model sees the column name in the schema, it will happily write SELECT salary FROM employees . Your database might block the query, or it might not. Either way, the model has already learned the column exists. schemagate 1.1.0 adds column rules you can write in a JSON file…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column-12ne

## Related notes
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-08-29-how-to-set-up-duckdb-run-sql-on-a-csv-with-no-import-step]]
