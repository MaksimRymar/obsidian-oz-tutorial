---
title: From Prompt to Graph Engineering, Explained With One Bug
date: '2026-09-19'
source: https://dev.to/miruky/from-prompt-to-graph-engineering-explained-with-one-bug-18mb
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-11-migration-diary-extract-loop-stop-conditions-before-you-leave-a-paid-coding-agent]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
- '[[2026-09-17-project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents]]'
status: unread
---

> **TL;DR:** Introduction Hi, I'm miruky. A timeout parser turns 250ms into 250.0 seconds. The intended value is 0.25 . The function fits in three lines. Completing the change means specifying accepted input, executing tests, handlin…

## What’s new and why it matters
Introduction Hi, I'm miruky. A timeout parser turns 250ms into 250.0 seconds. The intended value is 0.25 . The function fits in three lines. Completing the change means specifying accepted input, executing tests, handling failed repairs, and confirming which source the reviewer approved. The same bug gives us a concrete way to compare prompt, context, harness, loop, and graph engineering. Each stage changes what we ask the model to do, what information it receives, or how the surrounding program handles its work. The prompts below follow that repair from a chat request to a workflow with tests…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/miruky/from-prompt-to-graph-engineering-explained-with-one-bug-18mb

## Related notes
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-11-migration-diary-extract-loop-stop-conditions-before-you-leave-a-paid-coding-agent]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
- [[2026-09-17-project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents]]
