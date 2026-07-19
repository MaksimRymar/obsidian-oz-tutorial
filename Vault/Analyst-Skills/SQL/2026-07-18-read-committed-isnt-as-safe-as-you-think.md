---
title: READ COMMITTED isn't as safe as you think
date: '2026-07-18'
source: https://dev.to/dip_032d2fe1959e1990ddbb1/read-committed-isnt-as-safe-as-you-think-119i
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
status: unread
---

> **TL;DR:** Every Postgres app I've worked on runs at READ COMMITTED. It's the default. It's what your ORM opens transactions with unless you tell it otherwise. And it's silently allowing bugs you'd assume it prevents. We tend to wr…

## What’s new and why it matters
Every Postgres app I've worked on runs at READ COMMITTED. It's the default. It's what your ORM opens transactions with unless you tell it otherwise. And it's silently allowing bugs you'd assume it prevents. We tend to write database code with a vague sense that the transaction is "protecting" us — that once we wrapped a read and a write in BEGIN / COMMIT , the database would handle the concurrency. Most of the time it does. Right up until two requests hit the same row within the same few milliseconds. Let's look at what READ COMMITTED actually promises. And what it doesn't. What READ COMMITTED…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dip_032d2fe1959e1990ddbb1/read-committed-isnt-as-safe-as-you-think-119i

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
