---
title: The latest() Bug That Silently Duplicated Transaction IDs in Production
date: '2026-04-20'
source: https://dev.to/fazghfr/the-latest-bug-that-silently-duplicated-transaction-ids-in-production-42ip
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-03-20-from-68-to-100-how-we-built-a-text-to-sql-system-that-gets-smarter-every-day]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-03-15-surrealdb-the-one-size-fits-all-database-for-lazy-developers-part-1]]'
status: unread
---

> **TL;DR:** TL;DR: Using Model::latest()->first() to get the "latest" record by ID is wrong. latest() orders by created_at , not by the value of your ID column. When two rows are inserted within the same second, both reads return th…

## What’s new and why it matters
TL;DR: Using Model::latest()->first() to get the "latest" record by ID is wrong. latest() orders by created_at , not by the value of your ID column. When two rows are inserted within the same second, both reads return the same record, and you get duplicate IDs. Background I built a simple sequential ID generator for transaction IDs. The logic was straightforward: fetch the latest record, read its code, increment the number, return the next one. $start = "XX00000001" ; $latest = Model :: latest () -> first (); if ( ! $latest || ! $latest -> code ) { return $start ; } $value = $latest -> code ;…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fazghfr/the-latest-bug-that-silently-duplicated-transaction-ids-in-production-42ip

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-03-20-from-68-to-100-how-we-built-a-text-to-sql-system-that-gets-smarter-every-day]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-03-15-surrealdb-the-one-size-fits-all-database-for-lazy-developers-part-1]]
