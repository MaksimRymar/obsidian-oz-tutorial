---
title: Two PyTorch ops that stopped a CUDA text model on an Apple GPU
date: '2026-10-28'
source: https://dev.to/leonewton253/two-pytorch-ops-that-stopped-a-cuda-text-model-on-an-apple-gpu-4jb5
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-09-24-our-two-state-ucc-run-returned-200-rows-127-filings-and-zero-from-colorado]]'
- '[[2026-09-22-duckdb-on-the-apple-silicon-gpu-plain-sql-19-of-22-tpc-h-queries-on-the-macs-own-gpu-and-a-rule-that-says-never-slower]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
- '[[2026-10-16-scraping-workday-job-listings-with-python-the-2000-job-cap-and-two-other-traps]]'
status: unread
---

> **TL;DR:** The Next-Concept Modeling eval scripts would not start on this Mac. PyTorch 2.14.1 reported the Apple GPU as available, and evaluate.py still exited with no GPU visible; pass --gpus . The model itself did not need a rewr…

## What’s new and why it matters
The Next-Concept Modeling eval scripts would not start on this Mac. PyTorch 2.14.1 reported the Apple GPU as available, and evaluate.py still exited with no GPU visible; pass --gpus . The model itself did not need a rewrite. The released configs already turn FlexAttention off and use scaled dot-product attention, linear layers, embeddings, and RoPE. Three call sites assumed CUDA. Two of those assumptions are real Metal limits, and the third is just device plumbing. The launcher only counted CUDA devices evaluate.py asked torch.cuda.device_count() and then set CUDA_VISIBLE_DEVICES for each shar…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/leonewton253/two-pytorch-ops-that-stopped-a-cuda-text-model-on-an-apple-gpu-4jb5

## Related notes
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-09-24-our-two-state-ucc-run-returned-200-rows-127-filings-and-zero-from-colorado]]
- [[2026-09-22-duckdb-on-the-apple-silicon-gpu-plain-sql-19-of-22-tpc-h-queries-on-the-macs-own-gpu-and-a-rule-that-says-never-slower]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
- [[2026-10-16-scraping-workday-job-listings-with-python-the-2000-job-cap-and-two-other-traps]]
