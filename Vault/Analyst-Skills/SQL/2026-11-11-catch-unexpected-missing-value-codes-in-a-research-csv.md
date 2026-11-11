---
title: Catch unexpected missing-value codes in a research CSV
date: '2026-11-11'
source: https://dev.to/nanchuangresearch/catch-unexpected-missing-value-codes-in-a-research-csv-3lli
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-28-check-a-shopify-product-csv-for-missing-prices-and-images-before-you-import-it]]'
- '[[2026-07-29-python-part-2]]'
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]'
- '[[2026-07-20-learn-configuration-precedence-with-empty-missing-and-invalid-values]]'
status: unread
---

> **TL;DR:** Before calculating a summary from a research export, decide which values your codebook treats as missing. One site might leave a field blank while another sends 999 . A numeric conversion will accept 999 and carry it int…

## What’s new and why it matters
Before calculating a summary from a research export, decide which values your codebook treats as missing. One site might leave a field blank while another sends 999 . A numeric conversion will accept 999 and carry it into a mean. Here is a fictional symptom score with a range of 0–20. The agreed missing tokens are blank and NA . The check keeps those rows separate and flags a numeric value outside the range for review. from csv import DictReader from io import StringIO source = StringIO ( "record,score\nA,6\nB,NA\nC,999\nD,0\n" ) valid = [ ] missing = [ ] review = [ ] for row in DictReader ( s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nanchuangresearch/catch-unexpected-missing-value-codes-in-a-research-csv-3lli

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-28-check-a-shopify-product-csv-for-missing-prices-and-images-before-you-import-it]]
- [[2026-07-29-python-part-2]]
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]
- [[2026-07-20-learn-configuration-precedence-with-empty-missing-and-invalid-values]]
