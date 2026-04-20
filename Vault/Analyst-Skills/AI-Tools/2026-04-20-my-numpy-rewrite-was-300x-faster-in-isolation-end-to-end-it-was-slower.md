---
title: My numpy rewrite was 300x faster in isolation. End-to-end it was slower.
date: '2026-04-20'
source: https://dev.to/yuvrajangadsingh/my-numpy-rewrite-was-300x-faster-in-isolation-end-to-end-it-was-slower-3o2l
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-17-the-quote-as-ceiling-billing-pattern]]'
- '[[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** my CLI search took 4.3 seconds for 5000 files. i swapped the python cosine loop for a numpy matmul. it got slower. short-lived python CLIs punish optimizing the wrong layer. this is what happened shipping vemb 0.3.0: wha…

## What’s new and why it matters
my CLI search took 4.3 seconds for 5000 files. i swapped the python cosine loop for a numpy matmul. it got slower. short-lived python CLIs punish optimizing the wrong layer. this is what happened shipping vemb 0.3.0: what i tried first that regressed performance, and what actually worked. the setup vemb is a CLI that wraps Gemini Embedding 2 for text, images, audio, video, and PDFs. vemb search ./files "query" embeds every file, caches the vectors, and returns the top matches by cosine similarity. the cache in 0.2.0 was JSON: { "version" : 1 , "model" : "gemini-embedding-2-preview" , "dim" : 3…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yuvrajangadsingh/my-numpy-rewrite-was-300x-faster-in-isolation-end-to-end-it-was-slower-3o2l

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-17-the-quote-as-ceiling-billing-pattern]]
- [[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
