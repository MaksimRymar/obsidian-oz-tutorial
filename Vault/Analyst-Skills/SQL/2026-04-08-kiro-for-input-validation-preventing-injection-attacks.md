---
title: 'Kiro for Input Validation: Preventing Injection Attacks'
date: '2026-04-08'
source: https://dev.to/pedronino/kiro-for-input-validation-preventing-injection-attacks-2di9
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]'
status: unread
---

> **TL;DR:** This is an idea that I've had for some time, and never had the chance to complete. But, It's 2026 and I still see examples and some production code that concatenates user input straight into SQL queries. No parameterizat…

## What’s new and why it matters
This is an idea that I've had for some time, and never had the chance to complete. But, It's 2026 and I still see examples and some production code that concatenates user input straight into SQL queries. No parameterization. No escaping. Just vibes and prayers. I decided to take three of the most common injection vulnerabilities, right from the textbook: SQL injection, cross-site scripting, and command injection, then write the worst possible version of each in Python (pun intended), and then ask Kiro to fix them. Here's what happened, in my own experience. The Setup I built three small Flask…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pedronino/kiro-for-input-validation-preventing-injection-attacks-2di9

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]
