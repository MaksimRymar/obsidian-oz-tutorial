---
title: I built a tool that lets you query websites using SQL
date: '2026-05-20'
source: https://dev.to/michael_ozersky_9624310ec/i-built-a-tool-that-lets-you-query-websites-using-sql-5de
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]'
- '[[2026-05-07-python-tool-to-extract-and-analyze-web-page-text-in-seconds]]'
- '[[2026-03-28-drizzle-orm-has-a-free-api-sql-like-typescript-orm-with-zero-overhead]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]'
status: unread
---

> **TL;DR:** Have you ever wondered: Why can't I query a web page like I can query a DB? That question led me to start building https://SiteRows.com The idea is to expose web content as queryable datasets, so you can do things like:…

## What’s new and why it matters
Have you ever wondered: Why can't I query a web page like I can query a DB? That question led me to start building https://SiteRows.com The idea is to expose web content as queryable datasets, so you can do things like: URL: https://wikipedia.org SQL: select * from @a where text like '%English%' RESULT: A list of all links whose text contains "English" There is a front-end with a SQL-like object explorer, and there is an API to set up automation. Please feel free to visit SiteRows and let me know what you think. https://SiteRows.com

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michael_ozersky_9624310ec/i-built-a-tool-that-lets-you-query-websites-using-sql-5de

## Related notes
- [[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]
- [[2026-05-07-python-tool-to-extract-and-analyze-web-page-text-in-seconds]]
- [[2026-03-28-drizzle-orm-has-a-free-api-sql-like-typescript-orm-with-zero-overhead]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]
