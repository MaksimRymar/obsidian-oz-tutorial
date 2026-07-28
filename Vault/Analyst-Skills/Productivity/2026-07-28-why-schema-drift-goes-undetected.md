---
title: Why schema drift goes undetected
date: '2026-07-28'
source: https://dev.to/eggletric/why-schema-drift-goes-undetected-j2
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#productivity'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
status: unread
---

> **TL;DR:** Here is a scenario from a project in its third year of operation. Migrations are managed properly. CI is green. validate passes. Then an error shows up in production only. The production table has a column that doesn't e…

## What’s new and why it matters
Here is a scenario from a project in its third year of operation. Migrations are managed properly. CI is green. validate passes. Then an error shows up in production only. The production table has a column that doesn't exist anywhere else. Nobody remembers who added it, when, or why. There is no migration file for it. The important part is not the mystery column. It's that this divergence passed every check the team had . Nothing was broken. The tooling worked exactly as designed — and, as designed, it does not detect this class of problem. This post is about why. Code and databases are not sy…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/eggletric/why-schema-drift-goes-undetected-j2

## Related notes
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
