---
title: 'Scraping Adversarial Municipal Portals: A Permit Pipeline That Knows When
  It Failed'
date: '2026-09-16'
source: https://dev.to/andrewmaury/scraping-adversarial-municipal-portals-a-permit-pipeline-that-knows-when-it-failed-pie
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-07-04-how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Most California cities publish their building permits, and almost none of them publish the same way. The San Francisco Peninsula alone runs six vendor portal products (eTRAKiT, on at least two incompatible forks; Tyler T…

## What’s new and why it matters
Most California cities publish their building permits, and almost none of them publish the same way. The San Francisco Peninsula alone runs six vendor portal products (eTRAKiT, on at least two incompatible forks; Tyler Technologies' EnerGov and Civic Self Service; Accela; Clariti; PermitStack), one municipal open-data feed, and one city whose only complete record is a monthly report it posts as a document. Searches are login-gated, JavaScript-rendered, and driven by ASP.NET postbacks that rewrite the form under you. Two of the portals answer only to a real browser. A blocked request is loud: i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/andrewmaury/scraping-adversarial-municipal-portals-a-permit-pipeline-that-knows-when-it-failed-pie

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-07-04-how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
