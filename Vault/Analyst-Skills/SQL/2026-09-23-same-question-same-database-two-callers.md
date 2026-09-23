---
title: Same question, same database, two callers
date: '2026-09-23'
source: https://dev.to/ashish_sinha_5241c7673d93/same-question-same-database-two-callers-4df4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
status: unread
---

> **TL;DR:** Most text-to-SQL stacks send the model the whole schema and put the access check after the query is written. That ordering is the bug, and it is easier to show than to argue about. The whole idea in one picture Left -- t…

## What’s new and why it matters
Most text-to-SQL stacks send the model the whole schema and put the access check after the query is written. That ordering is the bug, and it is easier to show than to argue about. The whole idea in one picture Left -- the caller holds no roles. hr_compensation never reaches the model at all: 9 of 42 objects selected, 570 prompt tokens instead of 2,511, one object hidden from this caller. Right -- same question, same schema, same database. The caller now holds the payroll role, so hr_compensation is the first table in the prompt, and nothing is hidden. Nothing about the question changed. The i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/same-question-same-database-two-callers-4df4

## Related notes
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
