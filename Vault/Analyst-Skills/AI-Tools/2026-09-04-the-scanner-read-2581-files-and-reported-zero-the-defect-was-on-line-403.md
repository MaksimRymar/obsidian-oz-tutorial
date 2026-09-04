---
title: The scanner read 2581 files and reported zero. The defect was on line 403.
date: '2026-09-04'
source: https://dev.to/mahirhir/the-scanner-read-2581-files-and-reported-zero-the-defect-was-on-line-403-1jk9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-13-detecting-sqlite-full-table-scans-in-nodejs]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
status: unread
---

> **TL;DR:** On 2026-09-04 I pointed a scanner at langchain-ai/langchain . Shallow clone of the default branch, HEAD 79cab2d , read only. It walked 2581 files and printed zero sites. Its own control had passed immediately before the…

## What’s new and why it matters
On 2026-09-04 I pointed a scanner at langchain-ai/langchain . Shallow clone of the default branch, HEAD 79cab2d , read only. It walked 2581 files and printed zero sites. Its own control had passed immediately before the run, with two positive fixtures seen and four negative fixtures clean, so the zero was a measurement rather than a crash. Then I opened one file by hand. libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py , line 403: def _should_interrupt ( self , tool_call , config , state , runtime ) -> bool : """ Return False if the `when` predicate rejects this tool call, Tr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mahirhir/the-scanner-read-2581-files-and-reported-zero-the-defect-was-on-line-403-1jk9

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-13-detecting-sqlite-full-table-scans-in-nodejs]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
