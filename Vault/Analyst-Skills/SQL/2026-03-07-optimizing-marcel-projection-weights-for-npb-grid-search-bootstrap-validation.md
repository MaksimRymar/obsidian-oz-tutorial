---
title: Optimizing Marcel Projection Weights for NPB — Grid Search + Bootstrap Validation
date: '2026-03-07'
source: https://dev.to/yasumorishima/optimizing-marcel-projection-weights-for-npb-grid-search-bootstrap-validation-3pkm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-01-last-place-to-champions-what-marcel-projection-reveals-about-2021-npb-yakult-and-orix]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** Background The Marcel projection system is a simple but effective player performance forecasting method created by Tom Tango. It uses a weighted average of the last 3 seasons plus regression to the mean. GitHub : https:/…

## What’s new and why it matters
Background The Marcel projection system is a simple but effective player performance forecasting method created by Tom Tango. It uses a weighted average of the last 3 seasons plus regression to the mean. GitHub : https://github.com/yasumorishima/npb-marcel-weight-study I've been using these default parameters in npb-prediction ( blog post ), but they were originally calibrated for MLB data : Parameter Meaning Previous (MLB Default) w0 / w1 / w2 Weights for last 3 years 5 / 4 / 3 REG_PA Regression strength (hitters) 1200 REG_IP Regression strength (pitchers) 600 Are these optimal for NPB (Nippo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yasumorishima/optimizing-marcel-projection-weights-for-npb-grid-search-bootstrap-validation-3pkm

## Related notes
- [[2026-03-01-last-place-to-champions-what-marcel-projection-reveals-about-2021-npb-yakult-and-orix]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
