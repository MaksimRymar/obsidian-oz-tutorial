---
title: SQL Agents Need Business Context, Not Just Schema
date: '2026-10-05'
source: https://dev.to/mech_app_ai/sql-agents-need-business-context-not-just-schema-8a1
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-15-building-answer-lineage-for-enterprise-data-agents]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-07-the-semantic-cold-start-problem-in-enterprise-data-agents]]'
- '[[2026-08-20-beyond-sql-accuracy-building-evidence-chains-for-ai-data-agents]]'
- '[[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]'
status: unread
---

> **TL;DR:** A SQL agent sees a table called orders with columns promised_date , delivery_date , and status . You ask it for the on-time delivery rate. It generates a query, the query runs, and you get a number. The number is wrong b…

## What’s new and why it matters
A SQL agent sees a table called orders with columns promised_date , delivery_date , and status . You ask it for the on-time delivery rate. It generates a query, the query runs, and you get a number. The number is wrong because the agent guessed the formula. The real definition lives in a Confluence page, a Looker dashboard, or someone's head. Schema alone does not encode business semantics. This is the core problem every data team hits when deploying text-to-SQL agents in production. The LiveSQLBench Example LiveSQLBench includes a disaster relief database with a distributionhubs table. The be…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mech_app_ai/sql-agents-need-business-context-not-just-schema-8a1

## Related notes
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-15-building-answer-lineage-for-enterprise-data-agents]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-07-the-semantic-cold-start-problem-in-enterprise-data-agents]]
- [[2026-08-20-beyond-sql-accuracy-building-evidence-chains-for-ai-data-agents]]
- [[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]
