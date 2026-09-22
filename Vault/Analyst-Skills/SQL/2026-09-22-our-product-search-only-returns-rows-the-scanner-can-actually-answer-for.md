---
title: Our product search only returns rows the scanner can actually answer for
date: '2026-09-22'
source: https://dev.to/daniel_pertu/our-product-search-only-returns-rows-the-scanner-can-actually-answer-for-40a4
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Munchable answers a barcode. You point the phone at a pack, the rules engine checks the ingredient list against the conditions on your profile, and you get a verdict. That works in a shop. It does not work on a Tuesday e…

## What’s new and why it matters
Munchable answers a barcode. You point the phone at a pack, the rules engine checks the ingredient list against the conditions on your profile, and you get a verdict. That works in a shop. It does not work on a Tuesday evening when you are writing a list and the pack is still in the shop. So we added name search. It is one GET route and about a hundred lines of query building, and almost none of that hundred lines is about matching text. It is about which rows are allowed to appear at all. A hit you cannot tap is worse than no hit The catalogue has rows in states the scan path quietly refuses…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/our-product-search-only-returns-rows-the-scanner-can-actually-answer-for-40a4

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
