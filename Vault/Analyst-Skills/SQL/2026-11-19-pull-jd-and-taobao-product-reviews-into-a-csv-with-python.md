---
title: Pull JD and Taobao product reviews into a CSV with Python
date: '2026-11-19'
source: https://dev.to/qovia/pull-jd-and-taobao-product-reviews-into-a-csv-with-python-420g
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-11-05-search-wechat-official-account-articles-by-topic-in-python]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-11-03-small-guardrails-for-llm-calls-in-plain-python-injection-check-pii-masking-spend-cap-circuit-breaker-json-repair]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** I build Qovia, the API used in this post. The paging loop, CSV writer and rating summary are plain Python; they work with any source that returns the same review fields. The two HTTP paths below are Qovia's. If you are c…

## What’s new and why it matters
I build Qovia, the API used in this post. The paging loop, CSV writer and rating summary are plain Python; they work with any source that returns the same review fields. The two HTTP paths below are Qovia's. If you are comparing products, tracking a launch, or feeding reviews into a notebook, JD.com and Taobao/Tmall are the two marketplaces you will hit most often in China. Each site exposes reviews on its own product page, but the identifiers differ and the public pages are awkward to script against. This tutorial writes a small Python script that: pulls JD.com buyer reviews with GET /v1/raw/…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/qovia/pull-jd-and-taobao-product-reviews-into-a-csv-with-python-420g

## Related notes
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-11-05-search-wechat-official-account-articles-by-topic-in-python]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-11-03-small-guardrails-for-llm-calls-in-plain-python-injection-check-pii-masking-spend-cap-circuit-breaker-json-repair]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
