---
title: Why Production Databases Break Normalization (And Why That's Okay)
date: '2026-03-11'
source: https://dev.to/ayushshrivastav/why-production-databases-break-normalization-and-why-thats-okay-3hih
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-25-how-to-send-telegram-bot-messages-from-a-database-using-sql]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** If you've taken any database course, you've been taught that normalization is the right way to design a schema. No duplicate data. Clean relationships. Every table with a single responsibility. Then you get a job at a re…

## What’s new and why it matters
If you've taken any database course, you've been taught that normalization is the right way to design a schema. No duplicate data. Clean relationships. Every table with a single responsibility. Then you get a job at a real company, open the codebase, and see this: messages -------- message_id channel_id user_id user_name user_avatar message_body created_at user_name ? user_avatar ? Right there in the messages table? Your first instinct might be to flag it as a bug. But here's the thing — this is not a mistake. Systems like this run at Slack, Discord, Instagram, and Twitter. These are deliberat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ayushshrivastav/why-production-databases-break-normalization-and-why-thats-okay-3hih

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-25-how-to-send-telegram-bot-messages-from-a-database-using-sql]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
