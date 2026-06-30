---
title: Your database AI agent re-reads the whole catalog every step — that's the bill
date: '2026-06-30'
source: https://dev.to/saihmadmin/your-database-ai-agent-re-reads-the-whole-catalog-every-step-thats-the-bill-p9f
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]'
status: unread
---

> **TL;DR:** The AI agent that helps you tune queries feels cheap on a toy schema and expensive on a real warehouse. The reason is the same one that makes a long tuning session forget the index it suggested ten minutes ago — and it i…

## What’s new and why it matters
The AI agent that helps you tune queries feels cheap on a toy schema and expensive on a real warehouse. The reason is the same one that makes a long tuning session forget the index it suggested ten minutes ago — and it is fixable. Why each suggestion costs more than the last When an AI agent helps you run or tune a database, each step is a fresh call to the model. To reason well, that call carries the catalog with it: table definitions, indexes, constraints, and the query history it has seen so far. On a small schema that is cheap. On a warehouse with thousands of tables it is not — and every…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saihmadmin/your-database-ai-agent-re-reads-the-whole-catalog-every-step-thats-the-bill-p9f

## Related notes
- [[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]
