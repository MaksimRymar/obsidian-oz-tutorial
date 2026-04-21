---
title: Why Tokens Per Joule Matters More Than Tokens Per Second
date: '2026-04-21'
source: https://dev.to/dilberx/why-tokens-per-joule-matters-more-than-tokens-per-second-1o06
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-04-07-the-missing-infrastructure-for-agent-commerce]]'
status: unread
---

> **TL;DR:** Most GPU benchmarks report tokens/sec, but that metric ignores the dominant driver of real-world inference cost: energy. I built a cross-platform telemetry suite to measure Tokens Per Joule (T/J) — tokens/sec ÷ watts — a…

## What’s new and why it matters
Most GPU benchmarks report tokens/sec, but that metric ignores the dominant driver of real-world inference cost: energy. I built a cross-platform telemetry suite to measure Tokens Per Joule (T/J) — tokens/sec ÷ watts — alongside throughput. Think of it as miles per gallon for inference. The reference data across Apple Silicon and NVIDIA challenges some common assumptions about hardware selection. TL;DR Metric: Tokens Per Joule (T/J) = tokens/sec ÷ watts. The inference equivalent of miles per gallon. Finding: Apple M1 Pro achieves 2.42 T/J vs NVIDIA RTX 3080 at 0.90 T/J — a 2.7× energy efficien…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dilberx/why-tokens-per-joule-matters-more-than-tokens-per-second-1o06

## Related notes
- [[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-04-07-the-missing-infrastructure-for-agent-commerce]]
