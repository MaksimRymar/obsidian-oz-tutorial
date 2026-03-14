---
title: I Was Tired of Parsing XBRL, So I Built a SEC EDGAR API
date: '2026-03-14'
source: https://dev.to/liam_altie/i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api-1jp3
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-28-how-to-track-what-billionaire-investors-are-buying-using-sec-edgar-data]]'
- '[[2026-03-08-i-built-a-rest-api-generator-in-python-so-you-never-mock-an-endpoint-again]]'
- '[[2026-03-01-async-python-made-simple-a-practical-guide-to-asyncio]]'
- '[[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]'
- '[[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
status: unread
---

> **TL;DR:** If you've ever tried to pull financial data from the SEC's EDGAR system, you probably know where this is going. I wanted to build a stock screener. Simple idea — just show me revenue trends for a few companies. Should ta…

## What’s new and why it matters
If you've ever tried to pull financial data from the SEC's EDGAR system, you probably know where this is going. I wanted to build a stock screener. Simple idea — just show me revenue trends for a few companies. Should take an afternoon, right? Nope. First you need a company's CIK number (Apple is 0000320193 — don't ask me why it's zero-padded to 10 digits). Then you download their XBRL filings, which are nested XML with namespaces like us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax . Then you realize different companies use slightly different tags for the same concept. Then you st…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/liam_altie/i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api-1jp3

## Related notes
- [[2026-02-28-how-to-track-what-billionaire-investors-are-buying-using-sec-edgar-data]]
- [[2026-03-08-i-built-a-rest-api-generator-in-python-so-you-never-mock-an-endpoint-again]]
- [[2026-03-01-async-python-made-simple-a-practical-guide-to-asyncio]]
- [[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]
- [[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
