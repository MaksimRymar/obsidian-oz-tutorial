---
title: Building a DAG Orchestrator That Rewrites Its Own Execution Plan
date: '2026-04-18'
source: https://dev.to/kingsleyonoh/building-a-dag-orchestrator-that-rewrites-its-own-execution-plan-14bh
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
status: unread
---

> **TL;DR:** Step 7 is a condition: if the HTTP response came back 200, continue to step 8 and step 9. If not, skip them and jump to step 10. Five steps downstream of a single boolean, two possible paths, and a directed acyclic graph…

## What’s new and why it matters
Step 7 is a condition: if the HTTP response came back 200, continue to step 8 and step 9. If not, skip them and jump to step 10. Five steps downstream of a single boolean, two possible paths, and a directed acyclic graph that only understands one thing: which step depends on which. DAGs don't branch. That was the problem I had to solve. The linear model The linear step types worked without issues. HTTP calls, data transforms, delays, sub-workflows. The orchestrator in orchestrator.py called topological_sort() from graph.py , got back a flat list of steps in dependency order, and executed them…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kingsleyonoh/building-a-dag-orchestrator-that-rewrites-its-own-execution-plan-14bh

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
