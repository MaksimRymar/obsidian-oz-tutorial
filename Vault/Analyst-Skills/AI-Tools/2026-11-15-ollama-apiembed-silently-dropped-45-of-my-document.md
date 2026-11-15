---
title: Ollama /api/embed Silently Dropped 45% of My Document
date: '2026-11-15'
source: https://dev.to/acemeridian/ollama-apiembed-silently-dropped-45-of-my-document-4en
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-10-ollama-numctx-truncated-287-of-400-prompts-and-never-told-me]]'
status: unread
---

> **TL;DR:** On a machine without a GPU, Ollama 0.40.14 loaded qwen3-embedding:0.6b with a 4,096-token context, and /api/embed cut my 7,510-token document down to 4,095 tokens with no error, no warning and no flag in the response. Se…

## What’s new and why it matters
On a machine without a GPU, Ollama 0.40.14 loaded qwen3-embedding:0.6b with a 4,096-token context, and /api/embed cut my 7,510-token document down to 4,095 tokens with no error, no warning and no flag in the response. Send "truncate": false so an overlong input fails with HTTP 400, and split documents into chunks of about 2,000 characters before you embed them. This story was written with the assistance of an AI writing program. Every number below comes from one run on an 8-core Linux box with no GPU: Ollama 0.40.14, qwen3-embedding:0.6b (Q8_0, 1,024 dimensions) and Python 3.14.4 calling the H…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/acemeridian/ollama-apiembed-silently-dropped-45-of-my-document-4en

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-10-ollama-numctx-truncated-287-of-400-prompts-and-never-told-me]]
