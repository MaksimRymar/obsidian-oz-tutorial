---
title: 79 human visitors in one day. It was two browsers.
date: '2026-11-22'
source: https://dev.to/samuelfmedeiros/79-human-visitors-in-one-day-it-was-two-browsers-4cl0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** Yesterday my dashboard printed this line: visitas humano 7d/30d: 182 / 220 Two hundred and twenty humans in 30 days. For a store with zero sales that felt like the answer was somewhere else: the copy, the price, the miss…

## What’s new and why it matters
Yesterday my dashboard printed this line: visitas humano 7d/30d: 182 / 220 Two hundred and twenty humans in 30 days. For a store with zero sales that felt like the answer was somewhere else: the copy, the price, the missing Pix. Then I counted people instead of requests. A hit is not a person The table is hits : one row per request, each labelled humano , bot , incerto or dono . "Humano" means the User-Agent looks like a browser. It does not mean a person, and it does not mean a new person. The query I should have been running from day one: select count ( distinct visitor_id ) from hits where…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/samuelfmedeiros/79-human-visitors-in-one-day-it-was-two-browsers-4cl0

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
