---
title: How I Built a Drone-Based Crack Detection Pipeline on AWS
date: '2026-05-19'
source: https://dev.to/robertobelotti/how-i-built-a-drone-based-crack-detection-pipeline-on-aws-18i7
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-29-how-to-extract-data-from-invoices-with-python-3-lines-of-code]]'
status: unread
---

> **TL;DR:** I needed to build a pipeline that takes drone footage of infrastructure (bridges, facades, roads), detects surface defects like cracks and corrosion, and delivers actionable reports to engineers who don't care about ML.…

## What’s new and why it matters
I needed to build a pipeline that takes drone footage of infrastructure (bridges, facades, roads), detects surface defects like cracks and corrosion, and delivers actionable reports to engineers who don't care about ML. Sounds straightforward. It wasn't. This article walks through the architecture decisions, the Python code that ties it all together, and the lessons I learned about what happens when computer vision meets real-world AWS constraints. The problem (and why it's not a model problem) Let me be clear upfront: this project is not about training a state-of-the-art detection model. YOLO…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/robertobelotti/how-i-built-a-drone-based-crack-detection-pipeline-on-aws-18i7

## Related notes
- [[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-29-how-to-extract-data-from-invoices-with-python-3-lines-of-code]]
