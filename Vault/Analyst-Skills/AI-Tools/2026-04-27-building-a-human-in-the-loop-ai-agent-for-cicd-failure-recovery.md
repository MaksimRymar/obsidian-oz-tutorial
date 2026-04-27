---
title: Building a human-in-the-loop AI agent for CI/CD failure recovery
date: '2026-04-27'
source: https://dev.to/adil-khan-723/building-a-human-in-the-loop-ai-agent-for-cicd-failure-recovery-15pd
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-03-your-ai-agent-just-deleted-something-it-shouldnt-have-heres-how-to-prevent-it]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
status: unread
---

> **TL;DR:** My pipelines break every week. Usually Docker cache issues, sometimes a pip dependency conflict, occasionally a missing credential that someone rotated and forgot to update. Each one takes 20-40 minutes to diagnose. Most…

## What’s new and why it matters
My pipelines break every week. Usually Docker cache issues, sometimes a pip dependency conflict, occasionally a missing credential that someone rotated and forgot to update. Each one takes 20-40 minutes to diagnose. Most of that time is spent opening logs, figuring out which stage failed, cross-checking job config, then deciding what to actually fix. I built a tool that does most of that for me. It watches Jenkins, finds the failure, runs deterministic checks before touching any LLM, posts the analysis to a web UI, and waits for me to click a button before doing anything. Here's what actually…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/adil-khan-723/building-a-human-in-the-loop-ai-agent-for-cicd-failure-recovery-15pd

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-03-your-ai-agent-just-deleted-something-it-shouldnt-have-heres-how-to-prevent-it]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
