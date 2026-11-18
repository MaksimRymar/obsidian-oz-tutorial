---
title: 'Text-to-SQL on Oracle: 63.7% first try, on a benchmark my bug reports helped
  fix'
date: '2026-11-18'
source: https://dev.to/ashish_sinha_5241c7673d93/text-to-sql-on-oracle-637-first-try-on-a-benchmark-my-bug-reports-helped-fix-58a0
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
related:
- '[[2026-10-20-text-to-sql-on-oracle-two-prompt-rules-took-a-light-model-from-35-to-64]]'
- '[[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]'
- '[[2026-11-13-one-constant-was-costing-my-schema-retriever-17-points]]'
- '[[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]'
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-10-28-i-compared-four-ways-to-pick-tables-for-a-text-to-sql-prompt]]'
status: unread
---

> **TL;DR:** Most text-to-SQL prompts carry the whole schema. schemagate sends only the tables the question needs: 91% fewer schema tokens on 50+ table databases. It is #1 on BIRD's Mini-Dev leaderboard in SQLite, PostgreSQL and MySQ…

## What’s new and why it matters
Most text-to-SQL prompts carry the whole schema. schemagate sends only the tables the question needs: 91% fewer schema tokens on 50+ table databases. It is #1 on BIRD's Mini-Dev leaderboard in SQLite, PostgreSQL and MySQL (81.0 / 72.6 / 72.4), and works as a LangChain and LangGraph retriever. Oracle is where text-to-SQL breaks. On UniQL, BIRD's 1,534 questions translated into 16 dialects, schemagate with Gemini 3.8 Flash scores 63.69% on the first try (64.93% with repair). The best published Oracle score is 49.61% (Claude 4.5 Sonnet). What got it there Two Oracle rules in the prompt (no AS bef…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/text-to-sql-on-oracle-637-first-try-on-a-benchmark-my-bug-reports-helped-fix-58a0

## Related notes
- [[2026-10-20-text-to-sql-on-oracle-two-prompt-rules-took-a-light-model-from-35-to-64]]
- [[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]
- [[2026-11-13-one-constant-was-costing-my-schema-retriever-17-points]]
- [[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-10-28-i-compared-four-ways-to-pick-tables-for-a-text-to-sql-prompt]]
