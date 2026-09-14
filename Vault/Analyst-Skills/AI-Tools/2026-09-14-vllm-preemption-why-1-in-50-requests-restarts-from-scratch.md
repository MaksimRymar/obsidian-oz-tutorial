---
title: 'vLLM Preemption: Why 1 in 50 Requests Restarts From Scratch'
date: '2026-09-14'
source: https://dev.to/ji_ai/vllm-preemption-why-1-in-50-requests-restarts-from-scratch-32kk
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-07-every-extra-hop-buys-another-queue-ticket]]'
- '[[2026-04-30-how-to-serve-mistral-medium-35-128b-without-running-out-of-gpu-memory]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Our chat endpoint had a mean latency of 1.9s and a p99 of 11.4s. Same model. Same GPU. Same prompt template. nvidia-smi showed 96% utilization and no memory pressure worth mentioning. Nothing crashed. Nothing retried. Bu…

## What’s new and why it matters
Our chat endpoint had a mean latency of 1.9s and a p99 of 11.4s. Same model. Same GPU. Same prompt template. nvidia-smi showed 96% utilization and no memory pressure worth mentioning. Nothing crashed. Nothing retried. But roughly one request in fifty would stream a few tokens, freeze for six seconds mid-sentence, then finish normally like nothing happened. That freeze has a name: vLLM preemption . The scheduler evicted a request that was already 80% done, threw away every KV block it had built up, and put it back in the queue to be prefilled again from token zero. My users paid for those token…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ji_ai/vllm-preemption-why-1-in-50-requests-restarts-from-scratch-32kk

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-07-every-extra-hop-buys-another-queue-ticket]]
- [[2026-04-30-how-to-serve-mistral-medium-35-128b-without-running-out-of-gpu-memory]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
