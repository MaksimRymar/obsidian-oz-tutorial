---
title: I Counted the Turns That Didn't Need a Model
date: '2026-09-11'
source: https://dev.to/hackhub_6179/i-counted-the-turns-that-didnt-need-a-model-1j6p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]'
status: unread
---

> **TL;DR:** Half of a convincing agent loop is a state machine wearing a chat template. I did not believe that until I scored turns instead of demos. The model can still be useful. The question is which turns actually required it. Y…

## What’s new and why it matters
Half of a convincing agent loop is a state machine wearing a chat template. I did not believe that until I scored turns instead of demos. The model can still be useful. The question is which turns actually required it. You have seen the other version of this story. A loop, a tool list, a thought field, a screenshot. It looks like software that thinks. Then you watch it radio headquarters to ask whether priority=low and status=open should skip the on-call queue. That is not reasoning. That is a missing if . So I built a harness that asks a ruder question than "did the agent finish?" Did this tu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hackhub_6179/i-counted-the-turns-that-didnt-need-a-model-1j6p

## Related notes
- [[2026-09-07-score-the-trace-not-the-final-payload]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]
