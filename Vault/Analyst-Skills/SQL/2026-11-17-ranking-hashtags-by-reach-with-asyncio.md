---
title: Ranking Hashtags by Reach with Asyncio
date: '2026-11-17'
source: https://dev.to/jinyoung_byun_afc6ea20f1c/ranking-hashtags-by-reach-with-asyncio-4of5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-10-14-how-to-turn-google-maps-scraper-output-into-a-scored-local-seo-lead-list]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** Ranking Hashtags by Reach with Asyncio I maintain a ranked table of the hashtags in my niche, sorted by the median play count of their recent posts, with a post-count column next to it so I can tell a real signal from th…

## What’s new and why it matters
Ranking Hashtags by Reach with Asyncio I maintain a ranked table of the hashtags in my niche, sorted by the median play count of their recent posts, with a post-count column next to it so I can tell a real signal from three lucky videos. I regenerate it on demand in about the time of the slowest handful of HTTP requests, not the sum of all of them. The ranking is the useful part. A hashtag with 4M posts and a median in the hundreds is a landfill. A hashtag with 60k posts and a median in the tens of thousands is where my content should go. You cannot eyeball this from the Instagram app, and you…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jinyoung_byun_afc6ea20f1c/ranking-hashtags-by-reach-with-asyncio-4of5

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-10-14-how-to-turn-google-maps-scraper-output-into-a-scored-local-seo-lead-list]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
