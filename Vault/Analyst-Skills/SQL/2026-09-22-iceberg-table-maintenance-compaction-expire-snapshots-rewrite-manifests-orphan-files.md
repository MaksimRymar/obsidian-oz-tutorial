---
title: 'Iceberg Table Maintenance: Compaction, Expire Snapshots, Rewrite Manifests
  & Orphan Files'
date: '2026-09-22'
source: https://dev.to/gowthampotureddi/iceberg-table-maintenance-compaction-expire-snapshots-rewrite-manifests-orphan-files-1kpn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-15-the-small-files-problem-compaction-optimize-file-sizing-across-engines]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
status: unread
---

> **TL;DR:** iceberg table maintenance is the set of housekeeping jobs that keep an Apache Iceberg table fast to read, cheap to store, and correct over time — because Iceberg never edits data in place. Every insert, update, delete, a…

## What’s new and why it matters
iceberg table maintenance is the set of housekeeping jobs that keep an Apache Iceberg table fast to read, cheap to store, and correct over time — because Iceberg never edits data in place. Every insert, update, delete, and MERGE writes brand-new files and commits a brand-new snapshot that layers on top of the old one. That immutable, snapshot-per-commit design is exactly what buys you atomic writes, time travel, and safe concurrent readers — and it is also exactly why a table left unattended slowly rots into thousands of tiny files, a mile-high stack of dead snapshots, and a metadata layer so…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/iceberg-table-maintenance-compaction-expire-snapshots-rewrite-manifests-orphan-files-1kpn

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-15-the-small-files-problem-compaction-optimize-file-sizing-across-engines]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
