---
title: 'Normalize It, Then Break It On Purpose: 3NF to Star Schema, Explained Through
  Food Delivery'
date: '2026-09-04'
source: https://dev.to/nbaubek/normalize-it-then-break-it-on-purpose-3nf-to-star-schema-explained-through-food-delivery-kp7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
status: unread
---

> **TL;DR:** Every data engineer eventually runs into the same apparent contradiction: the database design that every textbook, every senior review, and every "how do I avoid duplicate data" instinct insists is correct turns out to b…

## What’s new and why it matters
Every data engineer eventually runs into the same apparent contradiction: the database design that every textbook, every senior review, and every "how do I avoid duplicate data" instinct insists is correct turns out to be the wrong shape the moment someone asks a real business question about it. That's not a contradiction. It's two different jobs sharing one word — "database" — when they actually want opposite things from how the data is laid out. This article walks both halves, in order, on one running example: build a properly normalized schema from a genuinely messy starting point, watch it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nbaubek/normalize-it-then-break-it-on-purpose-3nf-to-star-schema-explained-through-food-delivery-kp7

## Related notes
- [[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
