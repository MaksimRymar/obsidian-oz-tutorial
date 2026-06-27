---
title: I Reverse Engineered a Closed-Format App. Everything Was in SQLite.
date: '2026-06-26'
source: https://dev.to/antonio_zhu_e726fd856cd86/i-reverse-engineered-a-closed-format-app-everything-was-in-sqlite-340g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-saves-you-money-in-2026]]'
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-05-16-i-taught-sql-to-complete-beginners-heres-what-actually-happened]]'
status: unread
---

> **TL;DR:** I had accumulated over two thousand notes in Youdao Cloud Note over several years. When I decided to move to Obsidian, the first thing I checked was the export feature. There wasn't one. No batch export, no single-note e…

## What’s new and why it matters
I had accumulated over two thousand notes in Youdao Cloud Note over several years. When I decided to move to Obsidian, the first thing I checked was the export feature. There wasn't one. No batch export, no single-note export, nothing in the Mac client. So I went looking for the local data. Where The Data Was On macOS, Youdao Cloud Note stores its data here: ~/Library/Containers/ynote-desktop/Data/Library/Application Support/ynote-desktop/ Inside that directory, organized by account email, were three SQLite databases: < account >. db # note metadata, folder hierarchy < account >- content . db…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/antonio_zhu_e726fd856cd86/i-reverse-engineered-a-closed-format-app-everything-was-in-sqlite-340g

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-saves-you-money-in-2026]]
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-05-16-i-taught-sql-to-complete-beginners-heres-what-actually-happened]]
