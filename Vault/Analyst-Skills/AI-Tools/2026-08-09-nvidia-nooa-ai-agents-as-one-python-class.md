---
title: 'NVIDIA NOOA: AI Agents as One Python Class'
date: '2026-08-09'
source: https://dev.to/truongandev/nvidia-nooa-ai-agents-as-one-python-class-288c
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
status: unread
---

> **TL;DR:** NVIDIA NOOA is an open-source, model-agnostic Python framework from NVIDIA Labs that collapses an entire AI agent into a single Python class: methods become the actions the model can take, fields hold agent state, docstr…

## What’s new and why it matters
NVIDIA NOOA is an open-source, model-agnostic Python framework from NVIDIA Labs that collapses an entire AI agent into a single Python class: methods become the actions the model can take, fields hold agent state, docstrings are the prompts, and type annotations are contracts the runtime enforces. A 253-line agent built this way scores 82.2% on SWE-bench Verified with GPT-5.5 at xhigh effort — ahead of OpenCode at 78.6% and PI at 78.2%. It ships under Apache 2.0 as NVIDIA-NeMo/labs-OO-Agents . The trick that makes it work is almost rude in its simplicity. Write a method body as ... and the run…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/truongandev/nvidia-nooa-ai-agents-as-one-python-class-288c

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
