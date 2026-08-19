---
title: The cp932 crash in the build gate that only happened on Windows — static detection,
  behavioral testing, and a negative check
date: '2026-08-19'
source: https://dev.to/susumun/the-cp932-crash-in-the-build-gate-that-only-happened-on-windows-static-detection-behavioral-mpd
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-11-your-test-went-red-can-you-read-it]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-07-17-oracle-ora-01461-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** The symptom During the Windows build for v1.6.11, the build gate reported "version number consistency check failed." But the version numbers were correct everywhere. The real cause was not a version mismatch. The build g…

## What’s new and why it matters
The symptom During the Windows build for v1.6.11, the build gate reported "version number consistency check failed." But the version numbers were correct everywhere. The real cause was not a version mismatch. The build gate in build_app.py calls tools/bump_version.py via subprocess and checks its exit code. The success messages in bump_version.py contained emoji (✅ and similar). On Japanese Windows, the default code page is cp932, which cannot encode those characters. Python raised a UnicodeEncodeError on the very first write to stdout, the process exited non-zero, and the build gate misread t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/susumun/the-cp932-crash-in-the-build-gate-that-only-happened-on-windows-static-detection-behavioral-mpd

## Related notes
- [[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-11-your-test-went-red-can-you-read-it]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-07-17-oracle-ora-01461-error-causes-and-solutions-complete-guide]]
