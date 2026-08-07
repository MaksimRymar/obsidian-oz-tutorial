---
title: 'A SELECT-only prompt is not a sandbox: bounding agent-generated SQL'
date: '2026-08-06'
source: https://dev.to/yhay81/a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql-3mga
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
status: unread
---

> **TL;DR:** Suppose an AI agent has one job: read package.json and return the package name and version. You can put “use only SELECT ” in the prompt. But if the SQL engine can still open another file, load an extension, run forever,…

## What’s new and why it matters
Suppose an AI agent has one job: read package.json and return the package name and version. You can put “use only SELECT ” in the prompt. But if the SQL engine can still open another file, load an extension, run forever, or overwrite an output path, the prompt has not created a security boundary. It has only described one. I ran into this distinction while building sqrail , a small DuckDB-based executor for analytical SQL over explicitly named files. The useful lesson was not about generating better SQL. It was about turning the agent's request into a process contract that remains true when th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/yhay81/a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql-3mga

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
