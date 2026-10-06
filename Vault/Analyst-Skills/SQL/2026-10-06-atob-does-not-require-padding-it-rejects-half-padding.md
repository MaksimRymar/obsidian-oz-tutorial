---
title: atob() does not require padding. It rejects half-padding.
date: '2026-10-06'
source: https://dev.to/_4143d12ca219f32cb635/atob-does-not-require-padding-it-rejects-half-padding-11oe
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** A common claim about Base64 in the browser is that the input length must be a multiple of 4. It isn't. atob decodes unpadded input fine. What it rejects is something else. Here are all five cases, run: "YQ==" len % 4 = 0…

## What’s new and why it matters
A common claim about Base64 in the browser is that the input length must be a multiple of 4. It isn't. atob decodes unpadded input fine. What it rejects is something else. Here are all five cases, run: "YQ==" len % 4 = 0 -> "a" "YQ" len % 4 = 2 -> "a" <- no padding, still decodes "YWJjZGU" len % 4 = 3 -> "abcde" <- decodes "YWJjZ" len % 4 = 1 -> throws "YQ=" len % 4 = 3 -> throws <- half-padded So the rule has nothing to do with multiples of 4. Remainder 2 or 3 decodes without padding. The leftover bits are enough to reconstruct the bytes. Remainder 1 always fails. Six bits cannot encode a byt…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_4143d12ca219f32cb635/atob-does-not-require-padding-it-rejects-half-padding-11oe

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
