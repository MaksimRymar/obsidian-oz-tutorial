---
title: My Inferentia port matched its reference token-for-token — and still output
  garbage
date: '2026-07-17'
source: https://dev.to/xbill/my-inferentia-port-matched-its-reference-token-for-token-and-still-output-garbage-16d4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-17-porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-05-26-i-did-the-math-your-serpapi-bill-is-10x-what-it-should-be]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
status: unread
---

> **TL;DR:** I ported Google's biggest open Gemma-4 — the 30-billion-parameter dense model — to AWS Inferentia2. The compiled model passed my strictest check: its output was token-for-token identical to the CPU reference. It was also…

## What’s new and why it matters
I ported Google's biggest open Gemma-4 — the 30-billion-parameter dense model — to AWS Inferentia2. The compiled model passed my strictest check: its output was token-for-token identical to the CPU reference. It was also complete gibberish. Both facts were true at the same time, and the reason is a lesson worth more than the port. This is the sequel to porting the smaller Gemma-4 models (E2B/E4B/12B). Those were hard because of architecture — Per-Layer Embeddings, cross-layer KV-sharing, MatFormer nesting. The 31B throws all of that away and hands you a different kind of hard: scale . And a tr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/xbill/my-inferentia-port-matched-its-reference-token-for-token-and-still-output-garbage-16d4

## Related notes
- [[2026-07-17-porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-05-26-i-did-the-math-your-serpapi-bill-is-10x-what-it-should-be]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
