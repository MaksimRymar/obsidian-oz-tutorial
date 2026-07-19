---
title: RAG Apps Don’t Fail at Generation. They Fail at Retrieval
date: '2026-07-19'
source: https://dev.to/justatalentedguy/rag-apps-dont-fail-at-generation-they-fail-at-retrieval-l8d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-15-give-your-chatbot-a-memory-in-google-colab-before-your-next-ai-interview]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-08-rag-in-production-the-chunking-and-retrieval-mistakes-everyone-makes]]'
- '[[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]'
status: unread
---

> **TL;DR:** Why My RAG App Uses BM25, Vectors, Parent-Child Chunks, and Chat Memory Together PROJECT REPOSITORY: Open Most RAG projects start with a very confident idea: “Let us split the PDF, embed the chunks, store them in a vecto…

## What’s new and why it matters
Why My RAG App Uses BM25, Vectors, Parent-Child Chunks, and Chat Memory Together PROJECT REPOSITORY: Open Most RAG projects start with a very confident idea: “Let us split the PDF, embed the chunks, store them in a vector database, and ask questions.” Beautiful. Elegant. Wrong often enough to be annoying. That was also my first idea while building Docflow , a multi-user document question-answering app where users upload PDFs/images and chat with their own files. The application processes documents, stores chunks in Qdrant, retrieves relevant context, and sends that context to an LLM. The first…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/justatalentedguy/rag-apps-dont-fail-at-generation-they-fail-at-retrieval-l8d

## Related notes
- [[2026-07-15-give-your-chatbot-a-memory-in-google-colab-before-your-next-ai-interview]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-08-rag-in-production-the-chunking-and-retrieval-mistakes-everyone-makes]]
- [[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]
