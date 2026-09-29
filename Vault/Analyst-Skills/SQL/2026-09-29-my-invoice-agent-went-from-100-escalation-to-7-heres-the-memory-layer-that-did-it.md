---
title: My Invoice Agent Went From 100% Escalation to 7% — Here's the Memory Layer
  That Did It
date: '2026-09-29'
source: https://dev.to/karthik_smart_01/my-invoice-agent-went-from-100-escalation-to-7-heres-the-memory-layer-that-did-it-j40
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
status: unread
---

> **TL;DR:** The first time I ran the agent against a batch of invoices, it escalated every single one. 17 exceptions, 17 escalations, 17 "no precedent found." I had built a very expensive escalation machine. Three batches later, the…

## What’s new and why it matters
The first time I ran the agent against a batch of invoices, it escalated every single one. 17 exceptions, 17 escalations, 17 "no precedent found." I had built a very expensive escalation machine. Three batches later, the escalation rate was 7%. The agent was resolving 93% of exceptions autonomously, with citations. Here's what changed. The Starting Point MemoryOps processes accounts-payable invoice exceptions. When a vendor invoices an amount that doesn't match the purchase order or the goods receipt, the system flags it and the agent recommends what to do: approve it, reject it, adjust it, or…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/karthik_smart_01/my-invoice-agent-went-from-100-escalation-to-7-heres-the-memory-layer-that-did-it-j40

## Related notes
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
