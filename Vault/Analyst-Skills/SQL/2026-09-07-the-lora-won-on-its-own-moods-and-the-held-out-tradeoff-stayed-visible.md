---
title: The LoRA won on its own moods, and the held-out tradeoff stayed visible
date: '2026-09-07'
source: https://dev.to/ilya_mozerov_867dbdd91feb/the-lora-won-on-its-own-moods-and-the-held-out-tradeoff-stayed-visible-9i
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-04-your-llm-sends-valid-data-in-an-invalid-shape]]'
- '[[2026-09-05-the-watchdog-that-got-its-own-leash]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-08-03-building-a-3d-scene-from-30-photos-getting-gaussian-splatting-running-on-colab]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-07-17-context-engineering-isnt-enough-a-loop-engineering-experiment-with-no-llm-inside-the-loop]]'
status: unread
---

> **TL;DR:** I wanted a small answer to a practical question: can two topic-specific LoRA adapters improve perplexity on their own topic without simply making the model better at everything? The experiment used two specialists, guita…

## What’s new and why it matters
I wanted a small answer to a practical question: can two topic-specific LoRA adapters improve perplexity on their own topic without simply making the model better at everything? The experiment used two specialists, guitar and sourdough . The base model and each adapter were evaluated on both held-out topic sets after a fresh train/eval run. guitar-ppl sourdough-ppl base 18.2 19.4 lora-guitar 11.3 15.4 lora-sourdough 13.7 12.2 The intended effect is visible: each adapter is best on its own topic. The cross-topic numbers also make the tradeoff visible. lora-guitar improves sourdough over base, b…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ilya_mozerov_867dbdd91feb/the-lora-won-on-its-own-moods-and-the-held-out-tradeoff-stayed-visible-9i

## Related notes
- [[2026-08-04-your-llm-sends-valid-data-in-an-invalid-shape]]
- [[2026-09-05-the-watchdog-that-got-its-own-leash]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-08-03-building-a-3d-scene-from-30-photos-getting-gaussian-splatting-running-on-colab]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-07-17-context-engineering-isnt-enough-a-loop-engineering-experiment-with-no-llm-inside-the-loop]]
