---
title: Groq's 14,400 requests a day is not for the chat models
date: '2026-08-24'
source: https://dev.to/build996/groqs-14400-requests-a-day-is-not-for-the-chat-models-1m12
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-12-business-analytics-vs-data-analytics-which-career-is-better-in-2026]]'
- '[[2026-08-13-detecting-sqlite-full-table-scans-in-nodejs]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** If you have sized a project against Groq's free tier recently, the number you probably wrote down was 14,400 requests per day. It appears in a lot of comparison posts. It is on Groq's own rate limits page too, which is w…

## What’s new and why it matters
If you have sized a project against Groq's free tier recently, the number you probably wrote down was 14,400 requests per day. It appears in a lot of comparison posts. It is on Groq's own rate limits page too, which is why it keeps propagating. It just isn't attached to a model you would chat with. Groq's Free Plan limits are published per model. As of today the chat models sit at 30 RPM and 1,000 RPD: openai/gpt-oss-120b , openai/gpt-oss-20b , and qwen/qwen3.6-27b all get 30 requests per minute, 1,000 per day, 8K tokens per minute, 200K per day. groq/compound is lower still at 250 RPD. The tw…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/build996/groqs-14400-requests-a-day-is-not-for-the-chat-models-1m12

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-12-business-analytics-vs-data-analytics-which-career-is-better-in-2026]]
- [[2026-08-13-detecting-sqlite-full-table-scans-in-nodejs]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
