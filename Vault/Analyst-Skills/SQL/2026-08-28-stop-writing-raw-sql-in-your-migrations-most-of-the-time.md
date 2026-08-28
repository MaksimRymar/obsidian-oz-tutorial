---
title: Stop writing raw SQL in your migrations (most of the time)
date: '2026-08-28'
source: https://dev.to/darkmavis1980/stop-writing-raw-sql-in-your-migrations-most-of-the-time-i1o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-24-the-sql-query-mistakes-that-cost-me-points-in-my-database-assignment]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
status: unread
---

> **TL;DR:** Something I keep seeing across teams, especially with people who are getting comfortable with tools like db-migrate or Kysely , is a very specific habit: they reach for raw SQL for everything . Need to add a column? Raw…

## What’s new and why it matters
Something I keep seeing across teams, especially with people who are getting comfortable with tools like db-migrate or Kysely , is a very specific habit: they reach for raw SQL for everything . Need to add a column? Raw ALTER TABLE . Need to create a table? Raw CREATE TABLE . Need to add an index? You guessed it, another raw query. And look, raw SQL is not evil, and I'm not here to tell you to never use it. But when your migration tool gives you a proper schema builder and you skip it to write raw strings for a simple column addition, you're throwing away a lot of the things that make those to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/darkmavis1980/stop-writing-raw-sql-in-your-migrations-most-of-the-time-i1o

## Related notes
- [[2026-04-24-the-sql-query-mistakes-that-cost-me-points-in-my-database-assignment]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
