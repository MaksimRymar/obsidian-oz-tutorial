---
title: How I Stopped Recalculating the Same MAX(date) Subquery on Redshift
date: '2026-08-05'
source: https://dev.to/maithreyan11/how-i-stopped-recalculating-the-same-maxdate-subquery-on-redshift-j50
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-06-28-our-sql-server-loop-kept-writing-the-previous-rows-value]]'
- '[[2026-03-09-making-sense-of-sql-from-joins-to-window-functions]]'
status: unread
---

> **TL;DR:** A subquery that looked perfectly fine on its own was quietly running dozens of times a day across our Redshift pipeline. Here's the story of how I found it, why it hurt specifically on Redshift, and the fix that made it…

## What’s new and why it matters
A subquery that looked perfectly fine on its own was quietly running dozens of times a day across our Redshift pipeline. Here's the story of how I found it, why it hurt specifically on Redshift, and the fix that made it a non-issue. The setup I had a query that needed the most recent record for a given entity — a fairly common pattern: SELECT * FROM events WHERE event_date = ( SELECT MAX ( event_date ) FROM events e2 WHERE e2 . entity_id = events . entity_id ); This is a correlated subquery — the inner SELECT references the outer query's row ( e2.entity_id = events.entity_id ), so it can't jus…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maithreyan11/how-i-stopped-recalculating-the-same-maxdate-subquery-on-redshift-j50

## Related notes
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-06-28-our-sql-server-loop-kept-writing-the-previous-rows-value]]
- [[2026-03-09-making-sense-of-sql-from-joins-to-window-functions]]
