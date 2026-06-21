---
title: I Built an Open-Source Reliability Tester for Multi-Agent AI Systems — Here's
  What It Catches
date: '2026-06-21'
source: https://dev.to/suraj_kumar_96bb8767435e2/i-built-an-open-source-reliability-tester-for-multi-agent-ai-systems-heres-what-it-catches-217i
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-04-12-i-built-a-tcp-networking-library-in-python-at-14-and-v162-just-hit-110k-msgs-with-zero-dependencies]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** A multi-agent system where each agent is 95% reliable, chained 14 deep, is only about 49% reliable end-to-end. 0.95^14 ≈ 0.49. Every additional agent multiplies the failure surface, and standard testing doesn't catch the…

## What’s new and why it matters
A multi-agent system where each agent is 95% reliable, chained 14 deep, is only about 49% reliable end-to-end. 0.95^14 ≈ 0.49. Every additional agent multiplies the failure surface, and standard testing doesn't catch the failures that emerge from agent interaction — only the ones inside a single agent. I built swarm-test to test the interactions. It's open source, free, and works across CrewAI, LangGraph, AutoGen, and custom orchestrators. Here's what it does. Reliability scoring (0-100) Every system gets a Swarm Score from 8 structural chaos tests: cascade_failure — does one agent's failure t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/suraj_kumar_96bb8767435e2/i-built-an-open-source-reliability-tester-for-multi-agent-ai-systems-heres-what-it-catches-217i

## Related notes
- [[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-04-12-i-built-a-tcp-networking-library-in-python-at-14-and-v162-just-hit-110k-msgs-with-zero-dependencies]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
