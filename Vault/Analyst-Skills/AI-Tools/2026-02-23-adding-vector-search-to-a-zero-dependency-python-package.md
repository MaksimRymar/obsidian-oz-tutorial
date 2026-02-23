---
title: Adding Vector Search to a Zero-Dependency Python Package
date: '2026-02-23'
source: https://dev.to/xiaonaai/adding-vector-search-to-a-zero-dependency-python-package-fb7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]'
- '[[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]'
- '[[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]'
- '[[2026-02-22-applying-mvc-architecture-in-python-building-an-automated-certificate-generator]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
status: unread
---

> **TL;DR:** Last week I built agent-memory , a lightweight memory system for AI agents. It started with TF-IDF keyword search — simple, fast, zero dependencies. But keyword search has limits. "What did I learn about deployment?" won…

## What’s new and why it matters
Last week I built agent-memory , a lightweight memory system for AI agents. It started with TF-IDF keyword search — simple, fast, zero dependencies. But keyword search has limits. "What did I learn about deployment?" won't match "Figured out how to ship to production." I needed semantic search. The obvious answer: sentence-transformers + numpy. But that's 2GB of PyTorch for a 672-line package. The whole point was zero dependencies. Here's how I added vector search without adding a single dependency. The Architecture User configures embedding API (optional) ↓ add() → text → HTTP POST /v1/embedd…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/xiaonaai/adding-vector-search-to-a-zero-dependency-python-package-fb7

## Related notes
- [[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]
- [[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]
- [[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]
- [[2026-02-22-applying-mvc-architecture-in-python-building-an-automated-certificate-generator]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
