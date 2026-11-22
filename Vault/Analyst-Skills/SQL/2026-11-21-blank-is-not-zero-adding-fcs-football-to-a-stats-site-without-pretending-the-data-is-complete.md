---
title: 'Blank is not zero: adding FCS football to a stats site without pretending
  the data is complete'
date: '2026-11-21'
source: https://dev.to/pigskinlab/blank-is-not-zero-adding-fcs-football-to-a-stats-site-without-pretending-the-data-is-complete-4afk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#zendesk'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
status: unread
---

> **TL;DR:** I run Pigskin Lab, a football stats site where you ask questions in plain English. This week I added FCS, the second tier of Division I college football (North Dakota State, Montana, South Dakota State and about 125 othe…

## What’s new and why it matters
I run Pigskin Lab, a football stats site where you ask questions in plain English. This week I added FCS, the second tier of Division I college football (North Dakota State, Montana, South Dakota State and about 125 other schools). The hard part wasn't loading the data. It was being honest about what the data doesn't have. What the source actually has College data comes from the CollegeFootballData API. Before writing any UI I measured what it holds for FCS, season by season: Schedules and scores go back to 2004. Full box scores for FCS-vs-FCS games start in 2022. 2021 has only fragments. Befo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pigskinlab/blank-is-not-zero-adding-fcs-football-to-a-stats-site-without-pretending-the-data-is-complete-4afk

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
