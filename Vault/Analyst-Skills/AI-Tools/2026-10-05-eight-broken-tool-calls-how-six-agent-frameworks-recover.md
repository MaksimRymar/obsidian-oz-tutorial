---
title: 'Eight broken tool calls: how six agent frameworks recover'
date: '2026-10-05'
source: https://dev.to/code-with-rashid/eight-broken-tool-calls-how-six-agent-frameworks-recover-9k1
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-02-i-watched-an-8b-model-solve-a-multi-step-task-then-degrade-honestly-on-a-503-a-react-agent-with-real-guardrails]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
- '[[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]'
- '[[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
status: unread
---

> **TL;DR:** Models send bad tool calls: malformed JSON, a tool name that does not exist, a missing argument. What happens next is decided by the agent framework, not the model. In agentic-arena I measure that directly. What was meas…

## What’s new and why it matters
Models send bad tool calls: malformed JSON, a tool name that does not exist, a missing argument. What happens next is decided by the agent framework, not the model. In agentic-arena I measure that directly. What was measured The resilience arena feeds eight scripted faults to every framework. The scripted model turns are byte-identical for all of them, so any difference in outcome is the framework's own error handling: res-01 calculator called with malformed JSON arguments res-02 a tool that does not exist res-03 an unevaluable expression (the tool returns ERROR) res-04 a required argument mis…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/code-with-rashid/eight-broken-tool-calls-how-six-agent-frameworks-recover-9k1

## Related notes
- [[2026-08-02-i-watched-an-8b-model-solve-a-multi-step-task-then-degrade-honestly-on-a-503-a-react-agent-with-real-guardrails]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
- [[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]
- [[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
