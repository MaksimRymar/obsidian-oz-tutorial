---
title: 'Context budget optimization: how to design MCP tools that don''t waste tokens'
date: '2026-04-15'
source: https://dev.to/vdalhambra/context-budget-optimization-how-to-design-mcp-tools-that-dont-waste-tokens-3jcg
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-03-04-sqlite-as-an-mcp-context-saver-stop-cramming-raw-api-data-into-your-llm]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
status: unread
---

> **TL;DR:** Most MCP tools have a context budget problem nobody talks about. You call a tool. Claude gets back 4,000 tokens of raw JSON. It processes them, summarizes them, and the user gets a one-line answer. You just burned the eq…

## What’s new and why it matters
Most MCP tools have a context budget problem nobody talks about. You call a tool. Claude gets back 4,000 tokens of raw JSON. It processes them, summarizes them, and the user gets a one-line answer. You just burned the equivalent of 3 pages of reading for a sentence. I built this mistake into my first version of FinanceKit. Then I fixed it. Here's what I learned. The problem: raw data ≠ useful context A typical bad MCP tool response looks like this: { "symbol" : "AAPL" , "regularMarketPrice" : 213.49 , "regularMarketChange" : -1.23 , "regularMarketChangePercent" : -0.57 , "regularMarketVolume"…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vdalhambra/context-budget-optimization-how-to-design-mcp-tools-that-dont-waste-tokens-3jcg

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-03-04-sqlite-as-an-mcp-context-saver-stop-cramming-raw-api-data-into-your-llm]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
