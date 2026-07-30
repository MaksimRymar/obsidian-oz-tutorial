---
title: AI Didn't Break Enterprise Data Models. It Exposed Their Blind Spots.
date: '2026-07-29'
source: https://dev.to/arisyn/ai-didnt-break-enterprise-data-models-it-exposed-their-blind-spots-1kkl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-07-27-foreign-keys-arent-enough-why-enterprise-ai-needs-relationship-discovery]]'
- '[[2026-07-08-ai-agents-dont-need-more-tables-they-need-better-relationships]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-06-24-why-ai-analytics-has-a-knowledge-problem]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** Over the past few years, I've worked with several enterprise AI projects, especially those involving natural language querying and AI-powered analytics. One pattern keeps showing up. When an AI system returns the wrong a…

## What’s new and why it matters
Over the past few years, I've worked with several enterprise AI projects, especially those involving natural language querying and AI-powered analytics. One pattern keeps showing up. When an AI system returns the wrong answer, people usually blame the model. "Maybe we need a larger LLM." "Maybe the prompt needs more context." "Maybe SQL generation isn't mature enough." After digging into these projects, I came to a different conclusion. In many cases, the model isn't the real problem. The enterprise data model is. Enterprise Data Models Were Never Designed for AI For decades, enterprise databa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arisyn/ai-didnt-break-enterprise-data-models-it-exposed-their-blind-spots-1kkl

## Related notes
- [[2026-07-27-foreign-keys-arent-enough-why-enterprise-ai-needs-relationship-discovery]]
- [[2026-07-08-ai-agents-dont-need-more-tables-they-need-better-relationships]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-06-24-why-ai-analytics-has-a-knowledge-problem]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
