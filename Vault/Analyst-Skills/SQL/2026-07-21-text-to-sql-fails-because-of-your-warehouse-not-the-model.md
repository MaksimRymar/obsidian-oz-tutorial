---
title: Text-to-SQL Fails Because of Your Warehouse, Not the Model
date: '2026-07-21'
source: https://dev.to/konstantinas_mamonas/text-to-sql-fails-because-of-your-warehouse-not-the-model-3no5
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#presentations'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-05-02-ai-sql-assistant-or-mcp-database-server-they-are-not-the-same-thing]]'
- '[[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** I've been experimenting with pointing LLMs at databases through MCP servers and asking them questions. The results followed a pattern. First, the model would simply make up tables and columns that didn't exist, then writ…

## What’s new and why it matters
I've been experimenting with pointing LLMs at databases through MCP servers and asking them questions. The results followed a pattern. First, the model would simply make up tables and columns that didn't exist, then write plausible-looking SQL against them. Giving it tools to investigate the schema fixed the first failure: it could list tables and describe columns, and it stopped making up structure it could now look up. But a subtler failure was left behind. When it wasn't clear what a column meant, the model didn't ask and didn't flag it. It picked an interpretation and ran with it. That sec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/konstantinas_mamonas/text-to-sql-fails-because-of-your-warehouse-not-the-model-3no5

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-05-02-ai-sql-assistant-or-mcp-database-server-they-are-not-the-same-thing]]
- [[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
