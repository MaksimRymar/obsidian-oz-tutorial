---
title: 'Microsoft Agent Framework: From Agents to Workflows, Five Iterations of a
  DOCX-to-Markdown Pipeline'
date: '2026-04-26'
source: https://dev.to/rosidotidev/microsoft-agent-framework-from-agents-to-workflows-five-iterations-of-a-docx-to-markdown-pipeline-1l8p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
status: unread
---

> **TL;DR:** In my previous article , I built a multi-agent pipeline that reads a Markdown backlog and provisions Epics and Stories on Jira. That project used two agents collaborating sequentially, wired together with plain Python or…

## What’s new and why it matters
In my previous article , I built a multi-agent pipeline that reads a Markdown backlog and provisions Epics and Stories on Jira. That project used two agents collaborating sequentially, wired together with plain Python orchestration. This time I wanted to understand something specific: does the Microsoft Agent Framework (MFA) have a construct for defining execution graphs, similar to what LangGraph offers with its StateGraph or CrewAI with its Flow ? In other words, can you define nodes, edges, and let the framework handle execution order, state propagation, and event streaming? To find out, I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rosidotidev/microsoft-agent-framework-from-agents-to-workflows-five-iterations-of-a-docx-to-markdown-pipeline-1l8p

## Related notes
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
