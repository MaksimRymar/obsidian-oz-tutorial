---
title: My Repo Had Two Scripts That Hit the Same API. Only One Still Matched What
  I Actually Do.
date: '2026-07-16'
source: https://dev.to/enjoy_kumawat/my-repo-had-two-scripts-that-hit-the-same-api-only-one-still-matched-what-i-actually-do-10j4
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** I went looking for "the dev.to publish script" in this repo and found two of them. Not two versions in git history — two live, executable, fully-working .py files sitting in the same directory: post_article.py and publis…

## What’s new and why it matters
I went looking for "the dev.to publish script" in this repo and found two of them. Not two versions in git history — two live, executable, fully-working .py files sitting in the same directory: post_article.py and publish_devto.py . Both authenticate with the same DEV_TO_API key, both POST to the same https://dev.to/api/articles endpoint, both would run without error if invoked. Only one of them does what the current workflow actually needs. That's a specific, boring-sounding kind of bug, and I want to walk through why it's more dangerous for an agent than for a human maintainer, because the f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-repo-had-two-scripts-that-hit-the-same-api-only-one-still-matched-what-i-actually-do-10j4

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
