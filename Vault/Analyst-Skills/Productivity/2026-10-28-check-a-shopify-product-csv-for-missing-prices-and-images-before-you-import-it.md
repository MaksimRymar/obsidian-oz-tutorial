---
title: Check a Shopify product CSV for missing prices and images before you import
  it
date: '2026-10-28'
source: https://dev.to/steven_keil_cb87a560f87f0/check-a-shopify-product-csv-for-missing-prices-and-images-before-you-import-it-2p1i
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
status: unread
---

> **TL;DR:** Before you import a product CSV into Shopify, it helps to know which products have no price or no image. Shopify may accept the file anyway, and you only notice later that a product shows up without a picture or at 0.00.…

## What’s new and why it matters
Before you import a product CSV into Shopify, it helps to know which products have no price or no image. Shopify may accept the file anyway, and you only notice later that a product shows up without a picture or at 0.00. This script reads a product CSV and lists every product that has a missing, zero or unreadable price, or no image at all. It only reads the file and never changes it. It uses only Python's standard library. One product, several rows In Shopify's product CSV a product can span several rows: one per variant, plus extra rows that only carry another image. So "no image" cannot be…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/steven_keil_cb87a560f87f0/check-a-shopify-product-csv-for-missing-prices-and-images-before-you-import-it-2p1i

## Related notes
- [[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
