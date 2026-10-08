---
title: I parsed 110,000 EU procurement awards. Half of them don't say when the contract
  was signed.
date: '2026-10-08'
source: https://dev.to/pennyforgehq/i-parsed-110000-eu-procurement-awards-half-of-them-dont-say-when-the-contract-was-signed-eib
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** Every two months or so, the EU publishes an open archive of everything its public authorities bought — Tenders Electronic Daily (TED) , the official journal of the day for EU procurement. In October 2026 I downloaded the…

## What’s new and why it matters
Every two months or so, the EU publishes an open archive of everything its public authorities bought — Tenders Electronic Daily (TED) , the official journal of the day for EU procurement. In October 2026 I downloaded the complete monthly packages for July, August and September 2026 — 1.16 GB of eForms/UBL XML, 213,716 notices, of which 110,217 are award notices (the documents that say who won what). I wrote four small Python scripts, parsed everything in about ten minutes, and got numbers the official statistics don't show you. The rule: under Directive 2014/24/EU, Article 50(1) , a contractin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pennyforgehq/i-parsed-110000-eu-procurement-awards-half-of-them-dont-say-when-the-contract-was-signed-eib

## Related notes
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
