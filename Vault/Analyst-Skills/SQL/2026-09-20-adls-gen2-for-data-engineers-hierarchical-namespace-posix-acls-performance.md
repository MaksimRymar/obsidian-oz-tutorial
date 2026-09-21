---
title: 'ADLS Gen2 for Data Engineers: Hierarchical Namespace, POSIX ACLs & Performance'
date: '2026-09-20'
source: https://dev.to/gowthampotureddi/adls-gen2-for-data-engineers-hierarchical-namespace-posix-acls-performance-25l1
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
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-24-amazon-athena-federated-queries-partition-projection-iceberg-ctas-cost-tuning]]'
- '[[2026-08-15-the-small-files-problem-compaction-optimize-file-sizing-across-engines]]'
- '[[2026-08-18-rbac-vs-abac-for-data-platforms-roles-attributes-policy-engines-opa-immuta-privacera]]'
- '[[2026-08-23-apache-hive-deep-dive-for-data-engineers-metastore-partitions-orc-tez-vs-mapreduce]]'
status: unread
---

> **TL;DR:** ADLS Gen2 — Azure Data Lake Storage Gen2 — is not a new storage service you provision alongside Blob storage. It is Blob storage, with one capability switched on at account-creation time: the hierarchical namespace . Fli…

## What’s new and why it matters
ADLS Gen2 — Azure Data Lake Storage Gen2 — is not a new storage service you provision alongside Blob storage. It is Blob storage, with one capability switched on at account-creation time: the hierarchical namespace . Flip that one flag and a flat bucket of objects whose names merely happen to contain slashes becomes a real filesystem with true directories, atomic renames, and per-file POSIX permissions. Leave it off and you have ordinary Blob storage. Everything an interviewer will drill you on — why a Spark job commits cleanly, why a mv of a billion-file directory is instant, how you grant on…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowthampotureddi/adls-gen2-for-data-engineers-hierarchical-namespace-posix-acls-performance-25l1

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-24-amazon-athena-federated-queries-partition-projection-iceberg-ctas-cost-tuning]]
- [[2026-08-15-the-small-files-problem-compaction-optimize-file-sizing-across-engines]]
- [[2026-08-18-rbac-vs-abac-for-data-platforms-roles-attributes-policy-engines-opa-immuta-privacera]]
- [[2026-08-23-apache-hive-deep-dive-for-data-engineers-metastore-partitions-orc-tez-vs-mapreduce]]
