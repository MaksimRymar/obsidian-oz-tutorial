---
title: 'Data contracts for agents: what they miss and how to test meaning'
date: '2026-11-25'
source: https://dev.to/jacob_baruch_2a2aec3f6e3c/data-contracts-for-agents-what-they-miss-and-how-to-test-meaning-3c77
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-11-23-reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-and-identical]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-11-20-ducklake-vs-iceberg-which-table-format-for-a-small-team]]'
status: unread
---

> **TL;DR:** TL;DR. A data contract is a written, checked agreement between the people who produce or own a dataset and the people and agents who use it. The checks teams usually write (type, not null, fresh) test structure. The cost…

## What’s new and why it matters
TL;DR. A data contract is a written, checked agreement between the people who produce or own a dataset and the people and agents who use it. The checks teams usually write (type, not null, fresh) test structure. The costly failures change meaning and leave structure alone. Coding agents now sit on both sides: one changes the field, another reads it by its name. A contract protects you when it carries the meaning of each key field, two named owners and a rule that a change in meaning is a breaking change, and when it lives where your agent reads it. Use a plain meanings file before launch, add…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jacob_baruch_2a2aec3f6e3c/data-contracts-for-agents-what-they-miss-and-how-to-test-meaning-3c77

## Related notes
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-11-23-reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-and-identical]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-11-20-ducklake-vs-iceberg-which-table-format-for-a-small-team]]
