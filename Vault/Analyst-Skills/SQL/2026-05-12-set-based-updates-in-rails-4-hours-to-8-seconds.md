---
title: 'Set-Based Updates in Rails: 4 Hours to 8 Seconds'
date: '2026-05-12'
source: https://dev.to/travelingwilbur/set-based-updates-in-rails-4-hours-to-8-seconds-dkd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
status: unread
---

> **TL;DR:** I once inherited a background job to deactivate stale users. In production, a job processing 50,000 users that should have taken a minute was taking over 4 hours, consuming 2GB of RAM, and frequently timing out. The culp…

## What’s new and why it matters
I once inherited a background job to deactivate stale users. In production, a job processing 50,000 users that should have taken a minute was taking over 4 hours, consuming 2GB of RAM, and frequently timing out. The culprit was a classic Rails performance pitfall: the N+1 update loop. The code looked innocent: # Find users whose last login was more than 90 days ago users_to_deactivate = User . where ( "last_login_at < ?" , 90 . days . ago ) users_to_deactivate . each do | user | # This runs one UPDATE query for every single user user . update ( active: false ) end This generates a flood of que…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/travelingwilbur/set-based-updates-in-rails-4-hours-to-8-seconds-dkd

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
