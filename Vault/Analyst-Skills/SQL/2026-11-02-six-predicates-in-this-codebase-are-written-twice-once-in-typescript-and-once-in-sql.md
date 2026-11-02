---
title: Six predicates in this codebase are written twice, once in TypeScript and once
  in SQL
date: '2026-11-02'
source: https://dev.to/daniel_pertu/six-predicates-in-this-codebase-are-written-twice-once-in-typescript-and-once-in-sql-600
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-10-04-pause-became-a-question-with-three-answers-so-we-wrote-the-rules-twice-and-only-one-copy-has-tests]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]'
- '[[2026-10-03-the-free-plan-searches-exactly-like-the-paid-one-and-hides-the-results-and-the-blurred-rows-are-fake-on-purpose]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
status: unread
---

> **TL;DR:** A campaign in Nakodo can be paused in three different ways: stop finding new creators, stop the email flow, or stop both. Nakodo can also pause a campaign itself, for instance when a Free account's month of contacts is u…

## What’s new and why it matters
A campaign in Nakodo can be paused in three different ways: stop finding new creators, stop the email flow, or stop both. Nakodo can also pause a campaign itself, for instance when a Free account's month of contacts is used up, and our pricing page states a couple of those cases, including that extra campaigns are paused rather than deleted when a plan gets smaller. From that one product idea comes a question the code has to answer in two completely different places. A React component renders a status dot and needs to know whether this campaign is still searching. A background job runs a query…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/six-predicates-in-this-codebase-are-written-twice-once-in-typescript-and-once-in-sql-600

## Related notes
- [[2026-10-04-pause-became-a-question-with-three-answers-so-we-wrote-the-rules-twice-and-only-one-copy-has-tests]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]
- [[2026-10-03-the-free-plan-searches-exactly-like-the-paid-one-and-hides-the-results-and-the-blurred-rows-are-fake-on-purpose]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
