---
title: I Fine-Tuned a 7B Model on 549 A-Share Signal Samples. The Score Didn't Move
  — the Errors Did.
date: '2026-09-14'
source: https://dev.to/felixwang007/i-fine-tuned-a-7b-model-on-549-a-share-signal-samples-the-score-didnt-move-the-errors-did-44d3
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]'
status: unread
---

> **TL;DR:** I fine-tuned a 7B model to classify Chinese A-share signals. Setup cost me four minutes of GPU time and 549 training examples. The output looked right. Then I ran the same eval twice with 4x the LoRA rank and 2.7x the ep…

## What’s new and why it matters
I fine-tuned a 7B model to classify Chinese A-share signals. Setup cost me four minutes of GPU time and 549 training examples. The output looked right. Then I ran the same eval twice with 4x the LoRA rank and 2.7x the epochs — and the score landed in the same place. This post is the honest version of that experiment: what the data actually looked like, which knobs did nothing, and where the bottleneck really was (spoiler: it was never the model). The data: 549 samples, 12 stocks, 5 classes I collect A-share snapshots every trading day at 15:10 with a cron job. No paid API — Tencent's quote end…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/felixwang007/i-fine-tuned-a-7b-model-on-549-a-share-signal-samples-the-score-didnt-move-the-errors-did-44d3

## Related notes
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]
