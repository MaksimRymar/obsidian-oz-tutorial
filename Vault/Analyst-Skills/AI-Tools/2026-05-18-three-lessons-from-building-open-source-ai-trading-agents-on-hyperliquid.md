---
title: Three lessons from building open-source AI trading agents on Hyperliquid
date: '2026-05-18'
source: https://dev.to/caelyn_moss/three-lessons-from-building-open-source-ai-trading-agents-on-hyperliquid-17k8
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
status: unread
---

> **TL;DR:** A few months ago, we shipped Moss, an open-source platform that lets you describe a trading strategy in plain language and deploy it as an autonomous agent on Hyperliquid in about 60 seconds. Since March, users have crea…

## What’s new and why it matters
A few months ago, we shipped Moss, an open-source platform that lets you describe a trading strategy in plain language and deploy it as an autonomous agent on Hyperliquid in about 60 seconds. Since March, users have created 1,700+ agents in the first month, and those agents have run real strategies producing $100M+ in trading volume. Last week we open-sourced the whole thing: github.com/moss-site/moss-trade-bot-skills. This post is about three lessons we didn't expect when we started. Not the marketing version — the actual engineering decisions we kept reversing because reality kept disagreein…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/caelyn_moss/three-lessons-from-building-open-source-ai-trading-agents-on-hyperliquid-17k8

## Related notes
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
