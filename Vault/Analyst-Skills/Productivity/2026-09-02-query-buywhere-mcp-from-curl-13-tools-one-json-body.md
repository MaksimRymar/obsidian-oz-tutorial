---
title: Query BuyWhere MCP from curl — 13 tools, one JSON body
date: '2026-09-02'
source: https://dev.to/buywhere/query-buywhere-mcp-from-curl-13-tools-one-json-body-2h6n
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#tool'
related:
- '[[2026-09-01-build-a-4k-monitor-price-watcher-for-singapore-with-buywhere-mcp]]'
- '[[2026-07-12-build-a-cross-border-price-comparison-agent-with-buywhere-langchain]]'
- '[[2026-08-09-nvidia-nooa-ai-agents-as-one-python-class]]'
- '[[2026-06-18-building-an-mcp-sql-tool-that-lets-llms-query-live-databases-with-wanaku]]'
- '[[2026-03-05-i-built-a-job-search-tool-that-pulls-directly-from-company-ats-systems-not-job-boards]]'
- '[[2026-04-20-i-built-an-mcp-server-for-my-crypto-trading-signal-api-heres-how-and-why]]'
status: unread
---

> **TL;DR:** Agents should not need an SDK to price-check a product. BuyWhere MCP is at https://api.buywhere.ai/mcp and answers JSON-RPC. One call curl -s https://api.buywhere.ai/mcp \ -H "Content-Type: application/json" \ -d '{"json…

## What’s new and why it matters
Agents should not need an SDK to price-check a product. BuyWhere MCP is at https://api.buywhere.ai/mcp and answers JSON-RPC. One call curl -s https://api.buywhere.ai/mcp \ -H "Content-Type: application/json" \ -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_products","arguments":{"query":"macbook air m4","country":"SG"}}}' Prices come back nested: price.amount + price.currency . Filter currency == SGD for Singapore. Flat price fields are a common client bug. Live listings: Smithery ( smithery.ai/servers/BuyWhere/buywhere-mcp ) and Glama ( glama.ai/mcp/servers/BuyWher…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/buywhere/query-buywhere-mcp-from-curl-13-tools-one-json-body-2h6n

## Related notes
- [[2026-09-01-build-a-4k-monitor-price-watcher-for-singapore-with-buywhere-mcp]]
- [[2026-07-12-build-a-cross-border-price-comparison-agent-with-buywhere-langchain]]
- [[2026-08-09-nvidia-nooa-ai-agents-as-one-python-class]]
- [[2026-06-18-building-an-mcp-sql-tool-that-lets-llms-query-live-databases-with-wanaku]]
- [[2026-03-05-i-built-a-job-search-tool-that-pulls-directly-from-company-ats-systems-not-job-boards]]
- [[2026-04-20-i-built-an-mcp-server-for-my-crypto-trading-signal-api-heres-how-and-why]]
