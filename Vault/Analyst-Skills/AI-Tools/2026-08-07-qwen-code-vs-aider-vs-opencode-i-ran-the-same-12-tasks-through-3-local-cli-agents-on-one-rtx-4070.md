---
title: 'Qwen Code vs Aider vs OpenCode: I Ran the Same 12 Tasks Through 3 Local CLI
  Agents on One RTX 4070'
date: '2026-08-07'
source: https://dev.to/kenimo49/qwen-code-vs-aider-vs-opencode-i-ran-the-same-12-tasks-through-3-local-cli-agents-on-one-rtx-4070-378i
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]'
- '[[2026-05-04-how-i-built-an-agentic-coding-cli-from-scratch]]'
status: unread
---

> **TL;DR:** I pointed three coding CLIs at the same local model and ran twelve tasks through each one. The model was Qwen 35B, hosted on an RTX 4070 12GB via llama-server with --cpu-moe . The tasks were mundane: build a hello.py, ad…

## What’s new and why it matters
I pointed three coding CLIs at the same local model and ran twelve tasks through each one. The model was Qwen 35B, hosted on an RTX 4070 12GB via llama-server with --cpu-moe . The tasks were mundane: build a hello.py, add a CLI flag to an existing script, write a failing test then fix it, refactor a Python file to split a class into two. Nothing you would not do on a Tuesday. The results were not what I expected from reading each tool's README. The three tools, in one line each Aider : git-native pair-programming CLI (45k stars, Apache-2.0), most-used terminal option, mature and well-documente…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kenimo49/qwen-code-vs-aider-vs-opencode-i-ran-the-same-12-tasks-through-3-local-cli-agents-on-one-rtx-4070-378i

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]
- [[2026-05-04-how-i-built-an-agentic-coding-cli-from-scratch]]
