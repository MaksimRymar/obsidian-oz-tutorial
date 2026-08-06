---
title: 731 words or 2,042? Why an aggregate's population belongs in the view, not
  the query string
date: '2026-08-05'
source: https://dev.to/kynth/731-words-or-2042-why-an-aggregates-population-belongs-in-the-view-not-the-query-string-4i7o
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
status: unread
---

> **TL;DR:** I maintain a corpus of agent instruction files scraped from public repos — AGENTS.md , CLAUDE.md , Cursor rules and friends — and last week I added the page answering "what actually goes in a CLAUDE.md," counted rather t…

## What’s new and why it matters
I maintain a corpus of agent instruction files scraped from public repos — AGENTS.md , CLAUDE.md , Cursor rules and friends — and last week I added the page answering "what actually goes in a CLAUDE.md," counted rather than recommended. The first thing that fell out was two different answers to median length : basis files median words share with runnable commands every CLAUDE.md 775 2,042 34.2% repo-root CLAUDE.md only 201 731 79.6% Both are correct. The 574 non-root files — the per-package ones sitting in packages/api/CLAUDE.md — have a median of 2,276 words, which is the opposite of what I'd…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kynth/731-words-or-2042-why-an-aggregates-population-belongs-in-the-view-not-the-query-string-4i7o

## Related notes
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
