---
title: Creating a simple local RAG system
date: '2026-03-29'
source: https://dev.to/utak3r/creating-a-simple-local-rag-system-4d99
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]'
- '[[2026-03-09-specialized-chatbot-using-rag]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-16-how-to-extract-text-from-pdf-in-python-2026]]'
status: unread
---

> **TL;DR:** We'll build a simple RAG system using local only models. We will not use LangChain, which is introducing many bloated dependencies, is much slower than direct Transformers usage, is not error-free and its documentation i…

## What’s new and why it matters
We'll build a simple RAG system using local only models. We will not use LangChain, which is introducing many bloated dependencies, is much slower than direct Transformers usage, is not error-free and its documentation is mostly misleading. We'll use only bare Transformers functions for that. As a vector database for storing our embeddings from document, we'll use Faiss , which is really efficient in similarity search. Note it sits in RAM, not on a disk and is very fast. What is a RAG? Retrieval-Augmented Generation (RAG) is an AI framework that improves Large Language Model (LLM) accuracy by…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/utak3r/creating-a-simple-local-rag-system-4d99

## Related notes
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]
- [[2026-03-09-specialized-chatbot-using-rag]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-16-how-to-extract-text-from-pdf-in-python-2026]]
