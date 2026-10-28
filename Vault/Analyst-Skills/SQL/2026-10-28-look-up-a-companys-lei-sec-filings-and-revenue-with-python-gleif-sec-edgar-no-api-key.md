---
title: Look up a company's LEI, SEC filings and revenue with Python (GLEIF + SEC EDGAR,
  no API key)
date: '2026-10-28'
source: https://dev.to/hi_hphanthanh_41c4083/look-up-a-companys-lei-sec-filings-and-revenue-with-python-gleif-sec-edgar-no-api-key-4p74
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]'
- '[[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]'
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
- '[[2026-10-20-how-to-get-a-list-of-uk-companies-by-sic-code-and-postcode-no-api-key]]'
status: unread
---

> **TL;DR:** KYB checks, CRM enrichment and filing monitors all start with the same question: given a company name or ticker, who exactly is this legal entity, and what has it filed? Two free, official sources answer most of it: GLEI…

## What’s new and why it matters
KYB checks, CRM enrichment and filing monitors all start with the same question: given a company name or ticker, who exactly is this legal entity, and what has it filed? Two free, official sources answer most of it: GLEIF (the Legal Entity Identifier registry): legal name, jurisdiction, addresses, status and parent companies, worldwide. SEC EDGAR : CIK, industry code, every filing, and XBRL financials for US filers. Neither needs an API key. SEC only asks for a User-Agent with your contact and fewer than 10 requests per second. DIY: one company in about 30 lines # pip install requests import r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hi_hphanthanh_41c4083/look-up-a-companys-lei-sec-filings-and-revenue-with-python-gleif-sec-edgar-no-api-key-4p74

## Related notes
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]
- [[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
- [[2026-10-20-how-to-get-a-list-of-uk-companies-by-sic-code-and-postcode-no-api-key]]
