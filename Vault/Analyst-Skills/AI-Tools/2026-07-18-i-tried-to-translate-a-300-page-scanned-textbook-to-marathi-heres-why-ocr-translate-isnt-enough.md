---
title: 'I Tried to Translate a 300-Page Scanned Textbook to Marathi: Here''s Why "OCR
  + Translate" Isn''t Enough'
date: '2026-07-18'
source: https://dev.to/adityanile/i-tried-to-translate-a-300-page-scanned-textbook-to-marathi-heres-why-ocr-translate-isnt-bb0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-01-how-we-translate-300-page-books-using-claude-without-hitting-token-limits]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-07-14-i-got-tired-of-renting-my-own-ai-so-i-built-one-i-actually-own]]'
status: unread
---

> **TL;DR:** I needed to convert a 300-page scanned English textbook into Marathi while keeping the original layout intact — headings, tables, the works. The "obvious" approach (OCR the pages, translate the text) works right up until…

## What’s new and why it matters
I needed to convert a 300-page scanned English textbook into Marathi while keeping the original layout intact — headings, tables, the works. The "obvious" approach (OCR the pages, translate the text) works right up until it doesn't: OCR throws away structure, and generic machine translation throws away meaning the moment your input has any noise in it. This post walks through the four architectures I evaluated, the one bug that killed my first real approach, and the pipeline I ended up shipping for under $5. Repo: github.com/adityanile/BookTranslationPipeline The problem Scanned English textbo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/adityanile/i-tried-to-translate-a-300-page-scanned-textbook-to-marathi-heres-why-ocr-translate-isnt-bb0

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-01-how-we-translate-300-page-books-using-claude-without-hitting-token-limits]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-07-14-i-got-tired-of-renting-my-own-ai-so-i-built-one-i-actually-own]]
