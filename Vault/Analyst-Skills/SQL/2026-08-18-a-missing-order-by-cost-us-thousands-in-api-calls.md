---
title: A missing ORDER BY cost us Thousands in API calls
date: '2026-08-18'
source: https://dev.to/mathorde/a-missing-order-by-cost-us-thousands-in-api-calls-5elg
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]'
status: unread
---

> **TL;DR:** In 2022, I fixed one of the most expensive one-line bugs we've shipped. The fix was this: - Area.all() + Area.query().orderBy('id') That's it. A missing SQL ORDER BY was causing identical requests to generate different R…

## What’s new and why it matters
In 2022, I fixed one of the most expensive one-line bugs we've shipped. The fix was this: - Area.all() + Area.query().orderBy('id') That's it. A missing SQL ORDER BY was causing identical requests to generate different Redis cache keys. The application worked. Redis worked. MySQL worked. But our Google Maps API bill had climbed to around €3,500 per year. The context I'm the co-founder and CTO of MyCater , a B2B catering marketplace. One of the things our backend needs to determine is which caterers can deliver to a customer's address. These checks happen several times during the ordering proce…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mathorde/a-missing-order-by-cost-us-thousands-in-api-calls-5elg

## Related notes
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]
