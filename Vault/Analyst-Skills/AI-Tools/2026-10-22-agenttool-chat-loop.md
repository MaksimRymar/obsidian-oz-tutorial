---
title: 从零手写 Agent（一）：Tool 把我从 Chat 拽进了 Loop
date: '2026-10-22'
source: https://dev.to/zealot2002/cong-ling-shou-xie-agent-tool-ba-wo-cong-chat-zhuai-jin-liao-loop-27p2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-07-10-top-10-python-concepts-for-freshers]]'
- '[[2026-06-09-claude-tool-use-complete-guide-to-function-calling]]'
- '[[2026-05-04-day-3-prompting-techniques-in-ai-part-1]]'
- '[[2026-05-10-from-pydantic-model-to-ai-agent-in-10-lines-of-python]]'
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-04-21-authentication-vs-authorization-rbac-and-timing-attacks-2026]]'
status: unread
---

> **TL;DR:** 我学 Agent 时刻意没先上 LangGraph，而是在本地用 Ollama 写了一个最小的 Calculator Agent ：一个 calculator 、一个 while 、OpenAI 兼容的 Tool Calling。 写完、跑通、又测几轮之后，我发现： 搞懂 Tool，比搞懂某个框架的类名重要得多 ——Chat 和 Agent 的分水岭就在这里。 这篇只记录这一路 学到了什么、困惑过什么、日志里暴露了什么问题 。代码在文末…

## What’s new and why it matters
我学 Agent 时刻意没先上 LangGraph，而是在本地用 Ollama 写了一个最小的 Calculator Agent ：一个 calculator 、一个 while 、OpenAI 兼容的 Tool Calling。 写完、跑通、又测几轮之后，我发现： 搞懂 Tool，比搞懂某个框架的类名重要得多 ——Chat 和 Agent 的分水岭就在这里。 这篇只记录这一路 学到了什么、困惑过什么、日志里暴露了什么问题 。代码在文末仓库。 1. 动手之前，我以为 Agent 是「更长的 Prompt」 普通 Chat 是 User → LLM → Answer 。 我原来以为 Agent 无非是 Prompt 里多写几句「你可以使用工具……」 真正跑起来以后，轨迹变成： User → LLM →（可能）Tool → Observation → LLM → … → Answer Agent ≈ LLM + Tools + Loop + State ——这句话在写 Calculator 之前像口号；看到 tool_calls 和 role: tool 在 messages 里来回之后，才变成直觉。 Loop 的核心伪代码可以极短（仓库 agent/loop.py 与之一一对应）： while step < MAX_STEPS : response = llm ( messages…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zealot2002/cong-ling-shou-xie-agent-tool-ba-wo-cong-chat-zhuai-jin-liao-loop-27p2

## Related notes
- [[2026-07-10-top-10-python-concepts-for-freshers]]
- [[2026-06-09-claude-tool-use-complete-guide-to-function-calling]]
- [[2026-05-04-day-3-prompting-techniques-in-ai-part-1]]
- [[2026-05-10-from-pydantic-model-to-ai-agent-in-10-lines-of-python]]
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-04-21-authentication-vs-authorization-rbac-and-timing-attacks-2026]]
