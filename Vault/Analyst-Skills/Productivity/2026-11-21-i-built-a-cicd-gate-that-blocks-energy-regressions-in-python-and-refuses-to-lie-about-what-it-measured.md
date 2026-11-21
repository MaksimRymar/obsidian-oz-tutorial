---
title: I built a CI/CD gate that blocks energy regressions in Python — and refuses
  to lie about what it measured
date: '2026-11-21'
source: https://dev.to/babarustyhz/i-built-a-cicd-gate-that-blocks-energy-regressions-in-python-and-refuses-to-lie-about-what-it-2635
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-07-i-shipped-12-bi-dashboards-with-5-different-tools-here-is-the-honest-comparison]]'
- '[[2026-04-16-i-used-python-and-claude-to-write-validate-and-publish-a-bilingual-ebook-full-cost-timeline-and-output]]'
- '[[2026-10-20-marimo-vs-jupyter-reactive-notebooks-for-data-work]]'
- '[[2026-11-02-trimming-container-bloat-with-docker-history-and-dive]]'
- '[[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]'
- '[[2026-11-02-5-rules-we-used-to-turn-164963-daily-follower-readings-into-one-honest-growth-number]]'
status: unread
---

> **TL;DR:** **dol8 **is a CI/CD energy regression gate for Python. It blocks pull requests that increase CPU energy consumption by reading real RAPL Joules on bare-metal Linux, with honest fallbacks to perf counters on VMs and CPU t…

## What’s new and why it matters
**dol8 **is a CI/CD energy regression gate for Python. It blocks pull requests that increase CPU energy consumption by reading real RAPL Joules on bare-metal Linux, with honest fallbacks to perf counters on VMs and CPU time on Windows. The core is written in Rust (via PyO3) so the measurement does not contaminate itself, with Python handling statistics and orchestration. The differentiator is the honesty layer: every output is tagged with its measurement source and confidence level, the gate refuses to hard-fail CI on noisy data, and cross-tier comparisons (Joules vs CPU-seconds) are blocked b…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/babarustyhz/i-built-a-cicd-gate-that-blocks-energy-regressions-in-python-and-refuses-to-lie-about-what-it-2635

## Related notes
- [[2026-06-07-i-shipped-12-bi-dashboards-with-5-different-tools-here-is-the-honest-comparison]]
- [[2026-04-16-i-used-python-and-claude-to-write-validate-and-publish-a-bilingual-ebook-full-cost-timeline-and-output]]
- [[2026-10-20-marimo-vs-jupyter-reactive-notebooks-for-data-work]]
- [[2026-11-02-trimming-container-bloat-with-docker-history-and-dive]]
- [[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]
- [[2026-11-02-5-rules-we-used-to-turn-164963-daily-follower-readings-into-one-honest-growth-number]]
