---
title: 'NEP: A Semantic Transform That Beats zstd by 12% on Ethereum JSON-RPC Data'
date: '2026-06-06'
source: https://dev.to/lbwasserman/nep-a-semantic-transform-that-beats-zstd-by-12-on-ethereum-json-rpc-data-3am5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** If you've ever looked at what Ethereum JSON-RPC responses actually contain, you'll notice most of the data is structured waste: hex strings that could be raw bytes, field names repeated thousands of times per block, addr…

## What’s new and why it matters
If you've ever looked at what Ethereum JSON-RPC responses actually contain, you'll notice most of the data is structured waste: hex strings that could be raw bytes, field names repeated thousands of times per block, addresses appearing dozens of times in full 42-character form. NEP (Neurop Encoding Protocol) is a deterministic 4-stage binary transform that cleans all of this up before zstd runs. The result: 12% better compression than plain zstd, 200/200 block wins, fully lossless. What it does Ethereum JSON → NEP encode → zstd → storage Ethereum JSON ← NEP decode ← zstd ← storage Four stages,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lbwasserman/nep-a-semantic-transform-that-beats-zstd-by-12-on-ethereum-json-rpc-data-3am5

## Related notes
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
