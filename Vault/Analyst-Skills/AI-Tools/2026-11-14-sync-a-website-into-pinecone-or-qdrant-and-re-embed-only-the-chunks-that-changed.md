---
title: Sync a website into Pinecone or Qdrant and re-embed only the chunks that changed
date: '2026-11-14'
source: https://dev.to/aurelix_solutions/sync-a-website-into-pinecone-or-qdrant-and-re-embed-only-the-chunks-that-changed-21j3
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-05-turn-any-website-into-clean-markdown-chunks-for-rag]]'
- '[[2026-07-25-google-images-scraper-how-to-bulk-export-image-search-results-as-json-in-2026]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-11-07-a-broken-link-and-seo-audit-of-your-whole-site-with-a-ranked-fix-list-for-your-developer]]'
status: unread
---

> **TL;DR:** Getting a docs site into a vector database once is the easy part. Keeping it current is where most RAG projects quietly fail: the docs change every week, the index doesn't, and the assistant keeps citing a page that was…

## What’s new and why it matters
Getting a docs site into a vector database once is the easy part. Keeping it current is where most RAG projects quietly fail: the docs change every week, the index doesn't, and the assistant keeps citing a page that was rewritten a month ago. A nightly full re-crawl fixes freshness but re-embeds thousands of unchanged chunks to pick up a handful of edits, and still leaves deleted pages in the index. What a sync actually needs is a list of operations: these chunks are new or edited, upsert them; these chunk IDs no longer exist, delete them. This post gets that list from a scheduled run, one row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aurelix_solutions/sync-a-website-into-pinecone-or-qdrant-and-re-embed-only-the-chunks-that-changed-21j3

## Related notes
- [[2026-11-05-turn-any-website-into-clean-markdown-chunks-for-rag]]
- [[2026-07-25-google-images-scraper-how-to-bulk-export-image-search-results-as-json-in-2026]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-11-07-a-broken-link-and-seo-audit-of-your-whole-site-with-a-ranked-fix-list-for-your-developer]]
