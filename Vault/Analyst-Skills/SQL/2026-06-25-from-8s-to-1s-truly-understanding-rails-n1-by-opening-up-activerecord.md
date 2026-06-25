---
title: 'From 8s to 1s: Truly Understanding Rails N+1 by Opening Up ActiveRecord'
date: '2026-06-25'
source: https://dev.to/danewu/from-8s-to-1s-truly-understanding-rails-n1-by-opening-up-activerecord-1oj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-04-16-sql-joins-explained]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** The hook: I added includes and the page was still N+1 We had an admin page listing couriers, each row showing how many shipments that courier had. As data grew, the page went from 1 second to 7–8 seconds. I opened the AP…

## What’s new and why it matters
The hook: I added includes and the page was still N+1 We had an admin page listing couriers, each row showing how many shipments that courier had. As data grew, the page went from 1 second to 7–8 seconds. I opened the APM (New Relic): SQL alone took 6+ seconds, and the query count had exploded — one page listing 200 couriers fired 200+ queries. Classic N+1 . I added includes(:shipments) , the query count dropped to 2, the page came back under 1 second, and I installed the Bullet gem in dev to catch N+1 automatically. Problem solved, I thought. Until another page — which already had includes ,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danewu/from-8s-to-1s-truly-understanding-rails-n1-by-opening-up-activerecord-1oj

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-04-16-sql-joins-explained]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
