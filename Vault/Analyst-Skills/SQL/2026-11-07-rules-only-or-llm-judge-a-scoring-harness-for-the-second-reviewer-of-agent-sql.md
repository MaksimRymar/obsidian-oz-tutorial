---
title: Rules-Only or LLM Judge? A Scoring Harness for the Second Reviewer of Agent
  SQL
date: '2026-11-07'
source: https://dev.to/dataio_4921/rules-only-or-llm-judge-a-scoring-harness-for-the-second-reviewer-of-agent-sql-2ihe
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-17-transpile-or-re-ask-fixing-dialect-breaks-in-agent-written-sql]]'
- '[[2026-11-06-retry-the-cheap-model-or-escalate-a-decision-rule-for-failed-agent-sql-drafts]]'
- '[[2026-10-26-review-cost-per-section-decides-who-drafts-it-a-stop-rule-for-model-assisted-docs]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-10-19-a-read-only-sql-guard-for-llm-generated-queries-with-sqlglot]]'
status: unread
---

> **TL;DR:** Rules-Only or LLM Judge? A Scoring Harness for the Second Reviewer of Agent SQL Two engineers are looking at the same pull request. One of them added llm_judge.py , a second model call that re-reads every SQL draft befor…

## What’s new and why it matters
Rules-Only or LLM Judge? A Scoring Harness for the Second Reviewer of Agent SQL Two engineers are looking at the same pull request. One of them added llm_judge.py , a second model call that re-reads every SQL draft before the read-only warehouse role ever sees it. The other objects on latency, cost, and nondeterminism, and answers that the rule engine missed two incidents last quarter. Neither engineer has a number, so the thread keeps recycling the same two anecdotes in slightly different wording. This article replaces that argument with a harness. You label a set of drafts once, run both rev…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/rules-only-or-llm-judge-a-scoring-harness-for-the-second-reviewer-of-agent-sql-2ihe

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-17-transpile-or-re-ask-fixing-dialect-breaks-in-agent-written-sql]]
- [[2026-11-06-retry-the-cheap-model-or-escalate-a-decision-rule-for-failed-agent-sql-drafts]]
- [[2026-10-26-review-cost-per-section-decides-who-drafts-it-a-stop-rule-for-model-assisted-docs]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-10-19-a-read-only-sql-guard-for-llm-generated-queries-with-sqlglot]]
