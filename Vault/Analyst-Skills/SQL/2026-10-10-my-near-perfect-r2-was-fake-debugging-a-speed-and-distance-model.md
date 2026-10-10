---
title: 'My Near-Perfect R2 Was Fake: Debugging a Speed and Distance Model'
date: '2026-10-10'
source: https://dev.to/ayush_pangaonkar/my-near-perfect-r2-was-fake-debugging-a-speed-and-distance-model-43mn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-04-i-pulled-100-used-car-listings-from-portugals-largest-marketplace-what-prices-actually-look-like]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** The result looked great: R2 of 0.9993 and a correlation of 0.9994 between speed and distance. The problem was that the data had no real relationship in it. What the script does Generates 1,000 random speed values (10 to…

## What’s new and why it matters
The result looked great: R2 of 0.9993 and a correlation of 0.9994 between speed and distance. The problem was that the data had no real relationship in it. What the script does Generates 1,000 random speed values (10 to 1,000) and 1,000 random distance values (100 to 10,000) independently with random.randint . Sorts both arrays ascending, separately. Pairs them by index into a DataFrame and saves speed_dist.csv . Splits 97/3 into train and test (970 and 30 rows). Fits a LinearRegression of distance on speed and reports R2 on the test set. How I caught it Speed and distance were generated indep…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ayush_pangaonkar/my-near-perfect-r2-was-fake-debugging-a-speed-and-distance-model-43mn

## Related notes
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-04-i-pulled-100-used-car-listings-from-portugals-largest-marketplace-what-prices-actually-look-like]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
