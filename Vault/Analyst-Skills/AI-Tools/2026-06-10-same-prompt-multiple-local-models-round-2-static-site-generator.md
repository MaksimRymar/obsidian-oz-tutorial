---
title: 'Same Prompt, Multiple Local Models — Round 2: Static Site Generator'
date: '2026-06-10'
source: https://dev.to/harishkotra/same-prompt-multiple-local-models-round-2-static-site-generator-590
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-05-29-part-13-sql-injection-and-staying-safe]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
status: unread
---

> **TL;DR:** Day before, I ran an experiment: give several local LLMs the exact same prompt (build a terminal-based roguelike game in Python 3) and compare what comes out. The goal was never to declare a winner — it was to see how ar…

## What’s new and why it matters
Day before, I ran an experiment: give several local LLMs the exact same prompt (build a terminal-based roguelike game in Python 3) and compare what comes out. The goal was never to declare a winner — it was to see how architectural choices, edge-case handling, and failure modes diverge when the input is held perfectly constant. The results were more interesting than I expected. Surface compliance was common; correct state management was not. Presentation polish sometimes masked mechanical defects. Failed generations were still useful data points. So I did it again. Same methodology, different…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/harishkotra/same-prompt-multiple-local-models-round-2-static-site-generator-590

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-05-29-part-13-sql-injection-and-staying-safe]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
