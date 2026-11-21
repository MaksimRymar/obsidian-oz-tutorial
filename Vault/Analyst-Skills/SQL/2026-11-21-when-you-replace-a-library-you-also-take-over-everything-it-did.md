---
title: When you replace a library, you also take over everything it did
date: '2026-11-21'
source: https://dev.to/alkhatibdev/when-you-replace-a-library-you-also-take-over-everything-it-did-mbh
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** DPOLens is an open-source MCP server that gives AI assistants the text of privacy law. Its search runs on the CPU, so it needs no GPU. The usual way to run an embedding model in Python is sentence-transformers . DPOLens…

## What’s new and why it matters
DPOLens is an open-source MCP server that gives AI assistants the text of privacy law. Its search runs on the CPU, so it needs no GPU. The usual way to run an embedding model in Python is sentence-transformers . DPOLens doesn't use it: with PyTorch's CPU build it installs about 1 GB, against about 200 MB for ONNX Runtime , the tokenizers library and NumPy. So DPOLens calls the model through ONNX Runtime directly, and does the tokenising and pooling itself, in about forty lines. Those forty lines did their job. What they didn't do was what the library does without being asked. When a new instan…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/alkhatibdev/when-you-replace-a-library-you-also-take-over-everything-it-did-mbh

## Related notes
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
