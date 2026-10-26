---
title: Your UUID Column Is 9x Bigger Than It Needs to Be
date: '2026-10-26'
source: https://dev.to/zhihu_wu_dea1d82af01a04d7/your-uuid-column-is-9x-bigger-than-it-needs-to-be-2omi
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
status: unread
---

> **TL;DR:** A UUID is 16 bytes. In a surprising number of schemas, it occupies 144 bytes — and the index copy occupies 144 more. That's not a rounding error. It's the difference between an index that fits in memory and one that does…

## What’s new and why it matters
A UUID is 16 bytes. In a surprising number of schemas, it occupies 144 bytes — and the index copy occupies 144 more. That's not a rounding error. It's the difference between an index that fits in memory and one that doesn't. The 16-byte value stored as 144 bytes If your ORM maps a UUID to VARCHAR(36) or CHAR(36) — extremely common, because the string form is what the API returns — MySQL with utf8mb4 reserves 36 × 4 = 144 bytes per value . Put an index on it and the index stores the same 144 bytes per entry again, plus row overhead. An 8 KB index page holds roughly: ~54 keys for CHAR(36) utf8mb…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zhihu_wu_dea1d82af01a04d7/your-uuid-column-is-9x-bigger-than-it-needs-to-be-2omi

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
