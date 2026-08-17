---
title: Turn plain English into pandas code — with AST validation (free tool)
date: '2026-08-17'
source: https://dev.to/473185670/turn-plain-english-into-pandas-code-with-ast-validation-free-tool-46el
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
status: unread
---

> **TL;DR:** If you use pandas daily, you have probably burned minutes hunting for the right syntax. .agg() takes a dict or a list? .rolling() then .mean() — what is the window arg called? I built a tool: describe what you want in En…

## What’s new and why it matters
If you use pandas daily, you have probably burned minutes hunting for the right syntax. .agg() takes a dict or a list? .rolling() then .mean() — what is the window arg called? I built a tool: describe what you want in English, get syntax-validated pandas code back. Example Input: Group sales by month , calculate total revenue and average order size Output: df [ ' month ' ] = df [ ' date ' ]. dt . to_period ( ' M ' ) result = df . groupby ( ' month ' ). agg ( total_revenue = ( ' revenue ' , ' sum ' ), avg_order_size = ( ' order_size ' , ' mean ' ) ). reset_index () Note it auto-handled the date…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/473185670/turn-plain-english-into-pandas-code-with-ast-validation-free-tool-46el

## Related notes
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
