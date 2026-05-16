---
title: Stop reinventing 'ask GPT-4 and Claude and a regex, then count the votes'
date: '2026-05-16'
source: https://dev.to/lfzds4399cpu/stop-reinventing-ask-gpt-4-and-claude-and-a-regex-then-count-the-votes-5fkd
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
- '[[2026-04-21-is-chatgpt-citing-your-site-a-conceptual-guide-to-geo-tracking-in-python-published]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-03-stop-switching-between-chatgpt-claude-and-gemini-i-automated-it]]'
status: unread
---

> **TL;DR:** If you've ever wired up "ask GPT-4 and Claude and a regex, then count the votes" inside a moderation pipeline, an agent router, or a code-review bot — you've written this code before: gpt_ok = call_gpt ( prompt ) claude_…

## What’s new and why it matters
If you've ever wired up "ask GPT-4 and Claude and a regex, then count the votes" inside a moderation pipeline, an agent router, or a code-review bot — you've written this code before: gpt_ok = call_gpt ( prompt ) claude_ok = call_claude ( prompt ) regex_ok = not contains_blocklist ( prompt ) if ( gpt_ok and claude_ok ) or ( gpt_ok and regex_ok ): return APPROVE else : return REJECT Then someone asks "what about weighting the senior model 2x?" and the if-tree doubles. Then "what if regex sees a hard policy violation — that should veto everything?" and you bolt on another branch. Then the audit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lfzds4399cpu/stop-reinventing-ask-gpt-4-and-claude-and-a-regex-then-count-the-votes-5fkd

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
- [[2026-04-21-is-chatgpt-citing-your-site-a-conceptual-guide-to-geo-tracking-in-python-published]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-03-stop-switching-between-chatgpt-claude-and-gemini-i-automated-it]]
