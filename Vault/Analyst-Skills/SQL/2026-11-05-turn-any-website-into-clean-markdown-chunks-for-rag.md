---
title: Turn any website into clean Markdown chunks for RAG
date: '2026-11-05'
source: https://dev.to/aurelix_solutions/turn-any-website-into-clean-markdown-chunks-for-rag-475h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-21-pdf-to-clean-markdown-for-rag-chunking-ready-text-from-pdfs-word-and-scanned-files]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-10-14-google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser]]'
- '[[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** Most RAG quality problems start before the embedding model. If you feed it raw HTML, or text extracted with navigation, cookie banners and footers still attached, every chunk carries the same boilerplate. Retrieval then…

## What’s new and why it matters
Most RAG quality problems start before the embedding model. If you feed it raw HTML, or text extracted with navigation, cookie banners and footers still attached, every chunk carries the same boilerplate. Retrieval then matches "Privacy policy | Contact us | © 2026" as often as it matches the answer. This post covers the two steps that fix most of it: converting each page to clean Markdown of its main content, and chunking that Markdown along its headings so each chunk is a coherent section with a citation. Disclosure: I'm Aurelix, and I built the Website to Markdown Actor used for the crawl s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aurelix_solutions/turn-any-website-into-clean-markdown-chunks-for-rag-475h

## Related notes
- [[2026-10-21-pdf-to-clean-markdown-for-rag-chunking-ready-text-from-pdfs-word-and-scanned-files]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-10-14-google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser]]
- [[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
