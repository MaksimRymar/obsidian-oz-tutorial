---
title: 'def recall(query, k=8, alpha=0.6):'
date: '2026-10-18'
source: https://dev.to/nindhita/def-recallquery-k8-alpha06-1085
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-04-07-postgresql-explain-analyze-reading-query-plans-like-a-pro]]'
- '[[2026-05-19-stop-writing-ugly-sql-a-developers-guide-to-clean-readable-queries]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
- '[[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]'
- '[[2026-05-02-rivian-data-engineering-interview-questions-full-de-prep-guide]]'
status: unread
---

> **TL;DR:** python def recall(query, k=8, alpha=0.6): qvec = embed(query) rows = conn.execute(""" SELECT m.id, m.content, m.embedding, bm25(memories_fts) AS rank FROM memories_fts JOIN memories m ON m.id = memories_fts.rowid WHERE m…

## What’s new and why it matters
python def recall(query, k=8, alpha=0.6): qvec = embed(query) rows = conn.execute(""" SELECT m.id, m.content, m.embedding, bm25(memories_fts) AS rank FROM memories_fts JOIN memories m ON m.id = memories_fts.rowid WHERE memories_fts MATCH ? ORDER BY rank LIMIT 50 """, (query,)).fetchall() scored = [] for id_, content, blob, rank in rows: vec = struct.unpack(f"<{len(blob)//4}f", blob) dot = sum(a*b for a,b in zip(qvec, vec)) cosine = dot / (math.sqrt(sum(a*a for a in qvec)) * math.sqrt(sum(b*b for b in vec))) scored.append((alpha * (1/(1+rank)) + (1-alpha)* --- ### 🤖 Author Attribution & Transpa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nindhita/def-recallquery-k8-alpha06-1085

## Related notes
- [[2026-04-07-postgresql-explain-analyze-reading-query-plans-like-a-pro]]
- [[2026-05-19-stop-writing-ugly-sql-a-developers-guide-to-clean-readable-queries]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
- [[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]
- [[2026-05-02-rivian-data-engineering-interview-questions-full-de-prep-guide]]
