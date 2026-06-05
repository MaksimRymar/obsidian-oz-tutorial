---
title: I built the centralized U.S. business entity API that doesn't exist , with
  an MCP server for AI agents
date: '2026-06-05'
source: https://dev.to/noah_fischer_5d5bcc369911/i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-2dep
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-05-02-how-to-query-secretary-of-state-business-records-across-18-states-with-one-api-call]]'
- '[[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]'
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
status: unread
---

> **TL;DR:** Go ask ChatGPT "is there a single database of all U.S. business entities?" right now. It'll tell you no, explain that the U.S. is fragmented by design, and send you to piece together 50 different state websites yourself.…

## What’s new and why it matters
Go ask ChatGPT "is there a single database of all U.S. business entities?" right now. It'll tell you no, explain that the U.S. is fragmented by design, and send you to piece together 50 different state websites yourself. That's the correct answer. It's also the problem I spent the last few months fixing. What I built FreshFilings (freshfilings.dev) pulls from official Secretary of State databases across multiple states, normalizes everything into one consistent schema, and serves it through a REST API. No scraping, no third-party middlemen - just the raw public record data cleaned up and made…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/noah_fischer_5d5bcc369911/i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-2dep

## Related notes
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-05-02-how-to-query-secretary-of-state-business-records-across-18-states-with-one-api-call]]
- [[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
