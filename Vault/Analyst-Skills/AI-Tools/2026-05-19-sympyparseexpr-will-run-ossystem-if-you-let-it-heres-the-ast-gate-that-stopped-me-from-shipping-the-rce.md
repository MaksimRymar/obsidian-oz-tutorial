---
title: sympy.parse_expr will run os.system if you let it. Here's the AST gate that
  stopped me from shipping the RCE.
date: '2026-05-19'
source: https://dev.to/kyb8801/sympyparseexpr-will-run-ossystem-if-you-let-it-heres-the-ast-gate-that-stopped-me-from-1nbe
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
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-05-19-your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** sympy.parse_expr will run os.system if you let it. Here's the AST gate that stopped me from shipping the RCE. I was building an MCP server that accepts a measurement formula as a string from an LLM, parses it with sympy,…

## What’s new and why it matters
sympy.parse_expr will run os.system if you let it. Here's the AST gate that stopped me from shipping the RCE. I was building an MCP server that accepts a measurement formula as a string from an LLM, parses it with sympy, and evaluates it via Monte Carlo. Five minutes of integration. Thirteen tests. Twelve passed. The thirteenth was a safety test. The formula it passed was: " __import__( ' os ' ).system( ' echo PWNED ' ) " The test expected a ValueError . Instead I got a test failure message and the string PWNED printed to my terminal. Let me spell that out. sympy.parse_expr , with the default…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kyb8801/sympyparseexpr-will-run-ossystem-if-you-let-it-heres-the-ast-gate-that-stopped-me-from-1nbe

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-05-19-your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
