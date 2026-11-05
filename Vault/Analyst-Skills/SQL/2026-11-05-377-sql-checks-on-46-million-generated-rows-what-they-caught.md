---
title: '377 SQL checks on 4.6 million generated rows: what they caught'
date: '2026-11-05'
source: https://dev.to/generaterealdata/377-sql-checks-on-46-million-generated-rows-what-they-caught-5gkc
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-10-29-it-passed-every-constraint-it-was-still-wrong]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** In part 1 I showed the method: write every rule about your data as a sentence, then one SQL query that counts the rows breaking it. The rule holds when the query returns 0. I promised to run it at scale. So I did: 377 ch…

## What’s new and why it matters
In part 1 I showed the method: write every rule about your data as a sentence, then one SQL query that counts the rows breaking it. The rule holds when the query returns 0. I promised to run it at scale. So I did: 377 checks across 13 generated databases, 4,594,497 rows in total. Today every one of those queries returns 0. Getting there took several fixes, and this post covers the ones I'd never have found by looking at the data. The setup Thirteen databases, each generated from a schema plus rules, each with a checks.sql file holding one query per rule: Dataset Tables Rows Rules E-commerce da…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/generaterealdata/377-sql-checks-on-46-million-generated-rows-what-they-caught-5gkc

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-10-29-it-passed-every-constraint-it-was-still-wrong]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
