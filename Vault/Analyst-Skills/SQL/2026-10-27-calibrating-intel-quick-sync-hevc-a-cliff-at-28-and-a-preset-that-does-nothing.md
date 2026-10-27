---
title: 'Calibrating Intel Quick Sync HEVC: A Cliff at 28, and a Preset That Does Nothing'
date: '2026-10-27'
source: https://dev.to/hoelee/calibrating-intel-quick-sync-hevc-a-cliff-at-28-and-a-preset-that-does-nothing-19k0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** Originally published on my blog — read it there with the full context, code and updates . The question I could not answer: which number do I ship? My transcoding queue decides, per file, which encoder does the work: copy…

## What’s new and why it matters
Originally published on my blog — read it there with the full context, code and updates . The question I could not answer: which number do I ship? My transcoding queue decides, per file, which encoder does the work: copy when the source is already efficient, NVENC on the GPU, x265 on the CPU — and now Intel Quick Sync. Each tier has two knobs that decide quality, and every tier except QSV had numbers I had measured on my own library. QSV had none. And the code refused to guess: a shipping default of qsv_quality = 0 / qsv_preset = "" means nobody has calibrated this , and the engine treats that…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hoelee/calibrating-intel-quick-sync-hevc-a-cliff-at-28-and-a-preset-that-does-nothing-19k0

## Related notes
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
