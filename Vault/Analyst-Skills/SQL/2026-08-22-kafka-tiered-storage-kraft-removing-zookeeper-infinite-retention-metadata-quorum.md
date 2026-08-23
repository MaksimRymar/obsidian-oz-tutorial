---
title: 'Kafka Tiered Storage & KRaft: Removing ZooKeeper, Infinite Retention & Metadata
  Quorum'
date: '2026-08-22'
source: https://dev.to/gowthampotureddi/kafka-tiered-storage-kraft-removing-zookeeper-infinite-retention-metadata-quorum-4kig
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-22-kafka-consumer-group-internals-rebalance-protocols-static-membership-cooperative-sticky]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** Kafka KRaft is the single biggest change to how Apache Kafka is operated since the project shipped, and it is the topic that separates engineers who learned Kafka in 2018 from the ones running it in 2026 — because the en…

## What’s new and why it matters
Kafka KRaft is the single biggest change to how Apache Kafka is operated since the project shipped, and it is the topic that separates engineers who learned Kafka in 2018 from the ones running it in 2026 — because the entire control plane was rebuilt. For a decade every Kafka cluster shipped with a second distributed system bolted to its side: an Apache ZooKeeper ensemble that stored broker registrations, topic configs, partition assignments, ACLs, and — most critically — elected the controller. That split-brain-prone dependency was the source of a disproportionate share of production incident…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowthampotureddi/kafka-tiered-storage-kraft-removing-zookeeper-infinite-retention-metadata-quorum-4kig

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-22-kafka-consumer-group-internals-rebalance-protocols-static-membership-cooperative-sticky]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
