---
title: How I Aggregated 13 Public CTI Feeds into a Free Threat Intelligence Platform
date: '2026-07-16'
source: https://dev.to/david_moya_5b6cdd8b4e1219/how-i-aggregated-13-public-cti-feeds-into-a-free-threat-intelligence-platform-g65
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-05-01-i-built-an-osint-aggregator-that-queries-5-threat-intel-sources-in-one-command]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]'
status: unread
---

> **TL;DR:** TL;DR: I built a free threat intelligence aggregation platform by pulling from 13 public CTI feeds (MISP, OTX, Abuse.ch, etc.), normalizing the data into a common schema, and exposing it through a REST API. This post wal…

## What’s new and why it matters
TL;DR: I built a free threat intelligence aggregation platform by pulling from 13 public CTI feeds (MISP, OTX, Abuse.ch, etc.), normalizing the data into a common schema, and exposing it through a REST API. This post walks through the architecture, the normalization pipeline, deduplication strategy, and a few gotchas I hit along the way. Why Build Another Threat Intel Tool? Commercial threat intelligence platforms are expensive. Recorded Future, ThreatConnect, and Anomali are excellent products, but their price tags put them out of reach for small security teams, indie researchers, and hobbyis…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/david_moya_5b6cdd8b4e1219/how-i-aggregated-13-public-cti-feeds-into-a-free-threat-intelligence-platform-g65

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-05-01-i-built-an-osint-aggregator-that-queries-5-threat-intel-sources-in-one-command]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]
