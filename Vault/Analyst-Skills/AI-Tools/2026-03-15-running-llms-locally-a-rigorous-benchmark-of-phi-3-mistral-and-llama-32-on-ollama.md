---
title: 'Running LLMs Locally: A Rigorous Benchmark of Phi-3, Mistral, and Llama 3.2
  on Ollama'
date: '2026-03-15'
source: https://dev.to/gurjeet333/running-llms-locally-a-rigorous-benchmark-of-phi-3-mistral-and-llama-32-on-ollama-2289
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-09-5-prompt-engineering-patterns-that-actually-work-in-production]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-02-23-your-mac-is-now-a-personal-doctor-analyzing-5-years-of-healthkit-data-locally-with-llama-3-mlx]]'
status: unread
---

> **TL;DR:** Abstract This report presents a comprehensive evaluation of three small language models (SLMs) – Llama 3.2 (3B), Phi-3 mini, and Mistral 7B – running locally via Ollama. A FastAPI-based benchmarking framework was develop…

## What’s new and why it matters
Abstract This report presents a comprehensive evaluation of three small language models (SLMs) – Llama 3.2 (3B), Phi-3 mini, and Mistral 7B – running locally via Ollama. A FastAPI-based benchmarking framework was developed to measure inference speed, resource consumption, and the models' ability to produce valid JSON outputs as defined by Pydantic schemas. A retry mechanism with reprompting was implemented to handle malformed responses. The models were tested on a suite of 30 prompts spanning general knowledge, mathematics, coding, reasoning, and creative writing. Results highlight trade-offs…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gurjeet333/running-llms-locally-a-rigorous-benchmark-of-phi-3-mistral-and-llama-32-on-ollama-2289

## Related notes
- [[2026-03-09-5-prompt-engineering-patterns-that-actually-work-in-production]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-02-23-your-mac-is-now-a-personal-doctor-analyzing-5-years-of-healthkit-data-locally-with-llama-3-mlx]]
