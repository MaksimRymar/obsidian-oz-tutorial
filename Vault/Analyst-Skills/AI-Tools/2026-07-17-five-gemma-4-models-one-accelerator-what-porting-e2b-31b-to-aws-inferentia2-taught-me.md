---
title: 'Five Gemma-4 models, one accelerator: what porting E2B 31B to AWS Inferentia2
  taught me'
date: '2026-07-17'
source: https://dev.to/aws-builders/five-gemma-4-models-one-accelerator-what-porting-e2b-31b-to-aws-inferentia2-taught-me-2980
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-07-17-my-inferentia-port-matched-its-reference-token-for-token-and-still-output-garbage]]'
- '[[2026-07-17-porting-a-128-expert-moe-gemma-4-26b-a4b-to-aws-inferentia2-where-every-rank-weighted-the-wrong-experts]]'
- '[[2026-07-17-porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
status: unread
---

> **TL;DR:** I ported the whole Gemma-4 family — E2B, E4B, 12B, 31B, and the 26B-A4B MoE — to run on AWS Inferentia2. Each has its own write-up in this series; this is the map. What's shared, what's different, how the recipe evolved…

## What’s new and why it matters
I ported the whole Gemma-4 family — E2B, E4B, 12B, 31B, and the 26B-A4B MoE — to run on AWS Inferentia2. Each has its own write-up in this series; this is the map. What's shared, what's different, how the recipe evolved from "trace it and pray" to a single-rank-compile pipeline that carries a 30-billion-parameter dense model and a 128-expert MoE — and the one bug that appears, in some costume, in **every * port.* The whole family at a glance E2B E4B 12B 31B 26B-A4B Params (total / active) ~5B / 2B ~8B / 4B 12B 31B 26B / ~4B Dense or sparse dense dense dense dense MoE (128 exp, top-8) Per-Layer…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-builders/five-gemma-4-models-one-accelerator-what-porting-e2b-31b-to-aws-inferentia2-taught-me-2980

## Related notes
- [[2026-07-17-my-inferentia-port-matched-its-reference-token-for-token-and-still-output-garbage]]
- [[2026-07-17-porting-a-128-expert-moe-gemma-4-26b-a4b-to-aws-inferentia2-where-every-rank-weighted-the-wrong-experts]]
- [[2026-07-17-porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
