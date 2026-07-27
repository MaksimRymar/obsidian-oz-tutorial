---
title: Free Crypto KYT API — Enrich Sandbox, Sanction Checks, and Wallet Pre-Send
  Code
date: '2026-07-27'
source: https://dev.to/public_aml/free-crypto-kyt-api-enrich-sandbox-sanction-checks-and-wallet-pre-send-code-2lak
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
- '[[2026-02-27-json-to-python-complete-guide-to-dataclasses-pydantic-and-json-parsing]]'
- '[[2026-05-05-build-an-mcp-server-in-python-in-15-minutes]]'
- '[[2026-07-13-python-sdk-13-historical-trends-url-comparisons-and-slack-alerts-in-three-lines-each]]'
- '[[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]'
- '[[2026-03-20-pypi-api-discover-python-packages-in-any-domain-free-instant]]'
status: unread
---

> **TL;DR:** Free Crypto KYT API — Enrich Sandbox, Sanction Checks, and Wallet Pre-Send Code Interactive console + docs live at intelapi.publicaml.org . Same payload, same JSON your backend gets. This post turns that API into shippab…

## What’s new and why it matters
Free Crypto KYT API — Enrich Sandbox, Sanction Checks, and Wallet Pre-Send Code Interactive console + docs live at intelapi.publicaml.org . Same payload, same JSON your backend gets. This post turns that API into shippable code. Base URL: https://intelapi.publicaml.org Auth (public enrich path): none Chains: ETH , BTC , TRON , BSC Core: POST /v1/enrich curl -sS -X POST 'https://intelapi.publicaml.org/v1/enrich' \ -H 'Content-Type: application/json' \ -d '{ "addresses":[{"wallet_address":"0x67d40ee1a85bf4a4bb7ffae16de985e8427b6b45","chain":"ETH"}], "include":["aml_score","category"], "top_n":5…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/public_aml/free-crypto-kyt-api-enrich-sandbox-sanction-checks-and-wallet-pre-send-code-2lak

## Related notes
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
- [[2026-02-27-json-to-python-complete-guide-to-dataclasses-pydantic-and-json-parsing]]
- [[2026-05-05-build-an-mcp-server-in-python-in-15-minutes]]
- [[2026-07-13-python-sdk-13-historical-trends-url-comparisons-and-slack-alerts-in-three-lines-each]]
- [[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]
- [[2026-03-20-pypi-api-discover-python-packages-in-any-domain-free-instant]]
