---
title: We renamed two MCP tools and our agent's tool-call accuracy went from 71% to
  94%
date: '2026-05-26'
source: https://dev.to/james_oconnor_dev/we-renamed-two-mcp-tools-and-our-agents-tool-call-accuracy-went-from-71-to-94-3e47
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-23-on-static-analysis-llm]]'
status: unread
---

> **TL;DR:** Three months ago our customer-service agent confidently issued a $2,400 accounting reversal that should have been a $240 partial refund. The customer had asked for "a refund on the broken item." The agent had two tools a…

## What’s new and why it matters
Three months ago our customer-service agent confidently issued a $2,400 accounting reversal that should have been a $240 partial refund. The customer had asked for "a refund on the broken item." The agent had two tools available: refund and cancel. It picked cancel. The cancel tool, in our system, performed a full transaction reversal in the accounting ledger. The agent was technically correct. "Cancel" can mean "undo," which can mean "reverse." The customer was furious. The CFO was annoyed. For three weeks I tried to fix this with prompt engineering. None of it stuck. Tool-call accuracy on ou…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/james_oconnor_dev/we-renamed-two-mcp-tools-and-our-agents-tool-call-accuracy-went-from-71-to-94-3e47

## Related notes
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-23-on-static-analysis-llm]]
