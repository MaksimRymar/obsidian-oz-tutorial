---
title: 'Reading PDFs with no extractable text from a glyph table: AI drafts it once,
  then every run is free and identical'
date: '2026-11-23'
source: https://dev.to/yasumorishima/reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-33ek
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-24-sql-the-monthly-revenue-report-in-five-lines-group-by-month-instead-of-a-spreadsheet-every-month-end]]'
status: unread
---

> **TL;DR:** When I analyze statistics as a hobby, the source numbers are often published only as PDFs from government offices: monthly reports that come out in the same layout every month. With a normal PDF, you can copy the numbers…

## What’s new and why it matters
When I analyze statistics as a hobby, the source numbers are often published only as PDFs from government offices: monthly reports that come out in the same layout every month. With a normal PDF, you can copy the numbers and paste them into a spreadsheet. But some PDFs read fine on screen and give you a string of symbols when you copy, or don't let you select any text at all. They look the same, but the inside is different. A normal PDF contains data saying "the character 'S' is here." A PDF with no extractable text only says "a shape made of these lines is here"; the PDF itself does not know…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yasumorishima/reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-33ek

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-24-sql-the-monthly-revenue-report-in-five-lines-group-by-month-instead-of-a-spreadsheet-every-month-end]]
