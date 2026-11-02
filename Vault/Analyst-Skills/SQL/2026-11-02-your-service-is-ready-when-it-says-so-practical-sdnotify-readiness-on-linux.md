---
title: 'Your Service Is Ready When It Says So: Practical sd_notify Readiness on Linux'
date: '2026-11-02'
source: https://dev.to/lyraalishaikh/your-service-is-ready-when-it-says-so-practical-sdnotify-readiness-on-linux-38p8
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-09-02-your-agent-request-touches-12-containers-only-one-of-them-runs-a-model]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
status: unread
---

> **TL;DR:** A service that loads a 14 GB model takes longer to become useful than it takes to start. For years the workaround has been the same everywhere: [Service] Type = simple ExecStartPre = /bin/sleep 10 ExecStart = /usr/local/…

## What’s new and why it matters
A service that loads a 14 GB model takes longer to become useful than it takes to start. For years the workaround has been the same everywhere: [Service] Type = simple ExecStartPre = /bin/sleep 10 ExecStart = /usr/local/bin/inference-server --config /etc/inference.toml It works until the day the disk is slower, the model is bigger, or the host is busy. Then the reverse proxy starts routing traffic ten seconds after systemctl start returned, and every request during that window gets a 502. The opposite failure is just as common: a ten-second sleep on a service that needed two, which is eight se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lyraalishaikh/your-service-is-ready-when-it-says-so-practical-sdnotify-readiness-on-linux-38p8

## Related notes
- [[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-09-02-your-agent-request-touches-12-containers-only-one-of-them-runs-a-model]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
