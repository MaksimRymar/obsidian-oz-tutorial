---
title: 'Local-first multi-hop RAG: Chroma + an entity graph, zero tokens per query'
date: '2026-08-05'
source: https://dev.to/demigoddsk/local-first-multi-hop-rag-chroma-an-entity-graph-zero-tokens-per-query-1l43
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#zendesk'
related:
- '[[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** Chroma's sweet spot is local-first: embed your documents, query them on your own machine, no infrastructure ceremony. But local-first RAG hits a wall on multi-hop questions: "Which university did the founder of the compa…

## What’s new and why it matters
Chroma's sweet spot is local-first: embed your documents, query them on your own machine, no infrastructure ceremony. But local-first RAG hits a wall on multi-hop questions: "Which university did the founder of the company that acquired Polar Metrics study at?" The answering passage shares almost no vocabulary with the question. It's connected to it — through an acquisition, a founder, a biography — and similarity search can't follow connections. The usual fix is to put an LLM in the retrieval loop to decompose the question, which breaks exactly what makes local-first attractive: now every que…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/demigoddsk/local-first-multi-hop-rag-chroma-an-entity-graph-zero-tokens-per-query-1l43

## Related notes
- [[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
