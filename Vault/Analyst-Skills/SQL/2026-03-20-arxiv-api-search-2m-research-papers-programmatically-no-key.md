---
title: 'arXiv API: Search 2M+ Research Papers Programmatically (No Key)'
date: '2026-03-20'
source: https://dev.to/__8ef7243a4f/arxiv-api-search-2m-research-papers-programmatically-no-key-f2a
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-20-pypi-api-discover-python-packages-in-any-domain-free-instant]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-03-20-scraping-hacker-news-in-2026-complete-guide-algolia-api-date-filters]]'
- '[[2026-03-20-scraping-youtube-channel-data-in-2026-videos-playlists-and-metadata]]'
- '[[2026-03-17-why-developers-are-switching-to-self-hosted-ai-image-apis-in-2026]]'
status: unread
---

> **TL;DR:** arXiv has over 2 million papers and a completely free API. No authentication, no rate limits (within reason), structured XML responses. Basic Search curl 'http://export.arxiv.org/api/query?search_query=all:machine+learni…

## What’s new and why it matters
arXiv has over 2 million papers and a completely free API. No authentication, no rate limits (within reason), structured XML responses. Basic Search curl 'http://export.arxiv.org/api/query?search_query=all:machine+learning&max_results=5' Returns Atom XML with: title, abstract, authors, categories, published date, PDF link. Node.js Example async function searchArxiv ( query , maxResults = 10 ) { const url = `http://export.arxiv.org/api/query?search_query=all: ${ encodeURIComponent ( query )} &max_results= ${ maxResults } &sortBy=submittedDate&sortOrder=descending` ; const res = await fetch ( ur…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/__8ef7243a4f/arxiv-api-search-2m-research-papers-programmatically-no-key-f2a

## Related notes
- [[2026-03-20-pypi-api-discover-python-packages-in-any-domain-free-instant]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-03-20-scraping-hacker-news-in-2026-complete-guide-algolia-api-date-filters]]
- [[2026-03-20-scraping-youtube-channel-data-in-2026-videos-playlists-and-metadata]]
- [[2026-03-17-why-developers-are-switching-to-self-hosted-ai-image-apis-in-2026]]
