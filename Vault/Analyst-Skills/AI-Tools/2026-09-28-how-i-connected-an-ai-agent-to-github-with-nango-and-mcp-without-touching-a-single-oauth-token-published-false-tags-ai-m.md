---
title: 'How I connected an AI agent to GitHub with Nango and MCP (without touching
  a single OAuth token) published: false tags: ai, mcp, python, tutorial'
date: '2026-09-28'
source: https://dev.to/sravya_dangeti/how-i-connected-an-ai-agent-to-github-with-nango-and-mcp-without-touching-a-single-oauth-token-14j1
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
status: unread
---

> **TL;DR:** Every time you connect an AI agent to an external API, you inherit the boring, risky part: OAuth flows, token storage, token refresh, and making sure nothing leaks. In this tutorial I built a small MCP server in Python t…

## What’s new and why it matters
Every time you connect an AI agent to an external API, you inherit the boring, risky part: OAuth flows, token storage, token refresh, and making sure nothing leaks. In this tutorial I built a small MCP server in Python that exposes GitHub to any MCP client, where my code never sees a GitHub token . Nango handles the auth. My server only knows a Nango secret key and a connection ID. Code: https://github.com/sravya520/nango-github-mcp How it works MCP client -> my MCP server (Python) -> Nango proxy (adds GitHub auth) -> GitHub API The server exposes three tools: Tool What it does list_my_repos L…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sravya_dangeti/how-i-connected-an-ai-agent-to-github-with-nango-and-mcp-without-touching-a-single-oauth-token-14j1

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
