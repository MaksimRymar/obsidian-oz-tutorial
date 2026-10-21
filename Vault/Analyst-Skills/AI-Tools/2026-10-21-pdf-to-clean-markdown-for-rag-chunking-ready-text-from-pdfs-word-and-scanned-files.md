---
title: 'PDF to clean Markdown for RAG: chunking-ready text from PDFs, Word and scanned
  files'
date: '2026-10-21'
source: https://dev.to/fast_data_asap/pdf-to-clean-markdown-for-rag-chunking-ready-text-from-pdfs-word-and-scanned-files-3im3
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-07-liteparse-a-fast-local-document-parser-for-developers]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** Most RAG quality problems I have debugged were not embedding or prompt problems. They were extraction problems: a table flattened into a soup of numbers, a heading glued to the paragraph above it, a scanned appendix that…

## What’s new and why it matters
Most RAG quality problems I have debugged were not embedding or prompt problems. They were extraction problems: a table flattened into a soup of numbers, a heading glued to the paragraph above it, a scanned appendix that came back empty, so the retriever never had a chance. This post walks through turning PDFs, Word files and scans into Markdown that is ready to chunk, with a real test run and the actual output, warts included. Disclosure: I built the Apify actor used below ( Document to Markdown ). I also list the free DIY options, which are the right choice in plenty of cases. Why Markdown a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fast_data_asap/pdf-to-clean-markdown-for-rag-chunking-ready-text-from-pdfs-word-and-scanned-files-3im3

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-07-liteparse-a-fast-local-document-parser-for-developers]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
