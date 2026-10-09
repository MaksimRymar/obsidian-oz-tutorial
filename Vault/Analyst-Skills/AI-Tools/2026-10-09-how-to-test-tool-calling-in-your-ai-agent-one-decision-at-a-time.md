---
title: How to test tool calling in your AI agent, one decision at a time
date: '2026-10-09'
source: https://dev.to/sbhorus/how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time-2i64
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
status: unread
---

> **TL;DR:** Many agent bugs are not about bad prose. They are about bad tool calls. The agent picks the wrong tool. It sends a string where the schema wants an integer. It guesses a value the user never gave. It follows an instructi…

## What’s new and why it matters
Many agent bugs are not about bad prose. They are about bad tool calls. The agent picks the wrong tool. It sends a string where the schema wants an integer. It guesses a value the user never gave. It follows an instruction it found inside a web page. These bugs are easy to test if you test single decisions, not whole conversations. Here is a simple way, with three test cases you can copy. The idea: one case, one decision A tool-calling test case needs four things: The tools the agent may use, with JSON Schema parameters. The conversation so far, including any earlier tool calls and tool result…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sbhorus/how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time-2i64

## Related notes
- [[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
