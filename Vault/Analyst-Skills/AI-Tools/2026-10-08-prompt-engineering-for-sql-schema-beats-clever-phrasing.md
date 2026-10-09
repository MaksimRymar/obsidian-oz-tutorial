---
title: 'Prompt Engineering for SQL: Schema Beats Clever Phrasing'
date: '2026-10-08'
source: https://dev.to/tom-morgan-261976/prompt-engineering-for-sql-schema-beats-clever-phrasing-11kf
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]'
- '[[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-07-07-your-llm-fused-the-two-columns-you-asked-for-and-the-eval-marked-it-wrong]]'
- '[[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]'
status: unread
---

> **TL;DR:** Prompt engineering improves text-to-SQL accuracy mainly by supplying schema context, vetted examples, and execution feedback—not by phrasing the question… TL;DR: The accuracy gap is a schema problem before it’s a languag…

## What’s new and why it matters
Prompt engineering improves text-to-SQL accuracy mainly by supplying schema context, vetted examples, and execution feedback—not by phrasing the question… TL;DR: The accuracy gap is a schema problem before it’s a language problem: on the BIRD benchmark, human accuracy sits near 93%, the leading published system reaches roughly 82%, and on Spider 2.0’s enterprise schemas (800+ columns), a bare model’s success rate can fall to 10–20%. The number looks reasonable. The query ran, returned a result, and looked exactly like every correct query before it. Key takeaways Schema size makes the picture w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tom-morgan-261976/prompt-engineering-for-sql-schema-beats-clever-phrasing-11kf

## Related notes
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]
- [[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-07-07-your-llm-fused-the-two-columns-you-asked-for-and-the-eval-marked-it-wrong]]
- [[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]
