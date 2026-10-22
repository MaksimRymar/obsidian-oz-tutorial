---
title: I was tired of letting the OOM killer do my VRAM math, so I wrote a one-file
  CLI
date: '2026-10-22'
source: https://dev.to/techdevfun/i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli-4lge
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
- '[[2026-10-14-google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser]]'
- '[[2026-10-16-i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090]]'
- '[[2026-07-27-my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it]]'
status: unread
---

> **TL;DR:** My workflow for trying a new local model used to be: download 4 GB, watch the progress bar, then read failed to allocate 3412 MiB like it was a fortune cookie. The math that would have saved me fits on a napkin — weights…

## What’s new and why it matters
My workflow for trying a new local model used to be: download 4 GB, watch the progress bar, then read failed to allocate 3412 MiB like it was a fortune cookie. The math that would have saved me fits on a napkin — weights, plus KV cache, plus overhead — but nobody does it before downloading, because the tools that do it live in a browser tab and want you to type in the parameter count by hand. The file is sitting right there on your disk. It knows its own parameter count. So I wrote ggufit : one Python file, standard library only, no install. Point it at a .gguf file and it reads the actual hea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/techdevfun/i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli-4lge

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
- [[2026-10-14-google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser]]
- [[2026-10-16-i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090]]
- [[2026-07-27-my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it]]
