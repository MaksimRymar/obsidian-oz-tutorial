---
title: 'Backtesting Futures Gamma (ES & NQ): Historical GEX Done Right'
date: '2026-07-08'
source: https://dev.to/tomasz_dobrowolski_35d32c/backtesting-futures-gamma-es-nq-historical-gex-done-right-21gl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#presentations'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-14-build-your-own-second-brain-rag-powered-knowledge-tools-that-never-leave-your-machine]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-04-28-stop-making-dead-charts-plotly-and-the-world-of-interactive-visualization]]'
- '[[2026-06-08-retention-cohort-analysis-with-plain-sql]]'
status: unread
---

> **TL;DR:** "Can I backtest futures gamma?" is one of the most common questions we get from quant desks, and the honest answer has two parts. First: FlashAlpha serves live gamma exposure on ES and NQ futures today, computed properly…

## What’s new and why it matters
"Can I backtest futures gamma?" is one of the most common questions we get from quant desks, and the honest answer has two parts. First: FlashAlpha serves live gamma exposure on ES and NQ futures today, computed properly on the options-on-futures chains. Second: the historical replay engine does not yet cover the futures symbols, so /v1/exposure/gex/ES=F?at=... returns no data. That is a real limitation — and this article is about the fact that it is not the blocker it looks like. The reason is structural. The dealer gamma that pins or unpins ES is the gamma of the entire S&P 500 options compl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tomasz_dobrowolski_35d32c/backtesting-futures-gamma-es-nq-historical-gex-done-right-21gl

## Related notes
- [[2026-04-14-build-your-own-second-brain-rag-powered-knowledge-tools-that-never-leave-your-machine]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-04-28-stop-making-dead-charts-plotly-and-the-world-of-interactive-visualization]]
- [[2026-06-08-retention-cohort-analysis-with-plain-sql]]
