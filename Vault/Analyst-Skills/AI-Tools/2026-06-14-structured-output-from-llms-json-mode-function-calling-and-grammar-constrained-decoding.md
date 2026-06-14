---
title: 'Structured output from LLMs: JSON mode, function calling, and grammar-constrained
  decoding'
date: '2026-06-14'
source: https://dev.to/tech_nuggets/structured-output-from-llms-json-mode-function-calling-and-grammar-constrained-decoding-355d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-04-14-claude-api-tool-use-in-production-retry-logic-token-budgets-error-handling]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-05-tool-use-api-design-for-llms-5-patterns-that-prevent-agent-loops-and-silent-failures]]'
status: unread
---

> **TL;DR:** Structured output from LLMs: JSON mode, function calling, and grammar-constrained decoding You deployed a chatbot that translates natural-language requests into API calls. A user says "book a table for four at 7pm tomorr…

## What’s new and why it matters
Structured output from LLMs: JSON mode, function calling, and grammar-constrained decoding You deployed a chatbot that translates natural-language requests into API calls. A user says "book a table for four at 7pm tomorrow." Your prompt asks the LLM to emit a JSON like {"restaurant": string, "party_size": int, "time": string, "date": string} . One time it returns {"restaurant": "Olive Garden", "party_size": 4, "time": "19:00", "date": "2026-06-15"} -- valid JSON, everything works. The next request for "dim sum Saturday noon" produces {"restaurant": "Dim Sum House", "party_size": 2, "time": "12…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tech_nuggets/structured-output-from-llms-json-mode-function-calling-and-grammar-constrained-decoding-355d

## Related notes
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-04-14-claude-api-tool-use-in-production-retry-logic-token-budgets-error-handling]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-05-tool-use-api-design-for-llms-5-patterns-that-prevent-agent-loops-and-silent-failures]]
