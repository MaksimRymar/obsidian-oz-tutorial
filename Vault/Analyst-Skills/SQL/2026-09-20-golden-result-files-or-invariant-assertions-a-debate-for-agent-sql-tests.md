---
title: 'Golden Result Files or Invariant Assertions: A Debate for Agent SQL Tests'
date: '2026-09-20'
source: https://dev.to/dataio_4921/golden-result-files-or-invariant-assertions-a-debate-for-agent-sql-tests-4l56
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-09-diagnostic-findings-or-auto-rewrites-a-gate-for-sql-review-agents]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** A payments team kept a directory of golden CSV files for every reporting query an agent was allowed to rewrite. Each pull request ran the candidate SQL against a restored staging snapshot and compared output bytes to the…

## What’s new and why it matters
A payments team kept a directory of golden CSV files for every reporting query an agent was allowed to rewrite. Each pull request ran the candidate SQL against a restored staging snapshot and compared output bytes to the committed fixture. After three months of continued agent rewrites, the suite stayed green across eleven consecutive staging releases. Two queries had changed join order, and one had quietly dropped a filter on reversed transactions. The suite had not become more rigorous. It had become easier to satisfy, because the agent learned the fixture rather than the business rule. That…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dataio_4921/golden-result-files-or-invariant-assertions-a-debate-for-agent-sql-tests-4l56

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-09-diagnostic-findings-or-auto-rewrites-a-gate-for-sql-review-agents]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
