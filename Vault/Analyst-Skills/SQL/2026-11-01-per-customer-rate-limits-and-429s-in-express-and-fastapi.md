---
title: Per-customer rate limits and 429s in Express and FastAPI
date: '2026-11-01'
source: https://dev.to/superlede/per-customer-rate-limits-and-429s-in-express-and-fastapi-1ib0
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
status: unread
---

> **TL;DR:** Most rate limiting tutorials limit by IP address. That's the right tool for a login form, and the wrong one for an API that customers pay for. A customer's traffic can come from fifty servers behind fifty addresses, or f…

## What’s new and why it matters
Most rate limiting tutorials limit by IP address. That's the right tool for a login form, and the wrong one for an API that customers pay for. A customer's traffic can come from fifty servers behind fifty addresses, or from one office NAT shared with someone else's script. What you want to cap is the customer: "Acme gets 5 requests per second, however many keys or machines they use." This post builds that in Express and in FastAPI with nothing but the framework, then covers the 429 response and the parts that tend to go wrong: ordering, retries and running more than one process. A token bucket…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/superlede/per-customer-rate-limits-and-429s-in-express-and-fastapi-1ib0

## Related notes
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
