---
title: Ollama num_ctx Truncated 287 of 400 Prompts and Never Told Me
date: '2026-10-10'
source: https://dev.to/ji_ai/ollama-numctx-truncated-287-of-400-prompts-and-never-told-me-4fi4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
status: unread
---

> **TL;DR:** My local RAG bot answered 46% of my test questions correctly. Llama 3.1 8B on Ollama, a 128K context window on the model card, retrieved chunks that I had checked by hand. The right paragraph was in the prompt every sing…

## What’s new and why it matters
My local RAG bot answered 46% of my test questions correctly. Llama 3.1 8B on Ollama, a 128K context window on the model card, retrieved chunks that I had checked by hand. The right paragraph was in the prompt every single time. The model just never saw it. Ollama's num_ctx was set to 2048 tokens, and Ollama quietly chopped the front off every prompt longer than that. No error, no field in the response, no warning in my Python logs. 287 of my 400 prompts got cut. This is the autopsy. TL;DR Ollama num_ctx is the context window Ollama actually allocates , not the one on the model card. In the ve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ji_ai/ollama-numctx-truncated-287-of-400-prompts-and-never-told-me-4fi4

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
