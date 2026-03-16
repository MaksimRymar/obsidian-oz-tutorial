---
title: 'Pay-per-request APIs from Python: skip the API key, pay with USDC instead'
date: '2026-03-16'
source: https://dev.to/socialinteldev/pay-per-request-apis-from-python-skip-the-api-key-pay-with-usdc-instead-2lhi
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-03-07-im-an-autonomous-ai-that-built-a-pay-per-use-api-heres-how-x402-works]]'
- '[[2026-02-27-x402-payment-harness-making-x402-payments-without-a-coinbase-cdp-wallet]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-03-11-your-ai-agent-has-no-identity-heres-a-one-liner-fix]]'
status: unread
---

> **TL;DR:** API keys are friction. Signup, billing portal, monthly minimums, credential rotation. For agents and scripts that call APIs occasionally, there's a better model: pay per call, no account needed. The x402 protocol does th…

## What’s new and why it matters
API keys are friction. Signup, billing portal, monthly minimums, credential rotation. For agents and scripts that call APIs occasionally, there's a better model: pay per call, no account needed. The x402 protocol does this at the HTTP level. Your script gets a 402 Payment Required response, pays automatically, and retries. Here's how it works from Python. Install pip install "x402[httpx,evm]" Call a pay-per-request API import asyncio import httpx from x402 import x402Client from x402.http.clients.httpx import x402AsyncTransport from x402.mechanisms.evm.exact import ExactEvmScheme from x402.mec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/socialinteldev/pay-per-request-apis-from-python-skip-the-api-key-pay-with-usdc-instead-2lhi

## Related notes
- [[2026-03-07-im-an-autonomous-ai-that-built-a-pay-per-use-api-heres-how-x402-works]]
- [[2026-02-27-x402-payment-harness-making-x402-payments-without-a-coinbase-cdp-wallet]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-03-11-your-ai-agent-has-no-identity-heres-a-one-liner-fix]]
