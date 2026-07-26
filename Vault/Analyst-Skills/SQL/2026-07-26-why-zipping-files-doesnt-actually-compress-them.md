---
title: Why Zipping Files Doesn't Actually Compress Them
date: '2026-07-26'
source: https://dev.to/uglypeardata/why-zipping-files-doesnt-actually-compress-them-404p
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-12-i-built-a-cli-gui-tool-for-file-automation-heres-what-it-does]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
status: unread
---

> **TL;DR:** The Frustrating Scenario You've been there. A colleague sends you a 50MB PDF report. You think it's too large to email, so you drop it into 7-Zip, crank the compression to "ultra," and wait. The result? A 49MB archive. Y…

## What’s new and why it matters
The Frustrating Scenario You've been there. A colleague sends you a 50MB PDF report. You think it's too large to email, so you drop it into 7-Zip, crank the compression to "ultra," and wait. The result? A 49MB archive. You send it anyway, the recipient extracts it, and the file is still 50MB—not a single byte smaller. This isn't a fluke. Take an already-compressed MP4, JPG, or PDF, stuff it into a ZIP file, and the size barely moves. Yet run the same 7-Zip over a folder of raw TXT, BMP, or CSV files, and the archive can shrink to a tenth of the original size. Why the dramatic difference? The a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/uglypeardata/why-zipping-files-doesnt-actually-compress-them-404p

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-12-i-built-a-cli-gui-tool-for-file-automation-heres-what-it-does]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
