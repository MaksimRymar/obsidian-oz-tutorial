---
title: I rebuilt my Financial Mentor retrieval from scratch. Here's everything the
  RAG stack taught me
date: '2026-05-21'
source: https://dev.to/saulolinares10/i-rebuilt-my-financial-mentor-retrieval-from-scratch-heres-everything-the-rag-stack-taught-me-56cg
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-09-why-i-debug-my-rag-pipeline-stage-by-stage-not-end-to-end]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** From stuffing JSON into Claude to GraphRAG, hybrid search, CRAG, and adversarial evaluation — the complete honest account The problem with FinMentor started before I had the vocabulary to describe it... Users were asking…

## What’s new and why it matters
From stuffing JSON into Claude to GraphRAG, hybrid search, CRAG, and adversarial evaluation — the complete honest account The problem with FinMentor started before I had the vocabulary to describe it... Users were asking reasonable questions about their portfolios. The system was answering them. Some answers were right. Some answers were wrong. And I couldn't explain the pattern because I hadn't looked at what was actually flowing into the model. When I looked: every query was receiving the full IBKR portfolio snapshot. JSON format. Five positions, monthly P&L, thirty transactions, account met…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saulolinares10/i-rebuilt-my-financial-mentor-retrieval-from-scratch-heres-everything-the-rag-stack-taught-me-56cg

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-09-why-i-debug-my-rag-pipeline-stage-by-stage-not-end-to-end]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
