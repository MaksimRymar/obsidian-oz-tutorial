---
title: 'Probing FTS5 Support in node:sqlite: A Field Guide to Graceful Degradation'
date: '2026-10-01'
source: https://dev.to/shubh-sa-24/probing-fts5-support-in-nodesqlite-a-field-guide-to-graceful-degradation-2n8e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Probing FTS5 Support in node:sqlite: A Field Guide to Graceful Degradation A recall feature I had shipped with confidence died in a new environment with a single line: SQLITE_ERROR: no such module: fts5 The code was not…

## What’s new and why it matters
Probing FTS5 Support in node:sqlite: A Field Guide to Graceful Degradation A recall feature I had shipped with confidence died in a new environment with a single line: SQLITE_ERROR: no such module: fts5 The code was not wrong. The assumption was. I had assumed that because SQLite was present, SQLite's full-text search engine was present too. With node:sqlite — Node's built-in SQLite binding — that assumption is not guaranteed. This is the field guide I wish I had: how to probe for FTS5 honestly, how to degrade to a deterministic fallback without pretending, and how to keep the whole thing test…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shubh-sa-24/probing-fts5-support-in-nodesqlite-a-field-guide-to-graceful-degradation-2n8e

## Related notes
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
