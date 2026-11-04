---
title: 'A faster Tesseract alternative: OCR PDFs to markdown on CPU with Indra OCR'
date: '2026-11-04'
source: https://dev.to/dedupedai/a-faster-tesseract-alternative-ocr-pdfs-to-markdown-on-cpu-with-indra-ocr-568c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-06-07-liteparse-a-fast-local-document-parser-for-developers]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
status: unread
---

> **TL;DR:** Tesseract is still the default OCR engine in a lot of pipelines, mostly because it is free, local and needs no GPU. Indra OCR from Datalab keeps all three of those properties and adds layout, reading order and handwritin…

## What’s new and why it matters
Tesseract is still the default OCR engine in a lot of pipelines, mostly because it is free, local and needs no GPU. Indra OCR from Datalab keeps all three of those properties and adds layout, reading order and handwriting. This post shows how to install it, convert PDFs to markdown or JSON, and use it from Python. datalab-to/indra describes Indra OCR as a 1M-parameter OCR model that runs on CPU. It turns PDFs and images into markdown, text, or JSON with boxes, and reads handwriting, 80+ languages and pages at any angle. It runs on ONNX Runtime, with no PyTorch and no GPU. The numbers from the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dedupedai/a-faster-tesseract-alternative-ocr-pdfs-to-markdown-on-cpu-with-indra-ocr-568c

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-06-07-liteparse-a-fast-local-document-parser-for-developers]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
