---
title: What's eating your Claude Code context window? I wrote a 500-line Python script
  to find out
date: '2026-04-16'
source: https://dev.to/geniej/whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out-3oma
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-04-14-claude-api-prompt-caching-cut-costs-80-on-every-repeated-request]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** If you use Claude Code seriously — Max plan, 50+ skills, a CLAUDE.md that's grown organically over months — you've probably hit this moment: You run claude /context and it says your system prompt is sitting at 14% of you…

## What’s new and why it matters
If you use Claude Code seriously — Max plan, 50+ skills, a CLAUDE.md that's grown organically over months — you've probably hit this moment: You run claude /context and it says your system prompt is sitting at 14% of your context window before you've typed anything . And claude /cost tells you today's spend but doesn't say what inside your setup is expensive. Tokens are real money. You can't optimize what you can't see. So I wrote cc-healthcheck — a single Python file, zero dependencies, zero network, that reads ~/.claude/ locally and answers three questions: What auto-loads into every session…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/geniej/whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out-3oma

## Related notes
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-04-14-claude-api-prompt-caching-cut-costs-80-on-every-repeated-request]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
