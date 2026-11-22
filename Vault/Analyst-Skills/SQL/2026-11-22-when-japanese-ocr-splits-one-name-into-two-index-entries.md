---
title: When Japanese OCR splits one name into two index entries
date: '2026-11-22'
source: https://dev.to/taiki200504/when-japanese-ocr-splits-one-name-into-two-index-entries-1ld4
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-10-12-bookingcom-search-rows-hide-916-of-the-price-in-a-field-labelled-21-22-and-23]]'
- '[[2026-11-05-review-ai-generated-sql-before-you-trust-the-number-a-checklist-with-a-runnable-fixture]]'
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
status: unread
---

> **TL;DR:** I tested a small indexing workflow with four fictional rows across three pages. The simulated OCR output spelled the same local museum two ways: 青葉郷土舘 and 青葉郷土館. It also returned one year as full-width digits. I normaliz…

## What’s new and why it matters
I tested a small indexing workflow with four fictional rows across three pages. The simulated OCR output spelled the same local museum two ways: 青葉郷土舘 and 青葉郷土館. It also returned one year as full-width digits. I normalized the year field in Python and compared each row with a reference keyed to its source page. Three of the four rows matched after year normalization. Checking the remaining name against the reference brought the fixture to four out of four. The resulting index linked the museum and year 1977 to pages 1 and 2. The change log retained both spellings for page 1. This fixture exerc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/taiki200504/when-japanese-ocr-splits-one-name-into-two-index-entries-1ld4

## Related notes
- [[2026-10-12-bookingcom-search-rows-hide-916-of-the-price-in-a-field-labelled-21-22-and-23]]
- [[2026-11-05-review-ai-generated-sql-before-you-trust-the-number-a-checklist-with-a-runnable-fixture]]
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
