---
title: 'Prompt Injection and PII: How I Built Guardrails in LangGraph'
date: '2026-10-25'
source: https://dev.to/alexresch/prompt-injection-and-pii-how-i-built-guardrails-in-langgraph-2bi6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-10-12-prepaste----building-it-again-but-better]]'
- '[[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]'
status: unread
---

> **TL;DR:** This article is for AI developers who want to protect their RAG system against prompt injection and leaks of personal data (PII). There are three problems. First, personal data like email addresses or IBANs is sent to th…

## What’s new and why it matters
This article is for AI developers who want to protect their RAG system against prompt injection and leaks of personal data (PII). There are three problems. First, personal data like email addresses or IBANs is sent to the model provider and ends up in your logs. Second, a malicious prompt can make the model ignore its instructions, reveal its system prompt or, in agents with tools, run actions you never wanted, like deleting a database. Third, users can ask your app for harmful help, like writing malware. Below, I show how I built an input guardrail in LangGraph for all three and how I test it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alexresch/prompt-injection-and-pii-how-i-built-guardrails-in-langgraph-2bi6

## Related notes
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-10-12-prepaste----building-it-again-but-better]]
- [[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]
