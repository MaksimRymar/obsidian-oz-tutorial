---
title: Heart Part 7 - dalCTF 2026
date: '2026-06-08'
source: https://dev.to/exploitnotes/heart-part-7-dalctf-2026-2a77
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-28-tinybird-has-a-free-real-time-analytics-api-query-billions-of-rows-in-milliseconds]]'
- '[[2026-05-10-injection-attacks-are-not-dead-sql-nosql-orm-and-command-injection-how-to-actually-fix-them-2026]]'
- '[[2026-05-29-building-helix-an-open-source-visual-identity-mapper-that-cuts-the-noise]]'
- '[[2026-06-01-your-scraper-returned-a-clean-row-it-was-wrong]]'
- '[[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** Category: Web Flag: dalctf{p1mp_p1mp_h00r4y} Overview A multi-stage web challenge themed around Kendrick Lamar's m.A.A.d city / Kung Fu Kenny lore. The attack chain involved: SQL injection to bypass authentication and ge…

## What’s new and why it matters
Category: Web Flag: dalctf{p1mp_p1mp_h00r4y} Overview A multi-stage web challenge themed around Kendrick Lamar's m.A.A.d city / Kung Fu Kenny lore. The attack chain involved: SQL injection to bypass authentication and get an admin JWT Heap memory disclosure via an unbounded echo buffer to leak the AES-256 key Fetching and decrypting the flag using the leaked key and a separate IV field in the API response Step 1 - SQL Injection → Admin Session The /login endpoint was vulnerable to classic SQL injection. Commenting out the password check with -- - bypassed authentication entirely and redirected…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/exploitnotes/heart-part-7-dalctf-2026-2a77

## Related notes
- [[2026-03-28-tinybird-has-a-free-real-time-analytics-api-query-billions-of-rows-in-milliseconds]]
- [[2026-05-10-injection-attacks-are-not-dead-sql-nosql-orm-and-command-injection-how-to-actually-fix-them-2026]]
- [[2026-05-29-building-helix-an-open-source-visual-identity-mapper-that-cuts-the-noise]]
- [[2026-06-01-your-scraper-returned-a-clean-row-it-was-wrong]]
- [[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
