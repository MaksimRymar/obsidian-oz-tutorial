---
title: 'Catalog-bound Decide+Act: why free tool-calling felt wrong for SysOps writes'
date: '2026-11-17'
source: https://dev.to/thec0dewriter/catalog-bound-decideact-why-free-tool-calling-felt-wrong-for-sysops-writes-118b
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]'
- '[[2026-09-22-our-product-search-only-returns-rows-the-scanner-can-actually-answer-for]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-05-30-simple-sql-tool]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** This is a submission for the MLH x DEV Writing Challenge I spent MLH Global Hack Week: Builders Week (Nov 6–12, 2026) fighting a pattern that still shows up in “AI Ops” demos: an LLM that talks about fixing a host, then…

## What’s new and why it matters
This is a submission for the MLH x DEV Writing Challenge I spent MLH Global Hack Week: Builders Week (Nov 6–12, 2026) fighting a pattern that still shows up in “AI Ops” demos: an LLM that talks about fixing a host, then invents the shell command that would do it. This is a builder story — process and trust boundaries, not a preprint. What I Built Escalane is a catalog-bound Decide+Act harness for SysOps. The model chooses what kind of fix fits; the harness is the only thing that runs . Code + CLI: escalane-lab/escalane . System One is the decision backend — it answers typed questions (which pl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thec0dewriter/catalog-bound-decideact-why-free-tool-calling-felt-wrong-for-sysops-writes-118b

## Related notes
- [[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]
- [[2026-09-22-our-product-search-only-returns-rows-the-scanner-can-actually-answer-for]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-05-30-simple-sql-tool]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
