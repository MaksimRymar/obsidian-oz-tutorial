---
title: About 30% of public PX4 drone logs have a GPS delay setting more than 50 ms
  off, and EKF2's own residuals agree
date: '2026-11-02'
source: https://dev.to/munimv2/about-30-of-public-px4-drone-logs-have-a-gps-delay-setting-more-than-50-ms-off-and-ekf2s-own-haa
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-10-07-a-website-shared-by-more-than-three-places-is-a-chain-and-163-of-the-318-we-flagged-had-no-brand-field]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]'
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
status: unread
---

> **TL;DR:** PX4's state estimator, EKF2, has to know how old each GPS sample is when it arrives. Up to PX4 v1.17 that is the parameter EKF2_GPS_DELAY , 110 ms by default. Almost nobody changes it: in the public flight logs we read,…

## What’s new and why it matters
PX4's state estimator, EKF2, has to know how old each GPS sample is when it arrives. Up to PX4 v1.17 that is the parameter EKF2_GPS_DELAY , 110 ms by default. Almost nobody changes it: in the public flight logs we read, 96-98% of vehicles ran the default. So we measured it. We took random samples of real flights uploaded to PX4 Flight Review since October 2025, one log per vehicle, and wrote down every prediction before downloading anything. How the delay is measured gps_lag.py compares two things that should tell the same story. One is the change in GPS velocity between consecutive GPS sample…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/munimv2/about-30-of-public-px4-drone-logs-have-a-gps-delay-setting-more-than-50-ms-off-and-ekf2s-own-haa

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-10-07-a-website-shared-by-more-than-three-places-is-a-chain-and-163-of-the-318-we-flagged-had-no-brand-field]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
