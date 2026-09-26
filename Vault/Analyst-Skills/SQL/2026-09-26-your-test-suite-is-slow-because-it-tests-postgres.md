---
title: Your Test Suite Is Slow Because It Tests Postgres
date: '2026-09-26'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/your-test-suite-is-slow-because-it-tests-postgres-2k6o
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-24-how-to-connect-an-ai-assistant-to-your-sql-database-safely]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
status: unread
---

> **TL;DR:** I quit running the test suite on my laptop. Not deliberately. I just stopped typing the command, because by the time it finished I had lost the thread of whatever I was fixing. Standup would end, I would push, and wait f…

## What’s new and why it matters
I quit running the test suite on my laptop. Not deliberately. I just stopped typing the command, because by the time it finished I had lost the thread of whatever I was fixing. Standup would end, I would push, and wait for CI to tell me what I broke. That is the real cost of a slow suite: not the wall-clock time, but the gap between writing a line and knowing whether it works. Ours was slow for a boring reason. Every test opened its own connection, applied the migrations, and talked to a real Postgres instance. A test that checked whether an email address was normalized still paid for a connec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/your-test-suite-is-slow-because-it-tests-postgres-2k6o

## Related notes
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-24-how-to-connect-an-ai-assistant-to-your-sql-database-safely]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
