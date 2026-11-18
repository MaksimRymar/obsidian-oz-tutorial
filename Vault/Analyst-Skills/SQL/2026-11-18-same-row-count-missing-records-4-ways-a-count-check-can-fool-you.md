---
title: 'Same Row Count, Missing Records: 4 Ways a Count Check Can Fool You'
date: '2026-11-18'
source: https://dev.to/askkarenai/same-row-count-missing-records-4-ways-a-count-check-can-fool-you-4f34
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]'
status: unread
---

> **TL;DR:** A common check after a batch job is to compare two numbers: how many records went in, and how many came out. If they match, the job is marked healthy. That check is useful as an alarm. But it is not proof. Two lists can…

## What’s new and why it matters
A common check after a batch job is to compare two numbers: how many records went in, and how many came out. If they match, the job is marked healthy. That check is useful as an alarm. But it is not proof. Two lists can have the same length and still hold different records. A tiny made-up example The run was supposed to deliver four orders: Expected: A , B , C , D Found in the destination: A , A , C , E Count check: 4 expected, 4 found. Looks fine. Compare by ID instead: missing : B , D duplicate : A (written twice) unexpected : E (not part of this run) Three problems, and the count hid all of…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/askkarenai/same-row-count-missing-records-4-ways-a-count-check-can-fool-you-4f34

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]
