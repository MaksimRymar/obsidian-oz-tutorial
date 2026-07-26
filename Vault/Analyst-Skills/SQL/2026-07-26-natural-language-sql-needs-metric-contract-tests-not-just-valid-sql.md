---
title: Natural-language SQL needs metric contract tests, not just valid SQL
date: '2026-07-26'
source: https://dev.to/mads_hansen_27b33ebfee4c9/natural-language-sql-needs-metric-contract-tests-not-just-valid-sql-1ppp
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-11-natural-language-sql-needs-query-budgets]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]'
- '[[2026-07-18-finance-does-not-need-chatgpt-generated-sql-it-needs-governed-answers]]'
- '[[2026-05-12-schema-context-is-the-missing-layer-for-ai-database-agents]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
status: unread
---

> **TL;DR:** Valid SQL can still produce the wrong business answer. An AI SQL assistant may choose real tables, legal joins, and executable filters while misunderstanding what “active customer,” “revenue,” “churn,” or “open pipeline”…

## What’s new and why it matters
Valid SQL can still produce the wrong business answer. An AI SQL assistant may choose real tables, legal joins, and executable filters while misunderstanding what “active customer,” “revenue,” “churn,” or “open pipeline” means. So the production test should not stop at: did the SQL parse? did the query run? did it stay read-only? It should test a versioned metric contract. For every important metric, define: entity and grain eligible population and exclusions tenant and environment scope numerator, denominator, and state transitions time field, timezone, and late-arrival policy currency and pr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mads_hansen_27b33ebfee4c9/natural-language-sql-needs-metric-contract-tests-not-just-valid-sql-1ppp

## Related notes
- [[2026-05-11-natural-language-sql-needs-query-budgets]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]
- [[2026-07-18-finance-does-not-need-chatgpt-generated-sql-it-needs-governed-answers]]
- [[2026-05-12-schema-context-is-the-missing-layer-for-ai-database-agents]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
