---
title: 'HyperLogLog: Count Billions of Uniques in Kilobytes'
date: '2026-09-07'
source: https://dev.to/gowthampotureddi/hyperloglog-count-billions-of-uniques-in-kilobytes-5ae
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** hyperloglog is the probabilistic data structure that answers "how many distinct things did we see?" over billions of events using a few kilobytes of memory and roughly one percent of error — and it is the single algorith…

## What’s new and why it matters
hyperloglog is the probabilistic data structure that answers "how many distinct things did we see?" over billions of events using a few kilobytes of memory and roughly one percent of error — and it is the single algorithm that separates engineers who can count uniques at scale from engineers who keep crashing a job because they tried to hold every distinct value in a set. The question sounds trivial: how many unique visitors hit the site today, how many distinct IPs probed the firewall, how many distinct search terms appeared this hour. The exact answer requires remembering every distinct valu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/hyperloglog-count-billions-of-uniques-in-kilobytes-5ae

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
