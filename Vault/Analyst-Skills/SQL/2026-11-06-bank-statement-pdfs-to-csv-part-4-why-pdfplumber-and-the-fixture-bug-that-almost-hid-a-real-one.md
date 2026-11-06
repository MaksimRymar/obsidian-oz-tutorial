---
title: 'Bank statement PDFs to CSV, part 4: why pdfplumber, and the fixture bug that
  almost hid a real one'
date: '2026-11-06'
source: https://dev.to/alapha888/bank-statement-pdfs-to-csv-part-4-why-pdfplumber-and-the-fixture-bug-that-almost-hid-a-real-one-2o6e
domain: SQL
relevance: 🔴
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Parts 1 to 3 of this series covered what the converter does: 34 rows across four statement layouts, all fields correct, then a GUI, a Windows installer, and the scanned-PDF path through OCR. This post is about a decision…

## What’s new and why it matters
Parts 1 to 3 of this series covered what the converter does: 34 rows across four statement layouts, all fields correct, then a GUI, a Windows installer, and the scanned-PDF path through OCR. This post is about a decision underneath all of that — which PDF library to build on — and about the test fixtures, which nearly hid a real problem instead of catching one. The choice: one runtime dependency The converter has exactly one runtime dependency: pdfplumber==0.11.10 . It was picked over PyMuPDF and pypdf for two concrete reasons. First, its line-based table extraction fits bank statements, which…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/alapha888/bank-statement-pdfs-to-csv-part-4-why-pdfplumber-and-the-fixture-bug-that-almost-hid-a-real-one-2o6e

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
