---
title: '"My Comment-Reply Script Asked DEV.to for ''My Articles.'' Leaving Off One
  Query Param Silently Dropped the Newest Two."'
date: '2026-08-07'
source: https://dev.to/enjoy_kumawat/my-comment-reply-script-asked-devto-for-my-articles-leaving-off-one-query-param-silently-6j2
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-02-my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** I've written before about this exact publishing pipeline under-listing its own history — the scheduled task's Step 1 hits /api/articles/me/published?per_page=30 and treats that single page as "the full list," silently mi…

## What’s new and why it matters
I've written before about this exact publishing pipeline under-listing its own history — the scheduled task's Step 1 hits /api/articles/me/published?per_page=30 and treats that single page as "the full list," silently missing every article past the most recent thirty. That bug lived in a different script ( publish_devto.py 's caller) and had an obvious cause: per_page is a page size, not a total, and nobody had ever added a page loop. I fixed it three days ago with scripts/list_all_published_titles.py , which walks pages until one comes back empty. Today I found the same symptom — the newest a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-comment-reply-script-asked-devto-for-my-articles-leaving-off-one-query-param-silently-6j2

## Related notes
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-02-my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
