---
title: I built a MyBatis-style SQL mapper for .NET because EF Core was eating all
  our memory
date: '2026-03-07'
source: https://dev.to/yurgenschmidt/i-built-a-mybatis-style-sql-mapper-for-net-because-ef-core-was-eating-all-our-memory-146b
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-i-built-a-job-search-tool-that-pulls-directly-from-company-ats-systems-not-job-boards]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-02-24-stop-ignoring-rfc-2324-its-the-most-important-protocol-youve-never-implemented]]'
- '[[2026-03-06-we-built-an-agent-to-agent-job-marketplace-with-crypto-escrow-in-868-lines]]'
- '[[2026-03-05-i-built-a-self-hosted-llm-observability-tool-for-ai-applications-logmera]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
status: unread
---

> **TL;DR:** When I inherited a .NET-based stats service, the codebase was EF Core all the way down. Query performance was the first problem — and that I solved, eventually cutting response times by 2x to 3600x depending on the query…

## What’s new and why it matters
When I inherited a .NET-based stats service, the codebase was EF Core all the way down. Query performance was the first problem — and that I solved, eventually cutting response times by 2x to 3600x depending on the query. But memory was different. EF Core's change tracking, materialization overhead, and object graph behavior imposed a ceiling I couldn't optimize past. I'd spent most of my career on Java and Spring. MyBatis was my default tool for anything SQL-heavy. I looked at Dapper — solid library, genuinely good — but I wanted SQL and code to live in separate files, not inline strings. So…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yurgenschmidt/i-built-a-mybatis-style-sql-mapper-for-net-because-ef-core-was-eating-all-our-memory-146b

## Related notes
- [[2026-03-05-i-built-a-job-search-tool-that-pulls-directly-from-company-ats-systems-not-job-boards]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-02-24-stop-ignoring-rfc-2324-its-the-most-important-protocol-youve-never-implemented]]
- [[2026-03-06-we-built-an-agent-to-agent-job-marketplace-with-crypto-escrow-in-868-lines]]
- [[2026-03-05-i-built-a-self-hosted-llm-observability-tool-for-ai-applications-logmera]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
