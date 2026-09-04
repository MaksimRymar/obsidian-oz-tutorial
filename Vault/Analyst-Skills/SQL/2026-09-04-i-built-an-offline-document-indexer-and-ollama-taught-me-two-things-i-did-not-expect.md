---
title: I built an offline document indexer, and Ollama taught me two things I did
  not expect
date: '2026-09-04'
source: https://dev.to/alexccastilho/i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect-4ho5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
status: unread
---

> **TL;DR:** I had a folder with a few hundred scanned documents I could not upload anywhere. Confidential, mostly images of paper with no text layer, useless for search. Opening them one by one was the only way to find anything. So…

## What’s new and why it matters
I had a folder with a few hundred scanned documents I could not upload anywhere. Confidential, mostly images of paper with no text layer, useless for search. Opening them one by one was the only way to find anything. So I built the step that comes before the AI assistant, rather than trying to replace it. What it does You point it at a folder. It scans, runs OCR only on the pages that have no text layer (it checks per file and skips the rest), slices oversized PDFs, reads every page, and classifies each one into an item with a type, a date where one exists, an author and a summary. Then it wri…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alexccastilho/i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect-4ho5

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
