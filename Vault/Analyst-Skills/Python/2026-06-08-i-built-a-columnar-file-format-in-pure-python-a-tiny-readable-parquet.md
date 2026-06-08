---
title: I Built a Columnar File Format in Pure Python — a tiny, readable Parquet
date: '2026-06-08'
source: https://dev.to/hajirufai/i-built-a-columnar-file-format-in-pure-python-a-tiny-readable-parquet-nj7
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
status: unread
---

> **TL;DR:** A while back I caught myself in an interview saying "yeah, I use Parquet a lot" — and then realized I couldn't actually explain why it's faster than a CSV beyond hand-waving about "columnar." That bugged me. So I did the…

## What’s new and why it matters
A while back I caught myself in an interview saying "yeah, I use Parquet a lot" — and then realized I couldn't actually explain why it's faster than a CSV beyond hand-waving about "columnar." That bugged me. So I did the thing that always fixes this for me: I rebuilt it from scratch. The result is Columna , a columnar storage engine and file format written in pure Python. No pandas, no pyarrow, no numpy. Just struct and zlib from the standard library. It's about 3,000 lines, it has 81 tests, and on a 50,000-row dataset it ends up 91% smaller than the equivalent CSV while reading 98% fewer byte…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hajirufai/i-built-a-columnar-file-format-in-pure-python-a-tiny-readable-parquet-nj7

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
