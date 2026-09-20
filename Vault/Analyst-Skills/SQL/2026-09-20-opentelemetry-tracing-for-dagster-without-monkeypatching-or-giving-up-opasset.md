---
title: OpenTelemetry tracing for Dagster, without monkeypatching or giving up @op/@asset
date: '2026-09-20'
source: https://dev.to/hirofumi_tsuda/opentelemetry-tracing-for-dagster-without-monkeypatching-or-giving-up-opasset-g3d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
status: unread
---

> **TL;DR:** Dagster doesn't have a built-in way to get OpenTelemetry traces out of a run. There's an open issue on the main repo asking for it ( dagster-io/dagster#11191 ), and a more specific one asking for trace/span IDs correlate…

## What’s new and why it matters
Dagster doesn't have a built-in way to get OpenTelemetry traces out of a run. There's an open issue on the main repo asking for it ( dagster-io/dagster#11191 ), and a more specific one asking for trace/span IDs correlated into log lines ( #12353 ). Neither has shipped. The workarounds I could find were monkeypatching Dagster internals, or wrapping every @op / @asset in a third-party decorator that effectively takes ownership of the function away from Dagster's own decorators. Neither felt right for something I wanted to actually run. So I wrote dagster-otel : a small decorator, @traced() , tha…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hirofumi_tsuda/opentelemetry-tracing-for-dagster-without-monkeypatching-or-giving-up-opasset-g3d

## Related notes
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
