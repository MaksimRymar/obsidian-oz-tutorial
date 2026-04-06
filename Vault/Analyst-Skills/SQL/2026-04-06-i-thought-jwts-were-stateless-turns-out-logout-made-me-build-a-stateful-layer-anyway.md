---
title: I Thought JWTs Were Stateless. Turns Out Logout Made Me Build a Stateful Layer
  Anyway.
date: '2026-04-06'
source: https://dev.to/ravigupta97/i-thought-jwts-were-stateless-turns-out-logout-made-me-build-a-stateful-layer-anyway-48nd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-03-19-i-used-ai-to-build-my-project-but-then-i-had-to-actually-understand-it]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-02-27-orms-are-a-lie-we-tell-junior-developers-so-they-dont-have-to-learn-sql]]'
status: unread
---

> **TL;DR:** This is Part 3 of a 4-part series on building AuthShield - a production-ready standalone authentication microservice. This post covers JWT design, the logout problem, Redis blacklisting, the two-token strategy, and refre…

## What’s new and why it matters
This is Part 3 of a 4-part series on building AuthShield - a production-ready standalone authentication microservice. This post covers JWT design, the logout problem, Redis blacklisting, the two-token strategy, and refresh token rotation with reuse detection. Part 1 is here: Why I Stopped Writing Auth Code for Every Project and Built AuthShield Part 2 is here: I Thought OAuth Was Just Adding a Google Button. Turns Out It's a CSRF Problem Disguised as a Feature The selling point of JWTs is that they are stateless. The server issues a token, signs it, and forgets about it. Every subsequent reque…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ravigupta97/i-thought-jwts-were-stateless-turns-out-logout-made-me-build-a-stateful-layer-anyway-48nd

## Related notes
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-03-19-i-used-ai-to-build-my-project-but-then-i-had-to-actually-understand-it]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-02-27-orms-are-a-lie-we-tell-junior-developers-so-they-dont-have-to-learn-sql]]
