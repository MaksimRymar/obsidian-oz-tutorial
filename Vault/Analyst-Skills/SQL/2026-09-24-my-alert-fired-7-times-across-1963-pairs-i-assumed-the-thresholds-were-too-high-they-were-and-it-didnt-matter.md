---
title: My alert fired 7 times across 1963 pairs. I assumed the thresholds were too
  high. They were, and it didn't matter
date: '2026-09-24'
source: https://dev.to/juanauriti/my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-3n70
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** I shipped an alert that tells users when their score drops. Then I checked how often it had actually fired. 7 times, across 1963 consecutive-report pairs. A fire rate of 0.36%. An alert that almost never fires and a syst…

## What’s new and why it matters
I shipped an alert that tells users when their score drops. Then I checked how often it had actually fired. 7 times, across 1963 consecutive-report pairs. A fire rate of 0.36%. An alert that almost never fires and a system where almost nothing goes wrong produce exactly the same dashboard. There is no way to tell them apart by looking at the alert. Where the thresholds came from Two conditions, both had to hold: total score dropped by >= 5 points AND at least one category dropped by >= 3 points I would like to tell you those numbers came from an analysis. They came from me, in an afternoon, re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/juanauriti/my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-3n70

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
