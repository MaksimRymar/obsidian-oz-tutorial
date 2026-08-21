---
title: We tested "tokenize before you compress" against 452 configurations, and it
  mostly held up
date: '2026-08-21'
source: https://dev.to/ronak_parmar_033c50d168b5/we-tested-tokenize-before-you-compress-against-452-configurations-and-it-mostly-held-up-4m6p
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
status: unread
---

> **TL;DR:** A few weeks ago my friend @u84u and I ( @ronak-create ) had a simple, slightly annoying question: if LLMs get 30-45% smaller representations of text by tokenizing it into subwords instead of raw bytes, why don't we token…

## What’s new and why it matters
A few weeks ago my friend @u84u and I ( @ronak-create ) had a simple, slightly annoying question: if LLMs get 30-45% smaller representations of text by tokenizing it into subwords instead of raw bytes, why don't we tokenize text before handing it to a byte-level compressor like LZMA or zstd? It felt like the kind of idea someone must have already tried and quietly dropped. So instead of writing a blog post about the idea, we built the harness to actually test it, and the result is parmar — a subword-tokenization pre-filter for byte-level compressors, plus a fairly paranoid benchmarking rig to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ronak_parmar_033c50d168b5/we-tested-tokenize-before-you-compress-against-452-configurations-and-it-mostly-held-up-4m6p

## Related notes
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
