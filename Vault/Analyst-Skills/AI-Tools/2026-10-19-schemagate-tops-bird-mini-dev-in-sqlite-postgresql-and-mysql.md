---
title: schemagate tops BIRD Mini-Dev in SQLite, PostgreSQL and MySQL
date: '2026-10-19'
source: https://dev.to/ashish_sinha_5241c7673d93/schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql-372d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]'
- '[[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
status: unread
---

> **TL;DR:** BIRD Mini-Dev is 500 text-to-SQL questions over 11 real databases, in three dialects. It is scored by execution accuracy: run the query, and compare its rows with the gold query's rows. I ran schemagate on all of it. Eve…

## What’s new and why it matters
BIRD Mini-Dev is 500 text-to-SQL questions over 11 real databases, in three dialects. It is scored by execution accuracy: run the query, and compare its rows with the gold query's rows. I ran schemagate on all of it. Every number below comes from BIRD's own evaluator. schemagate + Claude Opus 5.5 #1 until now that entry's model SQLite 81.0 75.6 (Jitto Build) Claude Opus 5.5 PostgreSQL 72.6 65.8 (Ontology2SQL) deepseek-v4-flash, as a 12-step agent MySQL 72.4 49.2 (TA + GPT-4) GPT-4 SQLite is the like-for-like result. The previous #1 uses the same model (per JamLabs' own LiveSQLBench listing), a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql-372d

## Related notes
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]
- [[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
