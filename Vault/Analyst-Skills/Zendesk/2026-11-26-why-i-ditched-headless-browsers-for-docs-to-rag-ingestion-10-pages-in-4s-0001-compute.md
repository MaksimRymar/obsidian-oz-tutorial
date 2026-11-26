---
title: Why I Ditched Headless Browsers for Docs-to-RAG Ingestion (10 Pages in 4s,
  $0.001 Compute)
date: '2026-11-26'
source: https://dev.to/weiyi_wang_5fbdb721f38016/why-i-ditched-headless-browsers-for-docs-to-rag-ingestion-10-pages-in-4s-0001-compute-4k01
domain: Zendesk
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-20-extract-every-url-from-a-sitemapxml-in-python-indexes-gz-robotstxt-and-spot-competitors-new-pages]]'
- '[[2026-11-05-turn-any-website-into-clean-markdown-chunks-for-rag]]'
- '[[2026-11-06-how-to-convert-any-webpage-to-clean-markdown-for-rag-save-90-llm-tokens-in-nodejs]]'
- '[[2026-05-15-build-a-rag-pipeline-that-actually-reads-the-web]]'
- '[[2026-10-31-turning-any-website-into-clean-llm-ready-markdown-for-ai-rag-pipelines-in-python]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** If you have ever built a production RAG pipeline over external developer docs, you probably hit the same three walls I did: Headless browser tax : Spinning up Playwright/Chromium just to fetch static Docusaurus, Mintlify…

## What’s new and why it matters
If you have ever built a production RAG pipeline over external developer docs, you probably hit the same three walls I did: Headless browser tax : Spinning up Playwright/Chromium just to fetch static Docusaurus, Mintlify, or MkDocs documentation takes 45–90 seconds for 10 pages and burns gigabytes of RAM. Broken Markdown chunking : Naive ^# regex splitters mistake # this is a python comment inside fenced code blocks for H1 headings—splitting code snippets mid-function and dropping language tags ( ` python ). Wasted re-embedding spend : Running a weekly cron job re-scrapes and re-embeds all 500…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/weiyi_wang_5fbdb721f38016/why-i-ditched-headless-browsers-for-docs-to-rag-ingestion-10-pages-in-4s-0001-compute-4k01

## Related notes
- [[2026-10-20-extract-every-url-from-a-sitemapxml-in-python-indexes-gz-robotstxt-and-spot-competitors-new-pages]]
- [[2026-11-05-turn-any-website-into-clean-markdown-chunks-for-rag]]
- [[2026-11-06-how-to-convert-any-webpage-to-clean-markdown-for-rag-save-90-llm-tokens-in-nodejs]]
- [[2026-05-15-build-a-rag-pipeline-that-actually-reads-the-web]]
- [[2026-10-31-turning-any-website-into-clean-llm-ready-markdown-for-ai-rag-pipelines-in-python]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
