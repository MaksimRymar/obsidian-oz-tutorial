---
title: U-Net Beats FNO on In-Distribution Heat Conduction — Until You Double the Resolution
date: '2026-11-28'
source: https://dev.to/pack_petter_73cbede229ec2/u-net-beats-fno-on-in-distribution-heat-conduction-until-you-double-the-resolution-3kfo
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#tool'
related:
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]'
- '[[2026-09-18-rabbitmq-vs-kafka-for-data-engineering-queues-vs-logs-when-each-wins]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
status: unread
---

> **TL;DR:** I benchmarked three neural-operator surrogates — FNO, U-Net, and DeepONet — on 2D steady heat conduction, and the ranking flips depending on a question most surrogate papers don't ask: what resolution will you actually d…

## What’s new and why it matters
I benchmarked three neural-operator surrogates — FNO, U-Net, and DeepONet — on 2D steady heat conduction, and the ranking flips depending on a question most surrogate papers don't ask: what resolution will you actually deploy at? The setup (and why I verified the solver first) Before any learning, the reference finite-volume solver was verified: manufactured-solutions convergence order ≈ 2.00, a layered 1D analytic solution matched, and discrete energy balance to better than 3e-13. All three surrogates were then trained on identical budgets over 5 seeds, with out-of-distribution sets and a pai…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pack_petter_73cbede229ec2/u-net-beats-fno-on-in-distribution-heat-conduction-until-you-double-the-resolution-3kfo

## Related notes
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]
- [[2026-09-18-rabbitmq-vs-kafka-for-data-engineering-queues-vs-logs-when-each-wins]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
