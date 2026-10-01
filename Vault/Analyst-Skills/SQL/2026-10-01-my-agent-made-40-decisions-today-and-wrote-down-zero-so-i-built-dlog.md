---
title: My agent made 40 decisions today and wrote down zero. So I built dlog.
date: '2026-10-01'
source: https://dev.to/haoli/my-agent-made-40-decisions-today-and-wrote-down-zero-so-i-built-dlog-23hc
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-09-10-i-got-tired-of-my-ai-agents-fighting-over-one-repo-so-i-built-taskpods]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-03-15-i-was-tired-of-writing-fix-as-my-commit-message-so-i-built-this-in-one-afternoon]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]'
status: unread
---

> **TL;DR:** Coding agents make dozens of decisions per session — which library, which schema, which approach — and never write them down. The next session rediscovers all of it: same debates, same wrong turns, same "wait, why did we…

## What’s new and why it matters
Coding agents make dozens of decisions per session — which library, which schema, which approach — and never write them down. The next session rediscovers all of it: same debates, same wrong turns, same "wait, why did we do it this way?" Memory only holds what gets saved. If nobody saves the decision, it isn't there. dlog is the 30-second habit that fixes this. One line when you decide something: dlog add "chose sqlite over postgres" -r "single-file, zero deps, enough for v1" -t db,infra # logged -> ./.dlog.jsonl Later: $ dlog list 10-01 00:31 dropped tailwind [ css] 10-01 00:30 chose sqlite o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/haoli/my-agent-made-40-decisions-today-and-wrote-down-zero-so-i-built-dlog-23hc

## Related notes
- [[2026-09-10-i-got-tired-of-my-ai-agents-fighting-over-one-repo-so-i-built-taskpods]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-03-15-i-was-tired-of-writing-fix-as-my-commit-message-so-i-built-this-in-one-afternoon]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]
