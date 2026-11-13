---
title: 'Well Pump TDH in Python: The Pressure Switch Is Half the Head'
date: '2026-11-13'
source: https://dev.to/evgeniikonkin/well-pump-tdh-in-python-the-pressure-switch-is-half-the-head-2h2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-11-09-automating-smm-panel-orders-with-python-a-tiny-wrapper-for-the-apiv2-pattern]]'
- '[[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-05-27-how-to-brier-grade-your-own-ml-option-pricing-forecasts-in-40-lines-of-python]]'
- '[[2026-11-03-etsy-competitor-analysis-without-a-monthly-tool-what-40-pet-portrait-listings-showed-me]]'
status: unread
---

> **TL;DR:** Most well pump questions start with "my well is 200 feet deep." Depth is not what sizes the pump. A pump is selected by flow (gpm) and total dynamic head (TDH, in feet). Here is a small Python model that builds TDH from…

## What’s new and why it matters
Most well pump questions start with "my well is 200 feet deep." Depth is not what sizes the pump. A pump is selected by flow (gpm) and total dynamic head (TDH, in feet). Here is a small Python model that builds TDH from its parts, so you can see which part dominates. The model TDH has four components: Lift : static water level + drawdown (the pumping water level, not the well depth) Elevation rise : wellhead to the highest fixture Pressure head : switch cut-out pressure × 2.31 ft/psi Friction : Hazen-Williams loss over drop pipe + service line, plus a fitting allowance PIPE_ID_IN = { "1" : 1.0…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/evgeniikonkin/well-pump-tdh-in-python-the-pressure-switch-is-half-the-head-2h2

## Related notes
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-11-09-automating-smm-panel-orders-with-python-a-tiny-wrapper-for-the-apiv2-pattern]]
- [[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-05-27-how-to-brier-grade-your-own-ml-option-pricing-forecasts-in-40-lines-of-python]]
- [[2026-11-03-etsy-competitor-analysis-without-a-monthly-tool-what-40-pet-portrait-listings-showed-me]]
