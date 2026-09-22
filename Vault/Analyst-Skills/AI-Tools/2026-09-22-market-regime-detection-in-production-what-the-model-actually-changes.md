---
title: 'Market regime detection in production: what the model actually changes'
date: '2026-09-22'
source: https://dev.to/mohammed_arshadansari_f2/market-regime-detection-in-production-what-the-model-actually-changes-3i3i
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-07-02-an-al-writes-my-trading-code-three-gates-decide-if-it-ever-runs]]'
- '[[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-28-free-ai-compute-paid-review-queues-a-structured-debate-on-zero-dollar-sql-review]]'
- '[[2026-08-21-shipping-12-ios-apps-to-the-app-store-unattended-part-2-every-review-trap-beta-builds-rejected-pricing-name-collisions]]'
status: unread
---

> **TL;DR:** A while ago I wrote up two ways to detect market regimes : hidden Markov models and clustering on Wasserstein distance. That post was research on a toy S&P 500 series. This one is what actually runs, every trading day, i…

## What’s new and why it matters
A while ago I wrote up two ways to detect market regimes : hidden Markov models and clustering on Wasserstein distance. That post was research on a toy S&P 500 series. This one is what actually runs, every trading day, inside the trading system behind Ansaar . The short version: the model turned out to be the small part. What made it safe to run without me watching was everything around it. Three states, three features The model is a GaussianHMM from hmmlearn with three states. I tried more. The Bayesian information criterion kept picking three, and three is also the number a human can act on.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammed_arshadansari_f2/market-regime-detection-in-production-what-the-model-actually-changes-3i3i

## Related notes
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-07-02-an-al-writes-my-trading-code-three-gates-decide-if-it-ever-runs]]
- [[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-28-free-ai-compute-paid-review-queues-a-structured-debate-on-zero-dollar-sql-review]]
- [[2026-08-21-shipping-12-ios-apps-to-the-app-store-unattended-part-2-every-review-trap-beta-builds-rejected-pricing-name-collisions]]
