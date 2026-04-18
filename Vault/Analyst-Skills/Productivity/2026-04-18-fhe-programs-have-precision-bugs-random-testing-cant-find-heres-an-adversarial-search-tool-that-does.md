---
title: FHE programs have precision bugs random testing can't find — here's an adversarial
  search tool that does
date: '2026-04-18'
source: https://dev.to/bader82t/fhe-programs-have-precision-bugs-random-testing-cant-find-heres-an-adversarial-search-tool-that-1f75
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-17-the-quote-as-ceiling-billing-pattern]]'
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-04-15-how-to-see-inside-your-ai-model-in-3-lines-of-python]]'
- '[[2026-03-28-how-to-add-reputation-scoring-to-your-langchain-agent-in-5-lines]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
status: unread
---

> **TL;DR:** FHE has a precision-testing problem, and random testing misses it If you compile an ML model to run under Fully Homomorphic Encryption, the encrypted and plaintext versions should give the same answer on every input. Und…

## What’s new and why it matters
FHE has a precision-testing problem, and random testing misses it If you compile an ML model to run under Fully Homomorphic Encryption, the encrypted and plaintext versions should give the same answer on every input. Under CKKS — the scheme most FHE ML deployments use — they usually do. But CKKS is approximate : noise accumulates across multiplications, and on specific inputs it can push the decrypted output far from the plaintext result. In one worked example from the patent specification behind this work, the plaintext circuit returns 0.893 on a particular input while the FHE circuit returns…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bader82t/fhe-programs-have-precision-bugs-random-testing-cant-find-heres-an-adversarial-search-tool-that-1f75

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-17-the-quote-as-ceiling-billing-pattern]]
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-04-15-how-to-see-inside-your-ai-model-in-3-lines-of-python]]
- [[2026-03-28-how-to-add-reputation-scoring-to-your-langchain-agent-in-5-lines]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
