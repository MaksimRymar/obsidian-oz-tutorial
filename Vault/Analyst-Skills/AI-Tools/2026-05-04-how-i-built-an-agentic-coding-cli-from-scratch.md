---
title: How I Built an Agentic Coding CLI from Scratch
date: '2026-05-04'
source: https://dev.to/vigp17/how-i-built-an-agentic-coding-cli-from-scratch-2ob5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
- '[[2026-04-12-i-built-a-fully-local-voice-ai-agent-heres-what-broke-and-how-i-fixed-it]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-12-building-ai-agents-is-hard-so-i-built-a-12-step-visual-guide-to-make-it-easy]]'
status: unread
---

> **TL;DR:** I wanted to understand how AI coding tools actually work under the hood. Not just use them — but build one myself. So I built AgentCode : an open-source, multi-model agentic coding CLI. You type a request in plain Englis…

## What’s new and why it matters
I wanted to understand how AI coding tools actually work under the hood. Not just use them — but build one myself. So I built AgentCode : an open-source, multi-model agentic coding CLI. You type a request in plain English, and it reads your codebase, writes code, runs tests, manages git — all autonomously. Here's what I learned building it. The Core Insight: It's Just a Loop Every agentic coding tool — no matter how polished — runs the same fundamental pattern: while needs_follow_up : 1. Send conversation + tools → LLM 2. If LLM returns tool calls → execute them , append results , loop 3. If L…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vigp17/how-i-built-an-agentic-coding-cli-from-scratch-2ob5

## Related notes
- [[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
- [[2026-04-12-i-built-a-fully-local-voice-ai-agent-heres-what-broke-and-how-i-fixed-it]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-12-building-ai-agents-is-hard-so-i-built-a-12-step-visual-guide-to-make-it-easy]]
