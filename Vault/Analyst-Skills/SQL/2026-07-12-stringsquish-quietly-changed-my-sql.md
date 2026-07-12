---
title: String#squish Quietly Changed My SQL
date: '2026-07-12'
source: https://dev.to/jessalejo/stringsquish-quietly-changed-my-sql-gc3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** I use String#squish almost without thinking. It's one of those little ActiveSupport helpers that keeps heredoc SQL readable in code and tidy in logs. You write a nicely indented query, call .squish , and end up with a cl…

## What’s new and why it matters
I use String#squish almost without thinking. It's one of those little ActiveSupport helpers that keeps heredoc SQL readable in code and tidy in logs. You write a nicely indented query, call .squish , and end up with a clean one-liner. sql = <<~ SQL . squish SELECT * FROM orders WHERE status = 'active' SQL # => "SELECT * FROM orders WHERE status = 'active'" I still love it. Last week, though, it introduced a bug so subtle that I chased it through three layers of the stack before realizing the culprit had been sitting in plain sight the whole time. The bug report A reporting dashboard had an "Av…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jessalejo/stringsquish-quietly-changed-my-sql-gc3

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
