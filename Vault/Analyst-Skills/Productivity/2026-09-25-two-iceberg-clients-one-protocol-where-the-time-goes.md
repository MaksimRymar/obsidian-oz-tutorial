---
title: 'Two Iceberg Clients, One Protocol: Where the Time Goes'
date: '2026-09-25'
source: https://dev.to/gde/two-iceberg-clients-one-protocol-where-the-time-goes-4g88
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-07-07-the-caller-heard-silence-for-two-seconds-before-the-agent-spoke]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** This article provides a step by step comparison of the Rust and Python clients for Apache Iceberg REST catalogs. It times both clients on the same operations against the same tables, then breaks one request down to see w…

## What’s new and why it matters
This article provides a step by step comparison of the Rust and Python clients for Apache Iceberg REST catalogs. It times both clients on the same operations against the same tables, then breaks one request down to see where the time goes. https://github.com/xbill9/lakehouse-iceberg-2026 What is this project trying to Do? Two Apache clients talk to the same catalogs: iceberg-catalog-rest 0.10.1 , the Rust client, built in release mode pyiceberg 0.12.0 , the Python client, on Python 3.14.7 They run against three catalogs: Apache Polaris 1.7.0 in Docker on the same machine, so there is no networ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gde/two-iceberg-clients-one-protocol-where-the-time-goes-4g88

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-07-07-the-caller-heard-silence-for-two-seconds-before-the-agent-spoke]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
