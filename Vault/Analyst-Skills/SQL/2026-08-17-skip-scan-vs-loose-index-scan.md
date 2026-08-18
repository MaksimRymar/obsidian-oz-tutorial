---
title: Skip Scan vs. Loose Index Scan
date: '2026-08-17'
source: https://dev.to/franckpachot/skip-scan-vs-loose-index-scan-51pn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
status: unread
---

> **TL;DR:** Both optimizations avoid ( skip ) reading ( scan ) irrelevant leaf pages by repositioning ( seek ) via a fresh index descent instead of scanning sequentially. This surface similarity explains why people often used "skip…

## What’s new and why it matters
Both optimizations avoid ( skip ) reading ( scan ) irrelevant leaf pages by repositioning ( seek ) via a fresh index descent instead of scanning sequentially. This surface similarity explains why people often used "skip scan" and "loose index scan" interchangeably before the distinction was clearly defined. For example, I wrote YugabyteDB Skip Scan aka Loose Index Scan on compound index in 2022 because the two concepts were not clearly distinguished in the PostgreSQL wiki at that time. PostgreSQL implemented neither of those features yet, and YugabyteDB implemented both with the same hybrid sc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/skip-scan-vs-loose-index-scan-51pn

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
