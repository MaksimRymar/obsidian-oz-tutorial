---
title: Refresh token rotation with reuse detection in FastAPI (SQLAlchemy example)
date: '2026-11-27'
source: https://dev.to/launchpadkits/refresh-token-rotation-with-reuse-detection-in-fastapi-sqlalchemy-example-15n9
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-04-user-model-auth-basics-password-hashing-with-bcrypt-in-fastapi]]'
- '[[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]'
- '[[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
status: unread
---

> **TL;DR:** Long-lived refresh tokens are the weak point of JWT auth: if one leaks, the attacker can mint access tokens until it expires. Rotation plus reuse detection limits the damage. Here is a compact implementation with FastAPI…

## What’s new and why it matters
Long-lived refresh tokens are the weak point of JWT auth: if one leaks, the attacker can mint access tokens until it expires. Rotation plus reuse detection limits the damage. Here is a compact implementation with FastAPI and async SQLAlchemy. The idea Every refresh token has a unique id ( jti ) and belongs to a family , which is created at login. Each refresh token is single use . Calling /refresh revokes the old token and issues a new one in the same family. If a token that was already revoked shows up again, someone replayed it (the legitimate client or the thief used it first). Revoke the w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/launchpadkits/refresh-token-rotation-with-reuse-detection-in-fastapi-sqlalchemy-example-15n9

## Related notes
- [[2026-03-04-user-model-auth-basics-password-hashing-with-bcrypt-in-fastapi]]
- [[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]
- [[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
