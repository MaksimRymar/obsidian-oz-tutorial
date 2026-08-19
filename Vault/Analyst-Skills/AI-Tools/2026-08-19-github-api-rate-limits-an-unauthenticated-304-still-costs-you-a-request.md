---
title: 'GitHub API Rate Limits: an Unauthenticated 304 Still Costs You a Request'
date: '2026-08-19'
source: https://dev.to/0012303/github-api-rate-limits-an-unauthenticated-304-still-costs-you-a-request-3af7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-10-you-cannot-predict-what-an-llm-call-will-cost-before-you-make-it]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
status: unread
---

> **TL;DR:** No token. One IP. July 29, 2026: GET /repos/python/cpython 200 5996 B remaining 32 -> 31 + If-None-Match (no Authorization header) 304 0 B remaining 31 -> 30 + If-None-Match 304 0 B remaining 30 -> 29 + If-None-Match 304…

## What’s new and why it matters
No token. One IP. July 29, 2026: GET /repos/python/cpython 200 5996 B remaining 32 -> 31 + If-None-Match (no Authorization header) 304 0 B remaining 31 -> 30 + If-None-Match 304 0 B remaining 30 -> 29 + If-None-Match 304 0 B remaining 29 -> 28 Three conditional requests. Three 304 Not Modified . Zero bytes of body across all three. Three requests gone from a bucket of 60 per hour. I opened the terminal to write the opposite post. The short version: if you call the GitHub REST API without an Authorization header, an If-None-Match request that comes back 304 still decrements x-ratelimit-remainin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0012303/github-api-rate-limits-an-unauthenticated-304-still-costs-you-a-request-3af7

## Related notes
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-10-you-cannot-predict-what-an-llm-call-will-cost-before-you-make-it]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
