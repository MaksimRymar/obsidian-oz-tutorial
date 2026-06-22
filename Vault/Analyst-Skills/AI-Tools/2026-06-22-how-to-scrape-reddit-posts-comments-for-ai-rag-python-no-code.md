---
title: How to Scrape Reddit Posts & Comments for AI / RAG (Python + No-Code)
date: '2026-06-22'
source: https://dev.to/benthepythondev/how-to-scrape-reddit-posts-comments-for-ai-rag-python-no-code-4d46
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-09-how-to-scrape-g2-and-trustpilot-reviews-in-2026-with-python-examples]]'
- '[[2026-05-30-simple-sql-tool]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
status: unread
---

> **TL;DR:** Reddit is one of the richest sources of real human opinion on the internet — which makes it gold for RAG pipelines, sentiment analysis, and market research. Here's how to pull Reddit posts and comments in 2026, the limit…

## What’s new and why it matters
Reddit is one of the richest sources of real human opinion on the internet — which makes it gold for RAG pipelines, sentiment analysis, and market research. Here's how to pull Reddit posts and comments in 2026, the limits to know about, and a no-code option that outputs clean markdown ready for embeddings. Option 1: the official Reddit API (PRAW) import praw reddit = praw . Reddit ( client_id = " ... " , client_secret = " ... " , user_agent = " my-app " ) for post in reddit . subreddit ( " dataengineering " ). hot ( limit = 25 ): print ( post . title , post . score , post . url ) post . commen…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/benthepythondev/how-to-scrape-reddit-posts-comments-for-ai-rag-python-no-code-4d46

## Related notes
- [[2026-04-09-how-to-scrape-g2-and-trustpilot-reviews-in-2026-with-python-examples]]
- [[2026-05-30-simple-sql-tool]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
