---
title: Keep the Regex Writer Until Shadow Receipts Match
date: '2026-09-03'
source: https://dev.to/datago_8008/keep-the-regex-writer-until-shadow-receipts-match-432h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** A regex parser should keep the production write path. An LLM extractor belongs in shadow until frozen fixtures agree. This article shows a local receipt harness for that cutover. The harness compares structured fields in…

## What’s new and why it matters
A regex parser should keep the production write path. An LLM extractor belongs in shadow until frozen fixtures agree. This article shows a local receipt harness for that cutover. The harness compares structured fields instead of fluent prose. It writes a receipt file a reviewer can diff. Promotion waits for a clean receipt, not a demo. The silent break regex never caused Regex extractors fail loudly when lines do not match. LLM extractors fail by inventing keys or dropping ids. They also smooth timestamps that later break joins. Downstream tickets then look complete while identifiers vanish. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datago_8008/keep-the-regex-writer-until-shadow-receipts-match-432h

## Related notes
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
