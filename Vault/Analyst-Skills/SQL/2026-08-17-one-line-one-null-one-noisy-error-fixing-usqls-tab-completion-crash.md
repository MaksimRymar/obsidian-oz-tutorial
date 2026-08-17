---
title: 'One Line, One NULL, One Noisy Error: Fixing usql''s Tab Completion Crash'
date: '2026-08-17'
source: https://dev.to/gouranga-das-khulna/one-line-one-null-one-noisy-error-fixing-usqls-tab-completion-crash-3fmn
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** Not every open-source contribution needs a saga. Sometimes the whole story is: hit an annoying error, find the one missing COALESCE , ship a one-line diff, done. This is one of those — a small bug in usql , the universal…

## What’s new and why it matters
Not every open-source contribution needs a saga. Sometimes the whole story is: hit an annoying error, find the one missing COALESCE , ship a one-line diff, done. This is one of those — a small bug in usql , the universal command-line SQL client, that turned into a satisfying little fix with a slightly bumpy landing. The bug: tab completion that complains before it works While using usql against PostgreSQL, hitting Tab for autocompletion threw this at me every single time: Error getting selectables sql: Scan error on column index 6, name "routine_definition": converting NULL to string is unsupp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gouranga-das-khulna/one-line-one-null-one-noisy-error-fixing-usqls-tab-completion-crash-3fmn

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
