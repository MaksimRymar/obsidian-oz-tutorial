---
title: Stop detecting AI content. Start signing it at the source
date: '2026-10-06'
source: https://dev.to/indiainfranotes/stop-detecting-ai-content-start-signing-it-at-the-source-2575
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]'
- '[[2026-09-02-i-generate-every-blog-cover-with-headless-chrome-and-a-bit-of-css-no-design-tool]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
status: unread
---

> **TL;DR:** Every few months someone ships a new way to detect AI-generated text or images, and every few months someone else shows how to strip it. Paraphrase the text, crop or re-encode the image, and the hidden signal gets weaker…

## What’s new and why it matters
Every few months someone ships a new way to detect AI-generated text or images, and every few months someone else shows how to strip it. Paraphrase the text, crop or re-encode the image, and the hidden signal gets weaker or disappears. Detection is a cat and mouse game, and the mouse only needs to win once. There is a calmer way to think about this. Instead of asking "can I prove this was made by AI?", ask "can I prove where this came from and that nobody changed it since?" That is provenance, and it is a much easier problem to engineer. Watermark vs provenance Watermark / detector Signed prov…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/indiainfranotes/stop-detecting-ai-content-start-signing-it-at-the-source-2575

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]
- [[2026-09-02-i-generate-every-blog-cover-with-headless-chrome-and-a-bit-of-css-no-design-tool]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
