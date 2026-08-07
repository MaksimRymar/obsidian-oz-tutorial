---
title: Your text-to-SQL model isn't as wrong as your benchmark says. The gold SQL
  is.
date: '2026-08-07'
source: https://dev.to/omer_hochman/your-text-to-sql-model-isnt-as-wrong-as-your-benchmark-says-the-gold-sql-is-p16
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-07-07-your-llm-fused-the-two-columns-you-asked-for-and-the-eval-marked-it-wrong]]'
- '[[2026-07-20-not-in-returned-zero-rows-it-wasnt-your-data-it-was-one-null]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog You run BIRD-dev, read an execution accuracy of 0.512, and the instinct is immediate: start writing planner directives to close the gap. We had the same instinct. Before acting on i…

## What’s new and why it matters
Originally published at nlqdb.com/blog You run BIRD-dev, read an execution accuracy of 0.512, and the instinct is immediate: start writing planner directives to close the gap. We had the same instinct. Before acting on it we did one thing that changed the whole plan — we bucketed the losses. Not skimmed a few failures; tagged all 238 mismatches with a structural differ and counted what actually went wrong in each. 19% of our losses were one DISTINCT — added correctly The biggest bucket was startling: 46 of 238 mismatches (19%) differ from the gold SQL only by a DISTINCT the model added and gol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/omer_hochman/your-text-to-sql-model-isnt-as-wrong-as-your-benchmark-says-the-gold-sql-is-p16

## Related notes
- [[2026-07-07-your-llm-fused-the-two-columns-you-asked-for-and-the-eval-marked-it-wrong]]
- [[2026-07-20-not-in-returned-zero-rows-it-wasnt-your-data-it-was-one-null]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]
