---
title: 5 JSON Schemas That Stop AI Coding Agents From Shipping Garbage
date: '2026-10-04'
source: https://dev.to/housharenet/5-json-schemas-that-stop-ai-coding-agents-from-shipping-garbage-25b4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
- '[[2026-03-23-your-production-agent-is-flying-blind-heres-the-fix]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]'
- '[[2026-05-05-tool-use-api-design-for-llms-5-patterns-that-prevent-agent-loops-and-silent-failures]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** Your agent said "done". Production disagreed. If you run autonomous coding agents (Cursor, Claude Code, Windsurf, custom loops), you have met the silent failure mode: the agent returns plausible output, the pipeline acce…

## What’s new and why it matters
Your agent said "done". Production disagreed. If you run autonomous coding agents (Cursor, Claude Code, Windsurf, custom loops), you have met the silent failure mode: the agent returns plausible output, the pipeline accepts it, and the breakage surfaces three steps downstream. The fix is not a smarter model. It is deterministic contracts at every handoff. Below are the 5 JSON Schemas I now require in every agent pipeline. 1. Task Handoff Schema Every task between agents carries: id , goal , inputs[] , acceptance_criteria[] , max_turns . If an agent cannot produce acceptance_criteria , it is no…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/housharenet/5-json-schemas-that-stop-ai-coding-agents-from-shipping-garbage-25b4

## Related notes
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
- [[2026-03-23-your-production-agent-is-flying-blind-heres-the-fix]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]
- [[2026-05-05-tool-use-api-design-for-llms-5-patterns-that-prevent-agent-loops-and-silent-failures]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
