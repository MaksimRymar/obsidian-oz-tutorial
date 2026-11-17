---
title: Build a Tiny LLM Output Evaluation Harness in Python (No Framework Required)
date: '2026-11-17'
source: https://dev.to/tamer_kalla/build-a-tiny-llm-output-evaluation-harness-in-python-no-framework-required-14e9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-26-a-free-model-swap-is-not-a-config-change-a-contract-probe-you-can-run]]'
- '[[2026-11-01-dbt-tests-that-actually-catch-something]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
status: unread
---

> **TL;DR:** The problem Every team I have seen wire an LLM into a production service eventually ships the same bug: somebody improves a prompt, the demo looks great, and a downstream consumer quietly breaks. The summarizer stops inc…

## What’s new and why it matters
The problem Every team I have seen wire an LLM into a production service eventually ships the same bug: somebody improves a prompt, the demo looks great, and a downstream consumer quietly breaks. The summarizer stops including the one field the ticket parser needs. The classifier starts answering "The sentiment is positive" instead of "positive", and the exact-match routing downstream falls over. The extraction step returns JSON wrapped in markdown fences, and json.loads throws at 2 a.m. None of these are model-quality problems. They are contract problems. The model team changed the shape of t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tamer_kalla/build-a-tiny-llm-output-evaluation-harness-in-python-no-framework-required-14e9

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-26-a-free-model-swap-is-not-a-config-change-a-contract-probe-you-can-run]]
- [[2026-11-01-dbt-tests-that-actually-catch-something]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
