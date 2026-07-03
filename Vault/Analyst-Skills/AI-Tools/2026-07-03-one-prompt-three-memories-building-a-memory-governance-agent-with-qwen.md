---
title: 'One prompt, three memories: building a memory-governance agent with Qwen'
date: '2026-07-03'
source: https://dev.to/ghostyai_aionexo/one-prompt-three-memories-building-a-memory-governance-agent-with-qwen-2pal
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]'
- '[[2026-04-07-i-turned-notion-into-a-shared-brain-for-ai-agents-and-it-actually-made-sense]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** I gave the same caregiver prompt to my app three times and got three very different answers. "What's the plan for tomorrow's clinic visit?" Answer 1 — No Memory. Safe, and useless. It can't tell me the appointment time,…

## What’s new and why it matters
I gave the same caregiver prompt to my app three times and got three very different answers. "What's the plan for tomorrow's clinic visit?" Answer 1 — No Memory. Safe, and useless. It can't tell me the appointment time, who's driving, or what to bring, because it knows nothing about this family. Answer 2 — Raw Memory. Detailed, and unsafe. I dumped every stored note into the prompt, so the model happily surfaced a routine we dropped weeks ago, let contradictions slip through, and echoed a private insurance ID straight into the reply. Answer 3 — ERINYS + Qwen. Detailed and safe. Only governed c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ghostyai_aionexo/one-prompt-three-memories-building-a-memory-governance-agent-with-qwen-2pal

## Related notes
- [[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]
- [[2026-04-07-i-turned-notion-into-a-shared-brain-for-ai-agents-and-it-actually-made-sense]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
