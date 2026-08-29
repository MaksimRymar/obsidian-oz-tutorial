---
title: Add real search to your Python web app — no Elasticsearch, no separate service
date: '2026-08-29'
source: https://dev.to/priyasundaram/add-real-search-to-your-python-web-app-no-elasticsearch-no-separate-service-8la
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Every app eventually needs search that's better than WHERE title LIKE '%...%' . LIKE can't rank results, doesn't know that running should match run , and gets slow the moment your table is interesting. The usual next ste…

## What’s new and why it matters
Every app eventually needs search that's better than WHERE title LIKE '%...%' . LIKE can't rank results, doesn't know that running should match run , and gets slow the moment your table is interesting. The usual next step — stand up Elasticsearch or OpenSearch — means a JVM, a cluster to babysit, and a whole second data store to keep in sync. For a huge number of apps that's using a crane to hang a picture frame. whoosh3 is a pure-Python full-text search library (the maintained continuation of Whoosh). pip install whoosh3 and you get BM25 ranking, stemming, a real query language, and an index…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/priyasundaram/add-real-search-to-your-python-web-app-no-elasticsearch-no-separate-service-8la

## Related notes
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
