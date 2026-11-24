---
title: Every misread word had OCR confidence above 0.95. A second engine caught all
  three.
date: '2026-11-23'
source: https://dev.to/atraining/every-misread-word-had-ocr-confidence-above-095-a-second-engine-caught-all-three-57jk
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]'
status: unread
---

> **TL;DR:** If you feed PDFs to an agent or a RAG pipeline, the question you need answered for every word is whether it could be wrong. OCR confidence does not answer it. On our test pages it was highest exactly where the text was w…

## What’s new and why it matters
If you feed PDFs to an agent or a RAG pipeline, the question you need answered for every word is whether it could be wrong. OCR confidence does not answer it. On our test pages it was highest exactly where the text was wrong. What did answer it: two OCR engines that fail in opposite ways, and a list of the words where they disagree. We measured this on our own OCR service (ocr-software.com) with a public 42-page earnings call transcript (Schaeffler Q3 2026, original PDF , retrieved 13 November 2026; the text is theirs, so we quote single words only) and 300 further public pages. 15 pages of th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/atraining/every-misread-word-had-ocr-confidence-above-095-a-second-engine-caught-all-three-57jk

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]
