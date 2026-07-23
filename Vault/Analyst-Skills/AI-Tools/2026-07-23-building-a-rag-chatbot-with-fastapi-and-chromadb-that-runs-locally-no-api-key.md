---
title: Building a RAG Chatbot with FastAPI and ChromaDB (that runs locally, no API
  key)
date: '2026-07-23'
source: https://dev.to/deaw_ai/building-a-rag-chatbot-with-fastapi-and-chromadb-that-runs-locally-no-api-key-36aj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-07-01-ql-ai-database-solutions-building-a-text-to-sql-pipeline-you-can-actually-run]]'
- '[[2026-05-26-meter-llm-usage-like-anthropic-tokens-models-weekly-and-monthly-caps]]'
- '[[2026-06-10-i-built-a-production-rag-system-on-my-m1-mac-for-0]]'
status: unread
---

> **TL;DR:** Everyone wants a chatbot that can answer questions from their own documents — a company handbook, a contract, a research paper. The technique behind this is called RAG (Retrieval-Augmented Generation) . I build productio…

## What’s new and why it matters
Everyone wants a chatbot that can answer questions from their own documents — a company handbook, a contract, a research paper. The technique behind this is called RAG (Retrieval-Augmented Generation) . I build production RAG and LLM systems for a living, and I kept re-wiring the same foundation on every project. So I cleaned it up into a small, open-source starter. This post walks through how RAG actually works, the design decisions that matter, and how you can run the whole thing for free — no API key required. At the end there's a link to the full open-source repo you can clone and run in m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/deaw_ai/building-a-rag-chatbot-with-fastapi-and-chromadb-that-runs-locally-no-api-key-36aj

## Related notes
- [[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-07-01-ql-ai-database-solutions-building-a-text-to-sql-pipeline-you-can-actually-run]]
- [[2026-05-26-meter-llm-usage-like-anthropic-tokens-models-weekly-and-monthly-caps]]
- [[2026-06-10-i-built-a-production-rag-system-on-my-m1-mac-for-0]]
