---
title: From Local Docker Stack to a Working RAG API with Ollama, Qdrant, and Mistral
date: '2026-09-02'
source: https://dev.to/danielioni/from-local-docker-stack-to-a-working-rag-api-with-ollama-qdrant-and-mistral-1bl3
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-30-how-to-serve-mistral-medium-35-128b-without-running-out-of-gpu-memory]]'
- '[[2026-07-13-model-context-protocol-explained-build-your-first-mcp-server-with-python-and-docker]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
- '[[2026-09-02-why-serverless-engineers-already-understand-containers]]'
status: unread
---

> **TL;DR:** Introduction In the first phase of the MyZubster AI project, we prepared a local development stack containing: A Python and Flask API Ollama running on Windows Mistral as the language model Qdrant as the vector database…

## What’s new and why it matters
Introduction In the first phase of the MyZubster AI project, we prepared a local development stack containing: A Python and Flask API Ollama running on Windows Mistral as the language model Qdrant as the vector database Open WebUI as the browser interface Docker Compose for orchestration The infrastructure was running, but the MyZubster application was not yet using it. We have now completed the next step: MyZubster has a working Retrieval-Augmented Generation API . The final workflow is: Question ↓ MyZubster Flask API ↓ Embedding with nomic-embed-text ↓ Semantic search in Qdrant ↓ Relevant ob…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danielioni/from-local-docker-stack-to-a-working-rag-api-with-ollama-qdrant-and-mistral-1bl3

## Related notes
- [[2026-04-30-how-to-serve-mistral-medium-35-128b-without-running-out-of-gpu-memory]]
- [[2026-07-13-model-context-protocol-explained-build-your-first-mcp-server-with-python-and-docker]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
- [[2026-09-02-why-serverless-engineers-already-understand-containers]]
