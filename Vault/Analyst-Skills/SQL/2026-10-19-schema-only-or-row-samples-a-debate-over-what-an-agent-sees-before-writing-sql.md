---
title: 'Schema-Only or Row Samples: A Debate Over What an Agent Sees Before Writing
  SQL'
date: '2026-10-19'
source: https://dev.to/dataio_4921/schema-only-or-row-samples-a-debate-over-what-an-agent-sees-before-writing-sql-47md
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** Schema-Only or Row Samples: A Debate Over What an Agent Sees Before Writing SQL A review queue where two reviewers disagree The scenario repeats in most teams that let an agent draft SQL: a query passes review, runs in s…

## What’s new and why it matters
Schema-Only or Row Samples: A Debate Over What an Agent Sees Before Writing SQL A review queue where two reviewers disagree The scenario repeats in most teams that let an agent draft SQL: a query passes review, runs in staging, and returns something plausible that is still wrong. One reviewer blames the prompt for hiding the data, while another blames the habit of pasting production rows into a model context. Both are describing the same defect from opposite ends of the pipeline, and neither has a measurement that settles the argument. An illustrative example: the request is "active customers…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/schema-only-or-row-samples-a-debate-over-what-an-agent-sees-before-writing-sql-47md

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
