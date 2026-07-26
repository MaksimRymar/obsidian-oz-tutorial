---
title: A Small, Annoying Reminder About MySQL, Next.js, and Reality
date: '2026-07-25'
source: https://dev.to/nahamaalochi/a-small-annoying-reminder-about-mysql-nextjs-and-reality-2aln
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]'
- '[[2026-05-04-sql-date-time-functions-a-practical-guide-for-real-world-queries]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** Today's reminder that MySQL will happily let you believe you're doing everything "right" right up until it doesn't. I was wiring up a perfectly ordinary paginated query in a Next.js service. Nothing exotic. Prepared stat…

## What’s new and why it matters
Today's reminder that MySQL will happily let you believe you're doing everything "right" right up until it doesn't. I was wiring up a perfectly ordinary paginated query in a Next.js service. Nothing exotic. Prepared statements, placeholders, clean parameter handling. The kind of code you write on autopilot because you've written it a hundred times before. And then MySQL reminded me again that it is not PostgreSQL. The offending query looked harmless: SELECT * FROM writings ORDER BY created_at DESC LIMIT ? OFFSET ? The parameters were validated. Integers only. Floored. Bounded. Safe. Sensible.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nahamaalochi/a-small-annoying-reminder-about-mysql-nextjs-and-reality-2aln

## Related notes
- [[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]
- [[2026-05-04-sql-date-time-functions-a-practical-guide-for-real-world-queries]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
