---
title: A website shared by more than three places is a chain, and 163 of the 318 we
  flagged had no brand field
date: '2026-10-07'
source: https://dev.to/daniel_pertu/a-website-shared-by-more-than-three-places-is-a-chain-and-163-of-the-318-we-flagged-had-no-brand-4nlp
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-09-01-four-traps-in-querying-179m-overture-maps-records-with-duckdb]]'
- '[[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Nakodo's business campaigns find local businesses to email: the kinds you choose, in the places you choose. They come from the Overture Maps places data, an open listing released each month, and the default setting is "I…

## What’s new and why it matters
Nakodo's business campaigns find local businesses to email: the kinds you choose, in the places you choose. They come from the Overture Maps places data, an open listing released each month, and the default setting is "Independent only", because a brand selling a booking system to independent pubs has nothing to say to a Wetherspoons branch. So something has to decide what a chain is. Overture has a brand field for exactly this. It is not enough, and I can show you by how much, with a query you can run yourself in about 20 seconds. The rule It is two conditions, and it is written on our public…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/daniel_pertu/a-website-shared-by-more-than-three-places-is-a-chain-and-163-of-the-318-we-flagged-had-no-brand-4nlp

## Related notes
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-09-01-four-traps-in-querying-179m-overture-maps-records-with-duckdb]]
- [[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
