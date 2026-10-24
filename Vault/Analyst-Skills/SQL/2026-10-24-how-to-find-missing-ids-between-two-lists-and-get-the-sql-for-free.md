---
title: How to find missing IDs between two lists (and get the SQL for free)
date: '2026-10-24'
source: https://dev.to/kdkumawat/how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free-3dpk
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
status: unread
---

> **TL;DR:** You have two exports. One is the source of truth (every paying customer in billing), the other is what you're auditing (customers synced to the CRM). The question is always the same: which IDs are in the first list but m…

## What’s new and why it matters
You have two exports. One is the source of truth (every paying customer in billing), the other is what you're auditing (customers synced to the CRM). The question is always the same: which IDs are in the first list but missing from the second? Here are three ways to answer it, depending on where the data lives. 1. Both lists are already in the database Use an anti-join. NOT EXISTS is the safe default because it behaves correctly when the other side contains NULL s ( NOT IN does not): SELECT b . customer_id FROM billing b WHERE NOT EXISTS ( SELECT 1 FROM crm c WHERE c . customer_id = b . custom…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kdkumawat/how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free-3dpk

## Related notes
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
