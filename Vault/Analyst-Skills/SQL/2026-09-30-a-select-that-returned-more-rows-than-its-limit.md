---
title: A SELECT that returned more rows than its LIMIT
date: '2026-09-30'
source: https://dev.to/alphanumericentity/a-select-that-returned-more-rows-than-its-limit-42kl
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-08-30-vanna-aivanna-has-been-archived-since-march---whats-actually-frozen-what-isnt-and-your-four-real-options]]'
status: unread
---

> **TL;DR:** A scheduled job in one of our services started crashing every few days with this: TypeError: Cannot read properties of undefined (reading 'id') Inside a for..of over the rows of a query. Not on the first row, not on ever…

## What’s new and why it matters
A scheduled job in one of our services started crashing every few days with this: TypeError: Cannot read properties of undefined (reading 'id') Inside a for..of over the rows of a query. Not on the first row, not on every run, and never reproducible locally. The other clue turned up in a log line from the same job, which prints how many pending records it picked up. The query has LIMIT 500 . The log said pendingTotal: 534 . Another run said 813. A SELECT with a LIMIT of 500 returning 813 rows is the kind of thing that makes you go back and read your own SQL four times. The SQL was fine. So was…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/alphanumericentity/a-select-that-returned-more-rows-than-its-limit-42kl

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-08-30-vanna-aivanna-has-been-archived-since-march---whats-actually-frozen-what-isnt-and-your-four-real-options]]
