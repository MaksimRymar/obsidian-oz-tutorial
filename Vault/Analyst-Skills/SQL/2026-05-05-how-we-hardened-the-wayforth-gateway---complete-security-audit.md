---
title: How We Hardened the Wayforth Gateway - Complete Security Audit
date: '2026-05-05'
source: https://dev.to/wayforthofficial/how-we-hardened-the-wayforth-gateway-complete-security-audit-31n4
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-03-16-pay-per-request-apis-from-python-skip-the-api-key-pay-with-usdc-instead]]'
- '[[2026-02-28-delete-itemsid-removing-data-from-your-api-with-fastapi]]'
- '[[2026-04-17-the-ai-agent-economy-needs-payment-rails-heres-what-i-built]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
status: unread
---

> **TL;DR:** We shipped Wayforth — a search and payment rail for AI agents — and before expanding the managed services catalog we ran a full security audit. Here's how we fixed it. The Stack FastAPI · PostgreSQL · Railway · Base bloc…

## What’s new and why it matters
We shipped Wayforth — a search and payment rail for AI agents — and before expanding the managed services catalog we ran a full security audit. Here's how we fixed it. The Stack FastAPI · PostgreSQL · Railway · Base blockchain Supabase Auth · Stripe · Fernet AES-128 · BSL 1.1 uvx wayforth-mcp Critical Findings (5) C1 — JWT not cryptographically verified Fix: JWKS-based ES256 verification via Supabase's public endpoint — no shared secret needed. def verify_supabase_jwt ( token : str ) -> dict : jwks = get_jwks () # cached 1hr header = jwt . get_unverified_header ( token ) key = next ( k for k i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/wayforthofficial/how-we-hardened-the-wayforth-gateway-complete-security-audit-31n4

## Related notes
- [[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-03-16-pay-per-request-apis-from-python-skip-the-api-key-pay-with-usdc-instead]]
- [[2026-02-28-delete-itemsid-removing-data-from-your-api-with-fastapi]]
- [[2026-04-17-the-ai-agent-economy-needs-payment-rails-heres-what-i-built]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
