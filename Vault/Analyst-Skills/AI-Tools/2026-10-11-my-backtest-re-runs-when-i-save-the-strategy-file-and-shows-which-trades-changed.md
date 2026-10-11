---
title: My backtest re-runs when I save the strategy file, and shows which trades changed
date: '2026-10-11'
source: https://dev.to/hawkbtcommander/my-backtest-re-runs-when-i-save-the-strategy-file-and-shows-which-trades-changed-13cd
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]'
- '[[2026-10-09-dont-let-a-new-signal-engine-write-fake-trades-a-warm-up-flag-for-trading-alert-bots]]'
- '[[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]'
status: unread
---

> **TL;DR:** I'm building a backtesting web app called Hawk Backtester on the side. This post is about one feature, a watch mode for local Python strategies. The loop that annoyed me most was edit the strategy, run it in a terminal,…

## What’s new and why it matters
I'm building a backtesting web app called Hawk Backtester on the side. This post is about one feature, a watch mode for local Python strategies. The loop that annoyed me most was edit the strategy, run it in a terminal, open the results, then try to remember what the previous run looked like. The last step was the worst. If PnL went up a little, I couldn't tell whether my change did it or a couple of trades just happened to land differently. So now the backtest runs again the moment I save, and it tells me which trades changed. Using it On your machine: pip install -U hawk-bt hawk-bt run my_st…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hawkbtcommander/my-backtest-re-runs-when-i-save-the-strategy-file-and-shows-which-trades-changed-13cd

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]
- [[2026-10-09-dont-let-a-new-signal-engine-write-fake-trades-a-warm-up-flag-for-trading-alert-bots]]
- [[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]
