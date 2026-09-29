---
title: My Agent Never Hallucinates Invoice Decisions — Here's the Hard Rule That Prevents
  It
date: '2026-09-29'
source: https://dev.to/erehh07/my-agent-never-hallucinates-invoice-decisions-heres-the-hard-rule-that-prevents-it-1888
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-09-29-my-invoice-agent-went-from-100-escalation-to-7-heres-the-memory-layer-that-did-it]]'
status: unread
---

> **TL;DR:** I've watched LLMs confidently recommend approving an invoice for an amount that doesn't appear in the purchase order, the invoice, or any past decision. They do it with high confidence and well-structured reasoning. The…

## What’s new and why it matters
I've watched LLMs confidently recommend approving an invoice for an amount that doesn't appear in the purchase order, the invoice, or any past decision. They do it with high confidence and well-structured reasoning. The reasoning sounds right. The number is invented. For accounts-payable decisions, that's not an acceptable failure mode. I spent more time on the prevention mechanism than on any other part of MemoryOps. The Root Cause LLMs hallucinate in recommendation tasks for a specific reason: they're asked to reason about a space of possible answers, and they have no reliable way to disting…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/erehh07/my-agent-never-hallucinates-invoice-decisions-heres-the-hard-rule-that-prevents-it-1888

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-09-29-my-invoice-agent-went-from-100-escalation-to-7-heres-the-memory-layer-that-did-it]]
