---
title: 'vLLM Prefix Caching: One Timestamp Dropped My Hit Rate From 89% to 3%'
date: '2026-11-10'
source: https://dev.to/ji_ai/vllm-prefix-caching-one-timestamp-dropped-my-hit-rate-from-89-to-3-11ip
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-08-23-four-of-eight-kv-cache-bugs-are-bit-identical-at-step-1-so-the-check-everybody-writes-has-recall-exactly-0500]]'
- '[[2026-08-28-prompt-caching-strategies-to-cut-llm-costs-by-70]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
status: unread
---

> **TL;DR:** On Tuesday my support bot's time to first token roughly tripled, and nobody had touched the model, the GPU, or vLLM. The only change in the deploy was one helpful line at the top of the system prompt: Current date and ti…

## What’s new and why it matters
On Tuesday my support bot's time to first token roughly tripled, and nobody had touched the model, the GPU, or vLLM. The only change in the deploy was one helpful line at the top of the system prompt: Current date and time: 2026-10-27T14:03:22Z That line cost me almost all of my vLLM prefix caching. The server's stats line went from a prefix cache hit rate around 89% to around 3%. Every request was now prefilling a 2,400-token system prompt from scratch, because the timestamp at token 8 made every request look brand new to the cache. This post explains the mechanism: how vLLM prefix caching de…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ji_ai/vllm-prefix-caching-one-timestamp-dropped-my-hit-rate-from-89-to-3-11ip

## Related notes
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-08-23-four-of-eight-kv-cache-bugs-are-bit-identical-at-step-1-so-the-check-everybody-writes-has-recall-exactly-0500]]
- [[2026-08-28-prompt-caching-strategies-to-cut-llm-costs-by-70]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
