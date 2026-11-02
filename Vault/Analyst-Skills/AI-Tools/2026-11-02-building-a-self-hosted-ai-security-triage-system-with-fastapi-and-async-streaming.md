---
title: Building a Self-Hosted AI Security Triage System with FastAPI and Async Streaming
date: '2026-11-02'
source: https://dev.to/leo_martinez/building-a-self-hosted-ai-security-triage-system-with-fastapi-and-async-streaming-2k86
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-19-how-we-built-an-in-database-ai-agent-in-pure-t-sql-and-fixed-its-hidden-architectural-blindspots]]'
- '[[2026-10-07-building-a-secure-django-rest-api-for-task-management]]'
status: unread
---

> **TL;DR:** Why I Started Looking at beenuar/AiSOC When our SOC team complained about false positive fatigue (95% of alerts ignored), I needed an LLM-powered triage layer that could run internally without shipping sensitive logs to…

## What’s new and why it matters
Why I Started Looking at beenuar/AiSOC When our SOC team complained about false positive fatigue (95% of alerts ignored), I needed an LLM-powered triage layer that could run internally without shipping sensitive logs to external APIs. After evaluating commercial SOAR platforms and their vendor lock-in, I tested beenuar/AiSOC—a self-hosted alert fusion system built entirely on FastAPI with async streaming. The architectural promise: ingest raw alerts, run multi-agent investigation chains against MITRE ATT&CK, and stream decision reasoning back to analysts in real-time via Server-Sent Events. Al…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/leo_martinez/building-a-self-hosted-ai-security-triage-system-with-fastapi-and-async-streaming-2k86

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-19-how-we-built-an-in-database-ai-agent-in-pure-t-sql-and-fixed-its-hidden-architectural-blindspots]]
- [[2026-10-07-building-a-secure-django-rest-api-for-task-management]]
