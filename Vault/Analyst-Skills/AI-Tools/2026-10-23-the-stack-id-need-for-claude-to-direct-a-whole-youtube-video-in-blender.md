---
title: The Stack I'd Need for Claude to Direct a Whole YouTube Video in Blender
date: '2026-10-23'
source: https://dev.to/gu_cci_f94bedb90083e6aab4/the-stack-id-need-for-claude-to-direct-a-whole-youtube-video-in-blender-3fnn
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-12-structured-summary-json-schema-for-a-fintech-llm-code-review-api]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-06-13-adding-hard-per-agent-spending-limits-to-langchain-and-crewai-agents]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]'
status: unread
---

> **TL;DR:** Introduction I've been experimenting with LLM agents that control Blender. The goal: have Claude generate a complete YouTube video—script, 3D scenes, animations, camera moves, and render—without human intervention. The r…

## What’s new and why it matters
Introduction I've been experimenting with LLM agents that control Blender. The goal: have Claude generate a complete YouTube video—script, 3D scenes, animations, camera moves, and render—without human intervention. The result is a stack of Python components that bridge natural language to Blender's Python API. This post outlines the architecture, the code, and the hard limits I hit. Problem Blender is a GUI application with a massive Python API ( bpy ). An LLM can emit Python code, but directly executing it is dangerous and brittle. You need: Safety : Arbitrary code execution can delete files…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gu_cci_f94bedb90083e6aab4/the-stack-id-need-for-claude-to-direct-a-whole-youtube-video-in-blender-3fnn

## Related notes
- [[2026-08-12-structured-summary-json-schema-for-a-fintech-llm-code-review-api]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-06-13-adding-hard-per-agent-spending-limits-to-langchain-and-crewai-agents]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]
