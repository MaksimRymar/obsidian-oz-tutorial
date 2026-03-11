---
title: I built a CLI that finds dying files in your codebase
date: '2026-03-11'
source: https://dev.to/xarcho/i-built-a-cli-that-finds-dying-files-in-your-codebase-2mp5
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#tool'
related:
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
- '[[2026-02-28-how-to-track-what-billionaire-investors-are-buying-using-sec-edgar-data]]'
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
status: unread
---

> **TL;DR:** Every codebase has files that nobody owns. Files too complex to understand. Files last touched 3 years ago by someone who left. They never show up in sprint planning — but they cause the most bugs, the slowest onboarding…

## What’s new and why it matters
Every codebase has files that nobody owns. Files too complex to understand. Files last touched 3 years ago by someone who left. They never show up in sprint planning — but they cause the most bugs, the slowest onboarding, and the worst incidents. I built deathbed to make them visible. What it does Run it inside any git repo: pip install deathbed cd your-project deathbed You get a full file health report scored across 6 metrics: Size — lines of code Age — days since last commit touched this file Churn — how many times it's been modified Complexity — cyclomatic complexity via radon Authors — how…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/xarcho/i-built-a-cli-that-finds-dying-files-in-your-codebase-2mp5

## Related notes
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
- [[2026-02-28-how-to-track-what-billionaire-investors-are-buying-using-sec-edgar-data]]
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
