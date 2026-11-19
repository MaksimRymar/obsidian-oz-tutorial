---
title: 'Harnesses that improve themselves: how an agent can rewrite its own runtime
  without breaking it'
date: '2026-11-19'
source: https://dev.to/ahmad_dogar_7d098f5e48f72/harnesses-that-improve-themselves-how-an-agent-can-rewrite-its-own-runtime-without-breaking-it-1p2i
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-24-a-budget-guard-for-llm-agents-in-40-lines-of-python-written-by-an-agent-that-dies-at-0]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
status: unread
---

> **TL;DR:** If you run a coding agent for long enough, you end up maintaining two things: the model choice, and everything around it. The system prompt, the CLAUDE.md, the hooks, the tool wrappers, how much of a big file gets pasted…

## What’s new and why it matters
If you run a coding agent for long enough, you end up maintaining two things: the model choice, and everything around it. The system prompt, the CLAUDE.md, the hooks, the tool wrappers, how much of a big file gets pasted back into context, when the loop may stop. Most of my time on the second pile is reading a failed session, guessing what went wrong, and adding a line somewhere. A new paper argues that this pile is where most of the reliability lives, and that the guessing can be automated without the agent wrecking itself. It is Harnesses That Improve Themselves: A Unifying Framework for Sel…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ahmad_dogar_7d098f5e48f72/harnesses-that-improve-themselves-how-an-agent-can-rewrite-its-own-runtime-without-breaking-it-1p2i

## Related notes
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-24-a-budget-guard-for-llm-agents-in-40-lines-of-python-written-by-an-agent-that-dies-at-0]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
