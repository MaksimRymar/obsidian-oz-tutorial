---
title: An Al writes my trading code. Three gates decide if it ever runs.
date: '2026-07-02'
source: https://dev.to/inalpha/an-al-writes-my-trading-code-three-gates-decide-if-it-ever-runs-58k5
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
status: unread
---

> **TL;DR:** A few months ago I built a system where an AI can write trading strategies — actual Python files — and then run them against real market data. The first thing it wrote was a simple moving-average crossover. Clean, reason…

## What’s new and why it matters
A few months ago I built a system where an AI can write trading strategies — actual Python files — and then run them against real market data. The first thing it wrote was a simple moving-average crossover. Clean, reasonable, made money in backtest. Cool. The second thing it wrote tried to import os . This post is about what happened next, and the three gates I built to make sure the answer is always "nice try, but no." Why let an AI write code in the first place? In two earlier posts I talked about keeping an AI away from the order book — making sure it can't place trades directly. Those were…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/inalpha/an-al-writes-my-trading-code-three-gates-decide-if-it-ever-runs-58k5

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
