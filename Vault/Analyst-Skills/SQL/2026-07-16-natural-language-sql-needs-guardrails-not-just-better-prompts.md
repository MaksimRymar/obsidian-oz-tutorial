---
title: Natural language SQL needs guardrails, not just better prompts
date: '2026-07-16'
source: https://dev.to/mads_hansen_27b33ebfee4c9/natural-language-sql-needs-guardrails-not-just-better-prompts-33gg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-11-natural-language-sql-needs-query-budgets]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-05-12-schema-context-is-the-missing-layer-for-ai-database-agents]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-06-05-why-text-to-sql-needs-relationship-context-not-just-better-prompts]]'
- '[[2026-04-27-from-chaos-to-clarity-how-sql-transforms-raw-data-into-powerful-stories]]'
status: unread
---

> **TL;DR:** Natural language SQL demos are easy. Ask a question. Get an answer. Production is different. The real workflow should look more like this: Map the question to curated schema context Check tenant and role scope Prefer app…

## What’s new and why it matters
Natural language SQL demos are easy. Ask a question. Get an answer. Production is different. The real workflow should look more like this: Map the question to curated schema context Check tenant and role scope Prefer approved views for known metrics Estimate query cost before execution Enforce row limits, timeouts, and query budgets Return answer provenance with the result The dangerous version is letting the model discover raw tables and generate whatever SQL seems plausible. A read-only role helps, but it is not enough by itself. A read-only query can still expose sensitive columns, scan too…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mads_hansen_27b33ebfee4c9/natural-language-sql-needs-guardrails-not-just-better-prompts-33gg

## Related notes
- [[2026-05-11-natural-language-sql-needs-query-budgets]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-05-12-schema-context-is-the-missing-layer-for-ai-database-agents]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-06-05-why-text-to-sql-needs-relationship-context-not-just-better-prompts]]
- [[2026-04-27-from-chaos-to-clarity-how-sql-transforms-raw-data-into-powerful-stories]]
