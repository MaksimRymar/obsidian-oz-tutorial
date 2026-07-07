---
title: The paper reported jumps like 21% to 97%. My replication got +2%.
date: '2026-07-07'
source: https://dev.to/pranav_raj_dae81effb8b57d/the-paper-reported-jumps-like-21-to-97-my-replication-got-2-44jj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]'
- '[[2026-06-21-your-llm-got-the-variant-right-but-did-it-get-it-right-for-the-right-reason]]'
status: unread
---

> **TL;DR:** TL;DR: I ran a small replication of the paper "Prompt Repetition Improves Non-Reasoning LLMs": 100 MMLU questions, one non-reasoning model, prompt sent once versus twice. Baseline 59%, repetition 61%. Probably not statis…

## What’s new and why it matters
TL;DR: I ran a small replication of the paper "Prompt Repetition Improves Non-Reasoning LLMs": 100 MMLU questions, one non-reasoning model, prompt sent once versus twice. Baseline 59%, repetition 61%. Probably not statistically significant, and that turned out to be the interesting part. The gap between the paper's headline numbers and my +2% taught me more about transformer attention than the trick itself. Why I tried this The claim sounds like a joke: paste your prompt twice and a non-reasoning LLM gets better. No chain-of-thought, no fine-tuning, no extra instructions. The paper, Prompt Rep…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pranav_raj_dae81effb8b57d/the-paper-reported-jumps-like-21-to-97-my-replication-got-2-44jj

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]
- [[2026-06-21-your-llm-got-the-variant-right-but-did-it-get-it-right-for-the-right-reason]]
