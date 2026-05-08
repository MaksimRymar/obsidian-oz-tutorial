---
title: 'From -9.15pp to +0.61pp: An engineering journey through four DPO iteration
  failures'
date: '2026-05-08'
source: https://dev.to/namakoo/from-915pp-to-061pp-an-engineering-journey-through-four-dpo-iteration-failures-5doi
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
status: unread
---

> **TL;DR:** Over 36 hours we ran four DPO training iterations against Qwen2.5-Coder-7B-Instruct, trying to push HumanEval pass@1 above the base model's 87.20%. The first three iterations failed in different ways (-9.15pp, -1.22pp, t…

## What’s new and why it matters
Over 36 hours we ran four DPO training iterations against Qwen2.5-Coder-7B-Instruct, trying to push HumanEval pass@1 above the base model's 87.20%. The first three iterations failed in different ways (-9.15pp, -1.22pp, two NO-GO calls). The fourth recovered to +0.61pp. Each failure revealed a different class of bug in our chosen-sample generation pipeline — bugs the existing certification gates were not catching. This post walks through the four iterations and what we ended up building to fix them. We're sharing this because the same gate-blindness probably affects most teams running DPO on au…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/namakoo/from-915pp-to-061pp-an-engineering-journey-through-four-dpo-iteration-failures-5doi

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
