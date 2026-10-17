---
title: I Added a Fourth Shard in Python and 75% of the Keys Moved
date: '2026-10-17'
source: https://dev.to/realdev9868/i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved-2b7o
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-07-consistent-hashing-how-distributed-systems-partition-data]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]'
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
status: unread
---

> **TL;DR:** Every sharding answer starts the same way. Hash the key, take it modulo the number of shards, done. It works right up to the day someone says "we need one more shard." Then it breaks, and it breaks badly: almost every ke…

## What’s new and why it matters
Every sharding answer starts the same way. Hash the key, take it modulo the number of shards, done. It works right up to the day someone says "we need one more shard." Then it breaks, and it breaks badly: almost every key lands on a different machine than it did yesterday. You can say that in an interview, but it lands better if you have watched it happen. So I wrote a short Python script, used 100,000 fake keys like user:0 and user:1 , and counted. I hash with md5, because Python's built-in hash() for strings changes between runs and would make the numbers useless. The code blocks in this pos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/realdev9868/i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved-2b7o

## Related notes
- [[2026-09-07-consistent-hashing-how-distributed-systems-partition-data]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
