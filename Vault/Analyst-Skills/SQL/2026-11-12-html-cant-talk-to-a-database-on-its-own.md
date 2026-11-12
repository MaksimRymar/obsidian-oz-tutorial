---
title: HTML Can’t Talk to a Database on Its Own
date: '2026-11-12'
source: https://dev.to/zoymusk/html-cant-talk-to-a-database-on-its-own-545i
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]'
- '[[2026-11-11-your-query-is-slow-and-you-have-never-read-a-query-plan]]'
- '[[2026-11-09-my-first-project-one-website-for-hotels-movies-and-flights]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
- '[[2026-09-16-the-data-modeling-concepts-nobody-mentions-after-star-schema-101]]'
status: unread
---

> **TL;DR:** When we built our holiday planner in uni, we had a simple plan. HTML for the pages, SQL for the data. Connect the two and done. It took us days to realize it doesn’t work like that. Here’s what nobody told us. HTML can’t…

## What’s new and why it matters
When we built our holiday planner in uni, we had a simple plan. HTML for the pages, SQL for the data. Connect the two and done. It took us days to realize it doesn’t work like that. Here’s what nobody told us. HTML can’t talk to a database. A webpage only shows things. It can’t ask a database for anything. There has to be something in the middle that takes the request, asks the database, and sends the answer back to the page. We didn’t know that. So we kept trying to connect them directly, and nothing worked. No mentor, no one to ask, just us and Google. We searched, tried things, broke things…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zoymusk/html-cant-talk-to-a-database-on-its-own-545i

## Related notes
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]
- [[2026-11-11-your-query-is-slow-and-you-have-never-read-a-query-plan]]
- [[2026-11-09-my-first-project-one-website-for-hotels-movies-and-flights]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
- [[2026-09-16-the-data-modeling-concepts-nobody-mentions-after-star-schema-101]]
