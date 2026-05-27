---
title: 'From parser combinators to hand-written TDOP: adopting sqlparser-rs at Readyset'
date: '2026-05-26'
source: https://dev.to/readyset/from-parser-combinators-to-hand-written-tdop-adopting-sqlparser-rs-at-readyset-22ml
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-20-why-our-generative-ai-powered-sql-assistant-struggled-with-real-world-database-schemas]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-03-11-what-is-snowflake-a-beginners-guide-to-the-cloud-data-warehouse-everyones-talking-about]]'
- '[[2026-04-12-every-ai-pitch-at-forbes-under-30-had-the-same-architecture-gap]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-04-23-from-0-to-100-github-stars-with-a-python-cli-spoiler-its-not-as-easy-as-they-say]]'
status: unread
---

> **TL;DR:** If you've ever wondered why a query that runs fine in Postgres fails silently in a caching layer, the answer is usually in the parser. Here's the story of how a customer's BETWEEN query led us to replace the parser we'd…

## What’s new and why it matters
If you've ever wondered why a query that runs fine in Postgres fails silently in a caching layer, the answer is usually in the parser. Here's the story of how a customer's BETWEEN query led us to replace the parser we'd shipped since day one, what we gained (4x throughput, 44% lower tail latency), and why the old approach was broken in ways that were hard to see.

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/readyset/from-parser-combinators-to-hand-written-tdop-adopting-sqlparser-rs-at-readyset-22ml

## Related notes
- [[2026-04-20-why-our-generative-ai-powered-sql-assistant-struggled-with-real-world-database-schemas]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-03-11-what-is-snowflake-a-beginners-guide-to-the-cloud-data-warehouse-everyones-talking-about]]
- [[2026-04-12-every-ai-pitch-at-forbes-under-30-had-the-same-architecture-gap]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-04-23-from-0-to-100-github-stars-with-a-python-cli-spoiler-its-not-as-easy-as-they-say]]
