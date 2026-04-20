---
title: I Tracked Every LLM API Call For a Week — 65% Were Unnecessary
date: '2026-04-20'
source: https://dev.to/noahbatish/i-tracked-every-llm-api-call-for-a-week-65-were-unnecessary-5h9f
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-04-16-whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out]]'
- '[[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
- '[[2026-04-03-stop-switching-between-chatgpt-claude-and-gemini-i-automated-it]]'
status: unread
---

> **TL;DR:** I've been using GPT-5 and Claude via API for coding tasks — refactoring, code review, architecture questions, debugging. The bill was creeping past $150/month and I had no idea which calls were actually worth the money.…

## What’s new and why it matters
I've been using GPT-5 and Claude via API for coding tasks — refactoring, code review, architecture questions, debugging. The bill was creeping past $150/month and I had no idea which calls were actually worth the money. Provider dashboards show you totals. Tokens used, dollars spent, done. But they don't tell you which specific calls were unnecessary. Was that $2.80 request for "where is the auth middleware" really worth sending to GPT-4o? So I built a tracker to find out. The experiment I wrote a small Python library called llm-costlog that wraps around any LLM API call and records: Tokens us…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/noahbatish/i-tracked-every-llm-api-call-for-a-week-65-were-unnecessary-5h9f

## Related notes
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-04-16-whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out]]
- [[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
- [[2026-04-03-stop-switching-between-chatgpt-claude-and-gemini-i-automated-it]]
