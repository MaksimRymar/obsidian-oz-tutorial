---
title: ClickHouse IP Geolocation for Billions of Log Rows
date: '2026-11-18'
source: https://dev.to/abdullah_afzal/clickhouse-ip-geolocation-for-billions-of-log-rows-33bm
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Most ClickHouse IP geolocation tutorials turn each IP range into a CIDR block with a one-line XOR trick. On a commercial city database, that trick sizes 3 in 4 multi-address ranges wrong and claims almost 10x the address…

## What’s new and why it matters
Most ClickHouse IP geolocation tutorials turn each IP range into a CIDR block with a one-line XOR trick. On a commercial city database, that trick sizes 3 in 4 multi-address ranges wrong and claims almost 10x the addresses those ranges hold. Nothing throws. Your country and city columns just quietly pick up neighbours' answers. This walkthrough builds the exact version in plain ClickHouse SQL: one function that splits IPv4 and IPv6 ranges into CIDR blocks, an ip_trie dictionary that matched the vendor's own MMDB network for network, enrichment at insert time, and a daily refresh that swaps rel…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/abdullah_afzal/clickhouse-ip-geolocation-for-billions-of-log-rows-33bm

## Related notes
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
