---
title: How We Translate Entire Books with LLMs Without Losing Context
date: '2026-09-23'
source: https://dev.to/jacob_gong/how-we-translate-entire-books-with-llms-without-losing-context-5chm
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-09-translating-300-page-books-with-claude-taming-token-limits-and-context-windows]]'
- '[[2026-09-05-translating-300-page-books-with-claude-taming-token-limits-and-chunking-strategies]]'
- '[[2026-09-12-translating-entire-books-with-llms-a-chunking-strategy-that-doesnt-lose-context]]'
- '[[2026-09-02-chunking-300-page-books-for-claude-how-we-beat-token-limits-in-ai-translation]]'
- '[[2026-07-01-how-we-translate-300-page-books-using-claude-without-hitting-token-limits]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** Chunking strategies, context carry-over, and glossary injection for long-form translation The Problem: Translating Books is Not Like Translating Tweets At LectuLibre, we translate entire books using LLMs like Claude and…

## What’s new and why it matters
Chunking strategies, context carry-over, and glossary injection for long-form translation The Problem: Translating Books is Not Like Translating Tweets At LectuLibre, we translate entire books using LLMs like Claude and DeepSeek. Early on, we discovered that feeding a whole book into the API wasn't just expensive—it was impossible. A 300-page novel can be 120,000 tokens, but even the best models max out at 200k context (and the quality degrades near the limit). So we had to chunk. Our first attempt was naive: split text into fixed-size chunks of 4,000 characters. The result? Sentences cut off…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jacob_gong/how-we-translate-entire-books-with-llms-without-losing-context-5chm

## Related notes
- [[2026-09-09-translating-300-page-books-with-claude-taming-token-limits-and-context-windows]]
- [[2026-09-05-translating-300-page-books-with-claude-taming-token-limits-and-chunking-strategies]]
- [[2026-09-12-translating-entire-books-with-llms-a-chunking-strategy-that-doesnt-lose-context]]
- [[2026-09-02-chunking-300-page-books-for-claude-how-we-beat-token-limits-in-ai-translation]]
- [[2026-07-01-how-we-translate-300-page-books-using-claude-without-hitting-token-limits]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
