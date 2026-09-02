---
title: Your agent request touches 12 containers. Only one of them runs a model.
date: '2026-09-02'
source: https://dev.to/judezh/your-agent-request-touches-12-containers-only-one-of-them-runs-a-model-587b
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]'
status: unread
---

> **TL;DR:** In the last post I cut this stack down to four long-running containers. The most common follow-up was not "how did you cut it" but the inverse: So what are the rest of them actually for? That deserves a straight answer.…

## What’s new and why it matters
In the last post I cut this stack down to four long-running containers. The most common follow-up was not "how did you cut it" but the inverse: So what are the rest of them actually for? That deserves a straight answer. When a self-hosted project's quickstart starts a dozen containers, the default reading is either "the architecture never converged" or "someone is cosplaying enterprise." Neither reading is unfair — plenty of projects earn it. So this post does exactly one thing: it walks a single agent run from arrival to completion, and every time the run touches a service, says what that ser…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/judezh/your-agent-request-touches-12-containers-only-one-of-them-runs-a-model-587b

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]
