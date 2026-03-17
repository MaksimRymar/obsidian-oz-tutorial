---
title: 'SurrealDB: How I Deleted 70% of My Backend Code (Part 2)'
date: '2026-03-16'
source: https://dev.to/jakubb_ing/surrealdb-how-i-deleted-70-of-my-backend-code-part-2-238h
domain: SQL
relevance: 🔴
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]'
- '[[2026-03-15-surrealdb-the-one-size-fits-all-database-for-lazy-developers-part-1]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** Remember that "simple" Express server? We’ve all been there. You just want a user to be able to update their own profile. So you: Write an /api/update-profile endpoint. Validate the JWT (and pray the library doesn't have…

## What’s new and why it matters
Remember that "simple" Express server? We’ve all been there. You just want a user to be able to update their own profile. So you: Write an /api/update-profile endpoint. Validate the JWT (and pray the library doesn't have a new CVE). Fetch the data from the DB. Manually check if the user_id from the token matches the owner_id in the DB (because you don't want me changing your profile picture). Save it and send a 200 OK. Congratulations, you just wrote 50 lines of boilerplate that we’ve been writing since 2015. It’s 2026-we should be over this. As a freelancer and working with AI, I’ve realized…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jakubb_ing/surrealdb-how-i-deleted-70-of-my-backend-code-part-2-238h

## Related notes
- [[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]
- [[2026-03-15-surrealdb-the-one-size-fits-all-database-for-lazy-developers-part-1]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
