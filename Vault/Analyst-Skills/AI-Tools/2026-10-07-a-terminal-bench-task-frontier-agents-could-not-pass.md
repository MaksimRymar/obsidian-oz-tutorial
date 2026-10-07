---
title: A Terminal-Bench task frontier agents could not pass
date: '2026-10-07'
source: https://dev.to/amsozzer/a-terminal-bench-task-frontier-agents-could-not-pass-56jb
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
status: unread
---

> **TL;DR:** I wrote a task for Terminal-Bench, a public benchmark of hard command-line tasks for AI agents. The agent has to build a redactor for court-filing PDFs: black out every visible name and ID on a list, leave nothing recove…

## What’s new and why it matters
I wrote a task for Terminal-Bench, a public benchmark of hard command-line tasks for AI agents. The agent has to build a redactor for court-filing PDFs: black out every visible name and ID on a list, leave nothing recoverable in the file, and change nothing else on the page. I ran it three times each with Claude Opus 5.5 and GPT-6 Sol on their highest reasoning settings. All six runs failed, and so did two runs where the agent was told to cheat. Each agent wrote a tool of around 4,000 lines and tested it before stopping, and each one believed it had passed. This post is about how I built the t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/amsozzer/a-terminal-bench-task-frontier-agents-could-not-pass-56jb

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
