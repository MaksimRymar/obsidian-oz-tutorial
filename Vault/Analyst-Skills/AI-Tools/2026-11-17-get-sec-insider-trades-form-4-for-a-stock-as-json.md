---
title: Get SEC insider trades (Form 4) for a stock as JSON
date: '2026-11-17'
source: https://dev.to/boscolabs/get-sec-insider-trades-form-4-for-a-stock-as-json-5ag4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-28-look-up-a-companys-lei-sec-filings-and-revenue-with-python-gleif-sec-edgar-no-api-key]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-07-28-congress-stock-trading-data-how-to-query-financial-disclosures-by-api-in-2026]]'
- '[[2026-03-18-parsing-form-4-how-to-extract-signal-from-sec-insider-trading-data]]'
- '[[2026-10-12-the-same-sec-filing-has-two-acceptance-times-depending-on-which-edgar-file-you-read]]'
- '[[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]'
status: unread
---

> **TL;DR:** When a director, officer or 10% owner of a US-listed company buys or sells its stock, they file a Form 4 with the SEC within two business days. The filings are public, but each one is an XML document somewhere in EDGAR,…

## What’s new and why it matters
When a director, officer or 10% owner of a US-listed company buys or sells its stock, they file a Form 4 with the SEC within two business days. The filings are public, but each one is an XML document somewhere in EDGAR, and a single filing can hold several transactions. Our SEC Insider Trading API on Apify reads them and gives you one row per transaction. One stock, last 90 days Say you want the open-market buys and sells by NVIDIA insiders over the last 90 days. The input: { "tickers" : [ "NVDA" ] , "transactionCodes" : [ "P" , "S" ] , "lookbackDays" : 90 , "maxResults" : 3 , "includeClusterS…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/boscolabs/get-sec-insider-trades-form-4-for-a-stock-as-json-5ag4

## Related notes
- [[2026-10-28-look-up-a-companys-lei-sec-filings-and-revenue-with-python-gleif-sec-edgar-no-api-key]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-07-28-congress-stock-trading-data-how-to-query-financial-disclosures-by-api-in-2026]]
- [[2026-03-18-parsing-form-4-how-to-extract-signal-from-sec-insider-trading-data]]
- [[2026-10-12-the-same-sec-filing-has-two-acceptance-times-depending-on-which-edgar-file-you-read]]
- [[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]
