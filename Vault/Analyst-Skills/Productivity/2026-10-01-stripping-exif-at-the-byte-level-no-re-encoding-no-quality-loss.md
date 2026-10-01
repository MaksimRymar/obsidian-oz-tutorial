---
title: '"Stripping EXIF at the byte level: no re-encoding, no quality loss"'
date: '2026-10-01'
source: https://dev.to/danyblitz/stripping-exif-at-the-byte-level-no-re-encoding-no-quality-loss-5bpo
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-09-02-i-generate-every-blog-cover-with-headless-chrome-and-a-bit-of-css-no-design-tool]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-31-how-i-made-sql-run-inside-a-single-offline-html-file-no-wasm]]'
status: unread
---

> **TL;DR:** The tool everyone's using is quietly damaging your photos If you strip metadata from an image, the usual approach is to decode it, delete the fields, and encode it again. That is the natural way to do it, because every i…

## What’s new and why it matters
The tool everyone's using is quietly damaging your photos If you strip metadata from an image, the usual approach is to decode it, delete the fields, and encode it again. That is the natural way to do it, because every image library exposes exactly that: a decode step, a field dictionary, an encode step. The problem is that JPEG is a lossy format, and the encoder you use is not the encoder that made the file. So a round trip through Pillow changes the bytes of the image data itself, not just the metadata: from PIL import Image im = Image . open ( " photo.jpg " ) clean = Image . new ( im . mode…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danyblitz/stripping-exif-at-the-byte-level-no-re-encoding-no-quality-loss-5bpo

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-09-02-i-generate-every-blog-cover-with-headless-chrome-and-a-bit-of-css-no-design-tool]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-31-how-i-made-sql-run-inside-a-single-offline-html-file-no-wasm]]
