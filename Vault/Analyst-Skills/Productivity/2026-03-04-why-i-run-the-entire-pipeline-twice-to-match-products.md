---
title: Why I Run the Entire Pipeline Twice to Match Products
date: '2026-03-04'
source: https://dev.to/kingsleyonoh/why-i-run-the-entire-pipeline-twice-to-match-products-440e
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#productivity'
- '#tool'
related:
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
status: unread
---

> **TL;DR:** Why I Run the Entire Pipeline Twice to Match Products The pricing spreadsheet hit 4,162 rows and the retailer stopped updating it. Not because it was hard. Because it took 90 minutes every morning and the prices were wro…

## What’s new and why it matters
Why I Run the Entire Pipeline Twice to Match Products The pricing spreadsheet hit 4,162 rows and the retailer stopped updating it. Not because it was hard. Because it took 90 minutes every morning and the prices were wrong by the time he finished. The system I built to replace that process worked on the first deploy. Pulled supplier data, applied markup rules, synced to Shopify. Clean run. But 600 products had no supplier price attached. The logs showed them as "unmatched." Fifteen percent of the catalog, sitting in the store at stale prices. The first-pass matching was straightforward: take t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kingsleyonoh/why-i-run-the-entire-pipeline-twice-to-match-products-440e

## Related notes
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-03-01-sql-joins]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
