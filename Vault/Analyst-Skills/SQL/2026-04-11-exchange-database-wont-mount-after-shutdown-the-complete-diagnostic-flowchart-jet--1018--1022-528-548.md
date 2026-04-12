---
title: 'Exchange Database Won''t Mount After Shutdown: The Complete Diagnostic Flowchart
  (JET -1018, -1022, 528, 548)'
date: '2026-04-11'
source: https://dev.to/bharat_bsingh_6f4fe7fc7/exchange-database-wont-mount-after-shutdown-the-complete-diagnostic-flowchart-jet-1018-1022-59bg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-14-schema-risk]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** Quick Answer: In over 90% of cases, an Exchange database won't mount because of one of four JET (Joint Engine Technology) errors triggered by a dirty shutdown: -1018 (page checksum mismatch), -1022 (disk I/O failure), 52…

## What’s new and why it matters
Quick Answer: In over 90% of cases, an Exchange database won't mount because of one of four JET (Joint Engine Technology) errors triggered by a dirty shutdown: -1018 (page checksum mismatch), -1022 (disk I/O failure), 528 (missing log file), or 548 (log file mismatch). Each error points to a different failure layer and requires a different recovery path. Running eseutil /p without diagnosing the exact error first is the most common reason recovery attempts destroy data instead of saving it. Why Exchange Databases Fail to Mount: The Core Mechanic Microsoft Exchange Server stores all mailbox dat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bharat_bsingh_6f4fe7fc7/exchange-database-wont-mount-after-shutdown-the-complete-diagnostic-flowchart-jet-1018-1022-59bg

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-14-schema-risk]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
