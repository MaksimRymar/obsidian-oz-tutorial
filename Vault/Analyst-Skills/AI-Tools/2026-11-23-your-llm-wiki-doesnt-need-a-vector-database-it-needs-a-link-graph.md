---
title: Your LLM Wiki Doesn't Need a Vector Database. It Needs a Link Graph.
date: '2026-11-23'
source: https://dev.to/affineofficial/your-llm-wiki-doesnt-need-a-vector-database-it-needs-a-link-graph-di2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#tool'
related:
- '[[2026-11-20-your-llm-wiki-remembers-facts-teach-it-how-you-work-too]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-11-10-oracle-developer-tools-one-workspace-for-sql-diagrams-and-charts]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
status: unread
---

> **TL;DR:** Most LLM wiki setups I see pick up a vector database on day two. I understand why. Karpathy's LLM Wiki pattern — raw sources stay untouched, the model maintains linked Markdown pages, answers come back with citations — s…

## What’s new and why it matters
Most LLM wiki setups I see pick up a vector database on day two. I understand why. Karpathy's LLM Wiki pattern — raw sources stay untouched, the model maintains linked Markdown pages, answers come back with citations — sounds like a retrieval problem, and retrieval has meant embeddings for a few years now. So people chunk the wiki, embed the chunks, and ask an index to find "similar" passages. This week's feed was doing something older, and it worked well enough that I wanted a version I could unit-test. An Obsidian plugin for Karpathy's LLM Wiki was being passed around that uses lexical searc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/affineofficial/your-llm-wiki-doesnt-need-a-vector-database-it-needs-a-link-graph-di2

## Related notes
- [[2026-11-20-your-llm-wiki-remembers-facts-teach-it-how-you-work-too]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-11-10-oracle-developer-tools-one-workspace-for-sql-diagrams-and-charts]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
