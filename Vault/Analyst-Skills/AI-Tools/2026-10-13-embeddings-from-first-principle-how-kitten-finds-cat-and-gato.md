---
title: 'Embeddings from First Principle : How “Kitten” finds “Cat” (and “Gato”)'
date: '2026-10-13'
source: https://dev.to/ritwick_biswas_479398f747/embeddings-from-first-principle-how-kitten-finds-cat-and-gato-2nd0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-09-openai-voyage-cohere-or-open-weights-picking-an-embedding-model-in-2026]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-10-11-cosine-similarity-threshold-08-embedding-anisotropy-broke-my-rag]]'
- '[[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]'
status: unread
---

> **TL;DR:** RAG series · Part 1 TL;DR An embedding is a list of numbers that represents the meaning of a piece of text. Similar meanings → nearby vectors. Cosine similarity measures how close they are. This is the "R" (retrieval) in…

## What’s new and why it matters
RAG series · Part 1 TL;DR An embedding is a list of numbers that represents the meaning of a piece of text. Similar meanings → nearby vectors. Cosine similarity measures how close they are. This is the "R" (retrieval) in RAG. Pick the wrong embedding model and your RAG fails silently in other languages. The problem Computers can't compare meanings. They can only compare numbers. Keyword search fails on: Synonyms: "kitten" vs "cat" Translations: "cat" vs "gato" So we need a way to turn meaning into numbers . The idea An embedding model turns any text into a fixed-size list of numbers (a vector…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ritwick_biswas_479398f747/embeddings-from-first-principle-how-kitten-finds-cat-and-gato-2nd0

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-09-openai-voyage-cohere-or-open-weights-picking-an-embedding-model-in-2026]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-10-11-cosine-similarity-threshold-08-embedding-anisotropy-broke-my-rag]]
- [[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]
