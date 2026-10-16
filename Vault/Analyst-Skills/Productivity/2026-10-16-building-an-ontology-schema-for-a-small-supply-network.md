---
title: Building an Ontology Schema for a Small Supply Network
date: '2026-10-16'
source: https://dev.to/exploredataaiml/building-an-ontology-schema-for-a-small-supply-network-4jh0
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-11-i-almost-published-a-chart-saying-the-nifty-fell-51-in-2003-it-fell-16-here-is-the-bug]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** How I Defined Lanes, Shipments, and On-Time in One YAML Schema TL;DR I wanted one place that says what a shipment is, which lane it used, and what "on time" means, before any table or brief was allowed to invent a second…

## What’s new and why it matters
How I Defined Lanes, Shipments, and On-Time in One YAML Schema TL;DR I wanted one place that says what a shipment is, which lane it used, and what "on time" means, before any table or brief was allowed to invent a second meaning. LaneSchema is that place, as a personal experiment on a laptop. The ontology lives in schema/inland_network.yaml . The fact grain is Shipment . The dimensions are Node , Lane , Carrier , and Sku . The metrics I was willing to name are OnTime , FillPercent , DwellHours , and LateHours . A metric that points at a property the grain does not have dies in load_ontology wi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/exploredataaiml/building-an-ontology-schema-for-a-small-supply-network-4jh0

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-11-i-almost-published-a-chart-saying-the-nifty-fell-51-in-2003-it-fell-16-here-is-the-bug]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
