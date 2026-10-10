---
title: 'Visual Grounding for AI Agents: Set-of-Mark Prompting and Reliable UI Clicks'
date: '2026-10-10'
source: https://dev.to/nughes/visual-grounding-for-ai-agents-set-of-mark-prompting-and-reliable-ui-clicks-4n7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** Ask a frontier vision model for the pixel coordinates of a "Submit" button in a 1920x1080 screenshot and it will often miss by dozens of pixels. That miss is the difference between an agent that completes a checkout flow…

## What’s new and why it matters
Ask a frontier vision model for the pixel coordinates of a "Submit" button in a 1920x1080 screenshot and it will often miss by dozens of pixels. That miss is the difference between an agent that completes a checkout flow and one that clicks empty whitespace and loops until it hits a timeout. The fix is not a bigger model. It is a better interface between the model and the screen. That interface has two parts. Screen painting draws numbered marks onto the screenshot before the model sees it. Visual grounding maps the model's answer back to a real, clickable element. Together they turn a coordin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nughes/visual-grounding-for-ai-agents-set-of-mark-prompting-and-reliable-ui-clicks-4n7

## Related notes
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
