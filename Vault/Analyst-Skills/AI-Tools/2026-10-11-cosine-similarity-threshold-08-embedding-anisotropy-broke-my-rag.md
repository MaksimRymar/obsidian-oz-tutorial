---
title: 'Cosine Similarity Threshold 0.8: Embedding Anisotropy Broke My RAG'
date: '2026-10-11'
source: https://dev.to/ji_ai/cosine-similarity-threshold-08-embedding-anisotropy-broke-my-rag-p29
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** My RAG bot had exactly one safety rule: if the best chunk scores below 0.8 cosine similarity, answer "I don't know." That cosine similarity threshold ran for months without complaint. Then I swapped the embedding model,…

## What’s new and why it matters
My RAG bot had exactly one safety rule: if the best chunk scores below 0.8 cosine similarity, answer "I don't know." That cosine similarity threshold ran for months without complaint. Then I swapped the embedding model, redeployed, and the bot said "I don't know" to everything. Including "how do I reset my password," which has its own dedicated doc page. Nothing crashed. No errors. Retrieval still returned the right chunk at rank 1. My gate just threw it away, every single time. The worst part: when I went digging, I found the old setup had been broken too. In the other direction. TL;DR A cosi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ji_ai/cosine-similarity-threshold-08-embedding-anisotropy-broke-my-rag-p29

## Related notes
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
