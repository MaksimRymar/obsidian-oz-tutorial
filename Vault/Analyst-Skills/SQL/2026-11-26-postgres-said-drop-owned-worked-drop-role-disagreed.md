---
title: Postgres said DROP OWNED worked. DROP ROLE disagreed.
date: '2026-11-26'
source: https://dev.to/niyigbodo/postgres-said-drop-owned-worked-drop-role-disagreed-60e
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tableau'
- '#tutorial'
related:
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-11-25-how-to-find-duplicate-rows-in-mysql-before-they-break-your-app]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-07-09-how-do-i-answer-what-did-my-data-look-like-last-month-in-postgres]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
status: unread
---

> **TL;DR:** I'm the founder of Kilimanjaro , and this week's note is from the unglamorous end of the job: tearing down. When a customer project is removed, we remove the database role that belonged to it. It is the last step of a cl…

## What’s new and why it matters
I'm the founder of Kilimanjaro , and this week's note is from the unglamorous end of the job: tearing down. When a customer project is removed, we remove the database role that belonged to it. It is the last step of a cleanup that is supposed to leave nothing behind. One day that last step started failing, and it kept failing in a way that made no sense for about an afternoon. The symptom The cleanup did what every Postgres guide says to do: DROP OWNED BY r ; DROP ROLE r ; DROP OWNED reported success. DROP ROLE then failed, every time: ERROR: role "r" cannot be dropped because some objects dep…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/niyigbodo/postgres-said-drop-owned-worked-drop-role-disagreed-60e

## Related notes
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-11-25-how-to-find-duplicate-rows-in-mysql-before-they-break-your-app]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-07-09-how-do-i-answer-what-did-my-data-look-like-last-month-in-postgres]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
