---
title: Turning phone photos of a marksheet into one small PDF
date: '2026-10-30'
source: https://dev.to/glinck/turning-phone-photos-of-a-marksheet-into-one-small-pdf-4c2h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
- '[[2026-10-04-my-automated-quality-check-passed-garbage-here-is-the-second-layer-i-added]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-01-stripping-exif-at-the-byte-level-no-re-encoding-no-quality-loss]]'
status: unread
---

> **TL;DR:** A lot of upload forms want "one PDF, under 100 KB" for something you only have as phone photos: a two-sided marksheet, a certificate, a few pages of a transcript. Putting photos into a PDF is easy. Getting a small one wi…

## What’s new and why it matters
A lot of upload forms want "one PDF, under 100 KB" for something you only have as phone photos: a two-sided marksheet, a certificate, a few pages of a transcript. Putting photos into a PDF is easy. Getting a small one with even pages takes knowing what the PDF actually does with your JPEGs. Here's what I worked out, tested on dummy marksheet-style images I generated (no real documents). What a PDF does with a JPEG A PDF can store a JPEG as-is. The image object gets the filter /DCTDecode (DCT is the maths inside JPEG), and the compressed bytes from your file are copied straight in. Nothing is d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/glinck/turning-phone-photos-of-a-marksheet-into-one-small-pdf-4c2h

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
- [[2026-10-04-my-automated-quality-check-passed-garbage-here-is-the-second-layer-i-added]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-01-stripping-exif-at-the-byte-level-no-re-encoding-no-quality-loss]]
