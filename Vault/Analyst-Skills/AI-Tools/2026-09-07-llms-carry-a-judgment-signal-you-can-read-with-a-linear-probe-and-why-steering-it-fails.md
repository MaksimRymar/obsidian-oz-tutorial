---
title: LLMs carry a judgment signal you can read with a linear probe (and why steering
  it fails)
date: '2026-09-07'
source: https://dev.to/ai_openfree_b23025ef075cf/llms-carry-a-judgment-signal-you-can-read-with-a-linear-probe-and-why-steering-it-fails-31ng
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-04-21-how-we-certify-ai-reliability-with-one-number-conformal-prediction-for-llms-open-source]]'
- '[[2026-08-07-your-text-to-sql-model-isnt-as-wrong-as-your-benchmark-says-the-gold-sql-is]]'
- '[[2026-06-22-catch-llm-hallucinations-with-multi-model-consensus]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** LLMs carry a judgment signal you can read with a linear probe (and why steering it fails) LLM hidden states encode reward-related information: roughly, whether the current trajectory is heading toward a correct answer. W…

## What’s new and why it matters
LLMs carry a judgment signal you can read with a linear probe (and why steering it fails) LLM hidden states encode reward-related information: roughly, whether the current trajectory is heading toward a correct answer. We reproduced this on our own hardware, added the controls we felt were missing, and got a clear picture of what the signal can and cannot do. Setup Generate N answers, label each by final correctness Take the last-token hidden state at layer L Fit a linear probe (ridge) predicting correctness Report AUC on a held-out set No fine-tuning, no extra model. Result 1: the signal is r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ai_openfree_b23025ef075cf/llms-carry-a-judgment-signal-you-can-read-with-a-linear-probe-and-why-steering-it-fails-31ng

## Related notes
- [[2026-04-21-how-we-certify-ai-reliability-with-one-number-conformal-prediction-for-llms-open-source]]
- [[2026-08-07-your-text-to-sql-model-isnt-as-wrong-as-your-benchmark-says-the-gold-sql-is]]
- [[2026-06-22-catch-llm-hallucinations-with-multi-model-consensus]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
