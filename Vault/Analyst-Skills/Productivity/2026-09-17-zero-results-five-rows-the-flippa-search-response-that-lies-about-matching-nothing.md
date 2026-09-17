---
title: 'Zero results, five rows: the Flippa search response that lies about matching
  nothing'
date: '2026-09-17'
source: https://dev.to/devil_scrapes/zero-results-five-rows-the-flippa-search-response-that-lies-about-matching-nothing-h54
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]'
- '[[2026-09-06-checking-if-a-businesss-google-profile-actually-matches-its-own-website]]'
status: unread
---

> **TL;DR:** Quick answer: When Flippa's search returns metadata.totalResults: 0 , the results array is not empty — it still contains about five unrelated "recommended" listings. Read len(results) and you will hand your customer five…

## What’s new and why it matters
Quick answer: When Flippa's search returns metadata.totalResults: 0 , the results array is not empty — it still contains about five unrelated "recommended" listings. Read len(results) and you will hand your customer five junk rows labelled as search hits. totalResults , not the array length, is the only trustworthy answer to "did we match anything?" How does a zero-result search return five results? Confirmed live on 2026-09-16 with two filters Flippa's search doesn't actually support — status=closed and status=sold . Both came back with metadata.totalResults: 0 , and both came back with five…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/zero-results-five-rows-the-flippa-search-response-that-lies-about-matching-nothing-h54

## Related notes
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]
- [[2026-09-06-checking-if-a-businesss-google-profile-actually-matches-its-own-website]]
