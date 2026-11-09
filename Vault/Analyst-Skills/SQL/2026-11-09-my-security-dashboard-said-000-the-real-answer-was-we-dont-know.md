---
title: My security dashboard said $0.00. The real answer was "we don't know."
date: '2026-11-09'
source: https://dev.to/varun_poojari/my-security-dashboard-said-000-the-real-answer-was-we-dont-know-34bi
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-10-06-we-caught-our-own-ai-security-scanner-making-up-vulnerabilities]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
status: unread
---

> **TL;DR:** My last post was about a scanner that made up findings. This one is about something smaller and much more common: a tool showing you a number or label that is technically true and still sends you the wrong way. I found t…

## What’s new and why it matters
My last post was about a scanner that made up findings. This one is about something smaller and much more common: a tool showing you a number or label that is technically true and still sends you the wrong way. I found three of these while testing secfoo, the open-source (MIT) CLI I work on at RakFort. It hands AI coding agents a fixed security brief and tracks their findings and cost. None of the three crashed anything or failed a test. Each one just told the user something confidently wrong. 1. "$0.00" when the answer was "we don't know" secfoo tracks what each AI scan costs. Some agents rep…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/varun_poojari/my-security-dashboard-said-000-the-real-answer-was-we-dont-know-34bi

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-10-06-we-caught-our-own-ai-security-scanner-making-up-vulnerabilities]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
