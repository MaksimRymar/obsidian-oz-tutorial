---
title: Why I Stopped Using LLMs to Schedule LLMs
date: '2026-04-08'
source: https://dev.to/alex_chernysh/why-i-stopped-using-llms-to-schedule-llms-4176
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-28-soul-engine]]'
status: unread
---

> **TL;DR:** Last year I had 10 open tickets, a week-long deadline, and three AI coding agents installed on my machine. Claude Code, Codex, Gemini CLI. Each one individually capable of knocking out a task in minutes. Together? Absolu…

## What’s new and why it matters
Last year I had 10 open tickets, a week-long deadline, and three AI coding agents installed on my machine. Claude Code, Codex, Gemini CLI. Each one individually capable of knocking out a task in minutes. Together? Absolute chaos. Agent A edits auth.py . Agent B edits auth.py . Agent A's changes get silently overwritten. Meanwhile, Agent C decides to "refactor" the test suite and breaks everything. Nobody runs the linter. Nobody checks types. I spend more time mediating conflicts than I would have just writing the code myself. So I built an orchestrator. And the single most important design dec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/alex_chernysh/why-i-stopped-using-llms-to-schedule-llms-4176

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-28-soul-engine]]
