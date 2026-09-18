---
title: What I Learned Quantizing DistilBERT to ONNX for Browser Inference
date: '2026-09-18'
source: https://dev.to/fuxionixt/what-i-learned-quantizing-distilbert-to-onnx-for-browser-inference-5fok
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
status: unread
---

> **TL;DR:** What I Learned Quantizing DistilBERT to ONNX for Browser Inference I built a support-ticket classifier — 77 banking intents, fine-tuned DistilBERT, Banking77 — and got it to 92.2% accuracy. Then I tried to ship it, and r…

## What’s new and why it matters
What I Learned Quantizing DistilBERT to ONNX for Browser Inference I built a support-ticket classifier — 77 banking intents, fine-tuned DistilBERT, Banking77 — and got it to 92.2% accuracy. Then I tried to ship it, and ran into the actual problem: the checkpoint was 256 MB and took ~9 ms per query on CPU. That's fine on a GPU server. It is not fine as a static site with no backend, which is what I wanted this to be — no server to pay for, no cold start, no infra to babysit. The fix was exporting to ONNX and quantizing to int8, then running the whole thing client-side with Transformers.js. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fuxionixt/what-i-learned-quantizing-distilbert-to-onnx-for-browser-inference-5fok

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
