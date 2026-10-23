---
title: PAM, BLOSUM and scoring matrices from 1,000 human mitochondrial genomes
date: '2026-10-22'
source: https://dev.to/bioseqdb/pam-blosum-and-scoring-matrices-from-1000-human-mitochondrial-genomes-o37
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
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** Two sequences can agree at most positions and still leave us with a few awkward decisions. Is a leucine opposite an isoleucine a reasonable match? Should an alignment insert a gap here, or accept three mismatches and kee…

## What’s new and why it matters
Two sequences can agree at most positions and still leave us with a few awkward decisions. Is a leucine opposite an isoleucine a reasonable match? Should an alignment insert a gap here, or accept three mismatches and keep going? A scoring scheme puts numbers on those choices, and changing the numbers can change the alignment you get. PAM and BLOSUM are families of substitution matrices for proteins . They describe how amino-acid pairs occur in aligned related sequences, relative to the pairs we would expect from their individual abundance. We will work through those counts, then use BioseqDB t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bioseqdb/pam-blosum-and-scoring-matrices-from-1000-human-mitochondrial-genomes-o37

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
