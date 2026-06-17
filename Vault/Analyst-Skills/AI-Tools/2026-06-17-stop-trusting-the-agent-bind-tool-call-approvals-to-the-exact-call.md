---
title: 'Stop trusting the agent: bind tool-call approvals to the exact call'
date: '2026-06-17'
source: https://dev.to/whatsonyourmind/stop-trusting-the-agent-bind-tool-call-approvals-to-the-exact-call-5080
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-06-12-why-your-ai-agent-logs-are-not-evidence-and-what-to-do-about-it]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-17-how-to-add-policy-enforcement-to-a-langgraph-agent-before-it-does-something-dumb]]'
- '[[2026-05-19-your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it]]'
status: unread
---

> **TL;DR:** Agentic systems gate dangerous tool calls — file writes, money movement, deploys — behind an "approval": a human-in-the-loop click, or a policy check. Look at how that approval is usually represented and you'll often fin…

## What’s new and why it matters
Agentic systems gate dangerous tool calls — file writes, money movement, deploys — behind an "approval": a human-in-the-loop click, or a policy check. Look at how that approval is usually represented and you'll often find a boolean sitting in the run/session state: approved: true . A boolean is the wrong primitive, and it fails in three ways that prompt injection is happy to exploit. Three ways an approval boolean breaks Flip. Anything that can write the run state — a serialized context crossing a process/durable-execution boundary, a confused-deputy code path, an injection that steers state —…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/whatsonyourmind/stop-trusting-the-agent-bind-tool-call-approvals-to-the-exact-call-5080

## Related notes
- [[2026-06-12-why-your-ai-agent-logs-are-not-evidence-and-what-to-do-about-it]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-17-how-to-add-policy-enforcement-to-a-langgraph-agent-before-it-does-something-dumb]]
- [[2026-05-19-your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it]]
