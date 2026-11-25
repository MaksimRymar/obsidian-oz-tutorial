---
title: 'ORA-01722 Invalid Number: The Bad Rows Were Always There. The Plan Wasn''t.'
date: '2026-11-25'
source: https://dev.to/uptimearchitect/ora-01722-invalid-number-the-bad-rows-were-always-there-the-plan-wasnt-4jae
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]'
- '[[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-11-23-reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-and-identical]]'
status: unread
---

> **TL;DR:** A report has run every morning for months. Today it fails with the error older releases print as: ORA-01722: invalid number Nobody deployed anything. Nobody loaded new data. Someone checks the column, finds 'n/a' and 'AL…

## What’s new and why it matters
A report has run every morning for months. Today it fails with the error older releases print as: ORA-01722: invalid number Nobody deployed anything. Nobody loaded new data. Someone checks the column, finds 'n/a' and 'ALARM' in it, and asks the obvious question: how did this ever work? The rows that can't be converted were there all along. The query has a filter that's supposed to keep them away from TO_NUMBER . On some days it does, and on others it doesn't, because SQL doesn't promise an order of evaluation, and the plan decides which rows reach the conversion. This post shows that happening…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/uptimearchitect/ora-01722-invalid-number-the-bad-rows-were-always-there-the-plan-wasnt-4jae

## Related notes
- [[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]
- [[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-11-23-reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-and-identical]]
