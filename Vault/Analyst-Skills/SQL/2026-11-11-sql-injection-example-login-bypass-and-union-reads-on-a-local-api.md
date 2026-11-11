---
title: 'SQL injection example: login bypass and UNION reads on a local API'
date: '2026-11-11'
source: https://dev.to/excessionlabs/sql-injection-example-login-bypass-and-union-reads-on-a-local-api-2084
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-25-an-empty-column-is-not-an-external-caller]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** SQL injection example: login bypass and UNION reads on a local API SQL injection happens when an application pastes request data into the text of a query, so the input can change what the query means. In a small sqlite3-…

## What’s new and why it matters
SQL injection example: login bypass and UNION reads on a local API SQL injection happens when an application pastes request data into the text of a query, so the input can change what the query means. In a small sqlite3-backed HTTP API we bypassed a login with one crafted username and read every user's password hash through a search parameter. Binding values with placeholders stopped both attacks, but a sort parameter still leaked data until we replaced it with an allowlist. This is a scripted Python and curl experiment with downloadable source and responses. No AI agent or model ran the test.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/excessionlabs/sql-injection-example-login-bypass-and-union-reads-on-a-local-api-2084

## Related notes
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-25-an-empty-column-is-not-an-external-caller]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
