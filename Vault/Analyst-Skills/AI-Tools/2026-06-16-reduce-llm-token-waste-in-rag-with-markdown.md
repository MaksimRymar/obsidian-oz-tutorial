---
title: Reduce LLM Token Waste in RAG with Markdown
date: '2026-06-16'
source: https://dev.to/alterlab/reduce-llm-token-waste-in-rag-with-markdown-1jck
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-30-agentic-web-browsing-workflows-with-python-and-playwright]]'
- '[[2026-06-05-stop-scraping-google-html-do-this-for-your-ai-agents-instead]]'
- '[[2026-05-15-build-a-rag-pipeline-that-actually-reads-the-web]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-06-03-scraping-authenticated-web-pages-for-rag-pipelines]]'
- '[[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]'
status: unread
---

> **TL;DR:** TL;DR Feeding raw HTML to Large Language Models wastes tokens on markup, scripts, and styling. By rendering dynamic web pages in a headless browser and converting the final DOM to clean Markdown, you reduce token consump…

## What’s new and why it matters
TL;DR Feeding raw HTML to Large Language Models wastes tokens on markup, scripts, and styling. By rendering dynamic web pages in a headless browser and converting the final DOM to clean Markdown, you reduce token consumption by up to 90% while preserving semantic structure and improving retrieval accuracy in RAG pipelines. The Problem: LLMs, Context Windows, and the HTML Tax Building Retrieval-Augmented Generation (RAG) pipelines over web data introduces a specific data engineering problem. The web is built on HTML. Large Language Models operate on tokens. When you pass raw HTML to an embeddin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alterlab/reduce-llm-token-waste-in-rag-with-markdown-1jck

## Related notes
- [[2026-05-30-agentic-web-browsing-workflows-with-python-and-playwright]]
- [[2026-06-05-stop-scraping-google-html-do-this-for-your-ai-agents-instead]]
- [[2026-05-15-build-a-rag-pipeline-that-actually-reads-the-web]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-06-03-scraping-authenticated-web-pages-for-rag-pipelines]]
- [[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]
