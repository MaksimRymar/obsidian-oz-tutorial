---
title: 'vLLM vs SGLang: PagedAttention vs RadixAttention Benchmarks'
date: '2026-09-10'
source: https://dev.to/youngones/vllm-vs-sglang-pagedattention-vs-radixattention-benchmarks-1bk6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-08-contextlens-py-spypprof-but-for-whats-inside-your-llm-prompt]]'
- '[[2026-05-14-from-cold-starts-to-hot-paths-how-i-cut-llm-inference-latency-by-40-with-a-simple-routing-trick]]'
- '[[2026-08-11-automating-llm-agent-memory-testing-with-playwright-10x-efficiency-boost]]'
- '[[2026-08-28-prompt-caching-strategies-to-cut-llm-costs-by-70]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-08-17-retry-the-request-not-the-prompt-an-error-taxonomy-for-free-coding-models]]'
status: unread
---

> **TL;DR:** Direct Answer: In our empirical benchmarks on multi-turn agent workflows, SGLang's RadixAttention outperformed vLLM's PagedAttention Automatic Prefix Caching (APC), slashing warm Time-To-First-Token (TTFT) from 184ms to…

## What’s new and why it matters
Direct Answer: In our empirical benchmarks on multi-turn agent workflows, SGLang's RadixAttention outperformed vLLM's PagedAttention Automatic Prefix Caching (APC), slashing warm Time-To-First-Token (TTFT) from 184ms to 68ms (an 82.9% latency reduction over cold prefill) and boosting sustained throughput by 39.8%. While vLLM remains superior for broad hardware support and speculative decoding, SGLang is currently the de facto serving engine for agentic tool loops. Why Agentic AI Workloads Break Traditional LLM Serving Traditional LLM serving engines were architected for single-turn text genera…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/youngones/vllm-vs-sglang-pagedattention-vs-radixattention-benchmarks-1bk6

## Related notes
- [[2026-06-08-contextlens-py-spypprof-but-for-whats-inside-your-llm-prompt]]
- [[2026-05-14-from-cold-starts-to-hot-paths-how-i-cut-llm-inference-latency-by-40-with-a-simple-routing-trick]]
- [[2026-08-11-automating-llm-agent-memory-testing-with-playwright-10x-efficiency-boost]]
- [[2026-08-28-prompt-caching-strategies-to-cut-llm-costs-by-70]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-08-17-retry-the-request-not-the-prompt-an-error-taxonomy-for-free-coding-models]]
