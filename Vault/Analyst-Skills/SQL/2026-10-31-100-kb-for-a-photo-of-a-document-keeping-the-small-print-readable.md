---
title: '100 KB for a photo of a document: keeping the small print readable'
date: '2026-10-31'
source: https://dev.to/glinck/100-kb-for-a-photo-of-a-document-keeping-the-small-print-readable-5hi3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-10-30-turning-phone-photos-of-a-marksheet-into-one-small-pdf]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
status: unread
---

> **TL;DR:** Upload forms often want a scan or photo of a document "under 100 KB". A phone photo of a page is often a few megabytes, and the obvious fix, dragging a quality slider down until the number fits, tends to turn the small p…

## What’s new and why it matters
Upload forms often want a scan or photo of a document "under 100 KB". A phone photo of a page is often a few megabytes, and the obvious fix, dragging a quality slider down until the number fits, tends to turn the small print into mush. The order you do things in matters more than the slider. Here's what I worked out, tested on dummy document photos I generated (no real documents). 100 KB is two different numbers Some software counts 1 KB as 1,000 bytes and some as 1,024, so "100 KB" is either 100,000 or 102,400 bytes. A form rarely says which. If you aim for 100,000 bytes or less, the file pas…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/glinck/100-kb-for-a-photo-of-a-document-keeping-the-small-print-readable-5hi3

## Related notes
- [[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-10-30-turning-phone-photos-of-a-marksheet-into-one-small-pdf]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
