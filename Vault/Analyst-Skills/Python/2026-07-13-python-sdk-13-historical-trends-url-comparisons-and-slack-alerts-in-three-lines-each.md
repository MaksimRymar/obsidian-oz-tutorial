---
title: 'Python SDK 1.3: Historical Trends, URL Comparisons, and Slack Alerts in Three
  Lines Each'
date: '2026-07-13'
source: https://dev.to/avansledright/python-sdk-13-historical-trends-url-comparisons-and-slack-alerts-in-three-lines-each-4igo
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]'
- '[[2026-03-16-why-alembic-is-basically-git-for-your-database-and-why-you-need-it]]'
status: unread
---

> **TL;DR:** The Python client for SEO Score API hit 1.3.0 today. It picks up everything we shipped through the latest sprint: side-by-side URL comparison, the /history and /history/domains endpoints, and webhook alerts (Slack-format…

## What’s new and why it matters
The Python client for SEO Score API hit 1.3.0 today. It picks up everything we shipped through the latest sprint: side-by-side URL comparison, the /history and /history/domains endpoints, and webhook alerts (Slack-formatted by default) on the monitor system. If you already have seoscoreapi installed, upgrade with: pip install --upgrade seoscoreapi Then the rest of this post is a tour of what the new functions actually do. What's in 1.3 Function Endpoint Tier compare(urls, api_key) POST /compare Basic+ history(url, api_key, limit=100, since=None) GET /history Starter+ history_domains(api_key) G…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/avansledright/python-sdk-13-historical-trends-url-comparisons-and-slack-alerts-in-three-lines-each-4igo

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]
- [[2026-03-16-why-alembic-is-basically-git-for-your-database-and-why-you-need-it]]
