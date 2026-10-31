---
title: Modelling GTU's 4-backlog detain rule in 15 lines of Python
date: '2026-10-31'
source: https://dev.to/offpage_prince/modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python-32nc
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#support-analytics'
related:
- '[[2026-10-28-how-i-count-repeated-questions-across-44-gtu-exam-papers-and-what-broke]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-10-12-should-you-guess-on-the-bocconi-admission-test-a-short-python-simulation]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-13-detecting-sqlite-full-table-scans-in-nodejs]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
status: unread
---

> **TL;DR:** I keep seeing GTU (Gujarat Technological University) juniors panic about the "4 backlog" rule, and half of them count it wrong. The rule has one twist that makes it a nice little exercise in code. The rule A backlog is a…

## What’s new and why it matters
I keep seeing GTU (Gujarat Technological University) juniors panic about the "4 backlog" rule, and half of them count it wrong. The rule has one twist that makes it a nice little exercise in code. The rule A backlog is a subject with an FF grade (below 35 marks). Missing the exam also counts as not cleared. At any time you can carry at most 4 pending backlogs. More than 4 and you can be detained for one year. Backlogs from the semester just before your current one are not counted. That last line is the bug in most people's mental model. The code def detention_check ( current_sem : int , pendin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/offpage_prince/modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python-32nc

## Related notes
- [[2026-10-28-how-i-count-repeated-questions-across-44-gtu-exam-papers-and-what-broke]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-10-12-should-you-guess-on-the-bocconi-admission-test-a-short-python-simulation]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-13-detecting-sqlite-full-table-scans-in-nodejs]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
