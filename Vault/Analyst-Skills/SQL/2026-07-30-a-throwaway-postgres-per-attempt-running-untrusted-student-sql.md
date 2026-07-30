---
title: 'A throwaway Postgres per attempt: running untrusted student SQL'
date: '2026-07-30'
source: https://dev.to/cursora/a-throwaway-postgres-per-attempt-running-untrusted-student-sql-36gj
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-07-12-sql-week-we-deleted-products-dropped-tables-and-found-out-which-supplier-was-sitting-on-the-most-stock]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
status: unread
---

> **TL;DR:** The requirement Students submit arbitrary SQL. It has to be safe. And it has to allow real DDL — because "design this schema and populate it" is most of what teaching databases consists of, and an exercise limited to SEL…

## What’s new and why it matters
The requirement Students submit arbitrary SQL. It has to be safe. And it has to allow real DDL — because "design this schema and populate it" is most of what teaching databases consists of, and an exercise limited to SELECT against a fixed fixture teaches a fraction of the subject. Two obvious designs, both rejected: An in-process SQL engine in the backend. Fast, no containers. Also means evaluating untrusted input inside the application process — a shape that has burned this codebase before, in a different feature, with a real RCE as the outcome. Not again. A shared teaching database with res…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cursora/a-throwaway-postgres-per-attempt-running-untrusted-student-sql-36gj

## Related notes
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-07-12-sql-week-we-deleted-products-dropped-tables-and-found-out-which-supplier-was-sitting-on-the-most-stock]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
