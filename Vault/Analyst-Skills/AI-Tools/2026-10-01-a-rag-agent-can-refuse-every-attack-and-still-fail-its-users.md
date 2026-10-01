---
title: A RAG Agent Can Refuse Every Attack and Still Fail Its Users
date: '2026-10-01'
source: https://dev.to/lingikaushikreddy/a-rag-agent-can-refuse-every-attack-and-still-fail-its-users-3fe0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]'
- '[[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]'
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
- '[[2026-07-23-the-3-user-personas-that-determine-the-success-of-an-enterprise-data-platform]]'
status: unread
---

> **TL;DR:** Suppose an agent refuses every request. Its attack success rate might look excellent. Its usefulness would be terrible. That tradeoff is a central design concern in AegisEval , my adversarial evaluation project for a too…

## What’s new and why it matters
Suppose an agent refuses every request. Its attack success rate might look excellent. Its usefulness would be terrible. That tradeoff is a central design concern in AegisEval , my adversarial evaluation project for a tool-using customer-support RAG agent. Status first: the evaluation machinery is implemented, but no evaluation run has been recorded yet. This post describes the design, not measured safety improvements. Evaluate actions, not just answers The fictional retailer's chatbot retrieves help-centre content and has tools for refunds, cancellations and shipping-address changes. That crea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lingikaushikreddy/a-rag-agent-can-refuse-every-attack-and-still-fail-its-users-3fe0

## Related notes
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]
- [[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
- [[2026-07-23-the-3-user-personas-that-determine-the-success-of-an-enterprise-data-platform]]
