---
title: 'Confluent Tableflow & Kafka-to-Iceberg: Streaming Topics Straight Into the
  Lakehouse'
date: '2026-08-29'
source: https://dev.to/gowthampotureddi/confluent-tableflow-kafka-to-iceberg-streaming-topics-straight-into-the-lakehouse-1ko9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-08-06-avro-vs-protobuf-vs-json-schema-serialization-schema-evolution-for-streaming]]'
- '[[2026-08-27-semi-structured-data-at-scale-jsonvariant-nested-repeated-fields-across-dialects]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Confluent Tableflow is the feature that finally lets a Kafka topic stop being a stream you have to drain into the lakehouse with a bespoke pipeline and start being an Apache Iceberg table you can simply query — materiali…

## What’s new and why it matters
Confluent Tableflow is the feature that finally lets a Kafka topic stop being a stream you have to drain into the lakehouse with a bespoke pipeline and start being an Apache Iceberg table you can simply query — materialized continuously from the topic, its schema taken straight from the registry, its small files compacted and its rows deduplicated without a single job you wrote yourself. The hard problem was never "get the bytes out of Kafka"; it was everything that came after. A topic is an append-only log tuned for low-latency consumers reading a few records at a time, and a lakehouse table…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/confluent-tableflow-kafka-to-iceberg-streaming-topics-straight-into-the-lakehouse-1ko9

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-08-06-avro-vs-protobuf-vs-json-schema-serialization-schema-evolution-for-streaming]]
- [[2026-08-27-semi-structured-data-at-scale-jsonvariant-nested-repeated-fields-across-dialects]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
