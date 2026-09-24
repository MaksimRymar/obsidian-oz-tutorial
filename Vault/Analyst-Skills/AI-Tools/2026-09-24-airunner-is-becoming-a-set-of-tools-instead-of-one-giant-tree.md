---
title: AIRunner is becoming a set of tools instead of one giant tree
date: '2026-09-24'
source: https://dev.to/w4ffl35/airunner-is-becoming-a-set-of-tools-instead-of-one-giant-tree-3k9b
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-09-14-smarter-python-configs-an-oop-framework]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-07-16-switch-ai-models-without-rewriting-your-openai-sdk-integration]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** I had let AIRunner , my open-source desktop AI application, do too much in one repository. The split is now visible in four public packages: airunner-eval , airunner-tts-vendor , airunner-native and airunner-common . The…

## What’s new and why it matters
I had let AIRunner , my open-source desktop AI application, do too much in one repository. The split is now visible in four public packages: airunner-eval , airunner-tts-vendor , airunner-native and airunner-common . The names describe the boundaries. The evaluation package can process models without dragging the application into the run. The TTS vendor fork can be tested and published without importing the host application's database. Native tools can stay close to their sidecar binaries. Shared request and response payloads can be versioned once and consumed by the desktop and service layers…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/w4ffl35/airunner-is-becoming-a-set-of-tools-instead-of-one-giant-tree-3k9b

## Related notes
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-09-14-smarter-python-configs-an-oop-framework]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-07-16-switch-ai-models-without-rewriting-your-openai-sdk-integration]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
