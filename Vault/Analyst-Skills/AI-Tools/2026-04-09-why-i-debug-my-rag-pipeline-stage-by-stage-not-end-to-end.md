---
title: Why I debug my RAG pipeline stage by stage, not end to end
date: '2026-04-09'
source: https://dev.to/coldoven/why-i-debug-my-rag-pipeline-stage-by-stage-not-end-to-end-1faf
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-02-24-rag-from-scratch-build-a-system-that-answers-questions-from-your-docs]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]'
status: unread
---

> **TL;DR:** The problem with end-to-end RAG eval I had a working document retrieval pipeline. Fixed-size chunking, TF-IDF embeddings, FAISS index. Recall@10 was 0.82 on SciFact. Good enough. Then I made one change: I swapped fixed-s…

## What’s new and why it matters
The problem with end-to-end RAG eval I had a working document retrieval pipeline. Fixed-size chunking, TF-IDF embeddings, FAISS index. Recall@10 was 0.82 on SciFact. Good enough. Then I made one change: I swapped fixed-size chunking for sentence-based chunking. Recall dropped to 0.68. My first instinct was to roll back. But I wanted to understand why . End-to-end eval only told me "retrieval is worse." It couldn't tell me which stage was responsible. The debugging approach I restructured the pipeline so each stage can be evaluated independently. The pipeline is expressed as a string feature ch…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/coldoven/why-i-debug-my-rag-pipeline-stage-by-stage-not-end-to-end-1faf

## Related notes
- [[2026-02-24-rag-from-scratch-build-a-system-that-answers-questions-from-your-docs]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]
