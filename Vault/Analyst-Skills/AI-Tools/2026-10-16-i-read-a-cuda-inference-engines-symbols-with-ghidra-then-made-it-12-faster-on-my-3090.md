---
title: I read a CUDA inference engine's symbols with Ghidra, then made it 12% faster
  on my 3090
date: '2026-10-16'
source: https://dev.to/prodbymarcu/i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090-2c3l
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
status: unread
---

> **TL;DR:** I run one job at home that never sleeps, a coder model quantized to IQ1_M on an RTX 3090, and my agent sessions hit it all day. Before I changed a single flag I wanted to know what the binary was actually doing, so I rea…

## What’s new and why it matters
I run one job at home that never sleeps, a coder model quantized to IQ1_M on an RTX 3090, and my agent sessions hit it all day. Before I changed a single flag I wanted to know what the binary was actually doing, so I read it. The engine is Strata 0.1.44, behind a systemd service on :8090 , with llama-swap on :8080 proxying it so a whole GGUF collection shares one entry point. Reading the binary Ghidra 12.1.4, headless, on the Linux box. 40 segments, 8.88 MiB of host code in .text , 50.3 MiB of CUDA fatbin images and every one of them built for sm_86 , which is the card I own, so there's no JIT…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prodbymarcu/i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090-2c3l

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
