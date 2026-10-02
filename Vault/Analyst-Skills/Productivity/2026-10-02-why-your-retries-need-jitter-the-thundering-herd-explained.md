---
title: 'Why your retries need jitter: the thundering herd, explained'
date: '2026-10-02'
source: https://dev.to/kashif_manzer/why-your-retries-need-jitter-the-thundering-herd-explained-3eje
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#sql'
related:
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-09-08-write-code-once-use-it-forever-python-functions-explained]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
status: unread
---

> **TL;DR:** Picture this. It is 2:14 in the morning and your checkout service starts returning errors. Every request fails for about twenty seconds, then your deploy finishes rolling back and the error rate drops to zero. You exhale…

## What’s new and why it matters
Picture this. It is 2:14 in the morning and your checkout service starts returning errors. Every request fails for about twenty seconds, then your deploy finishes rolling back and the error rate drops to zero. You exhale. Then the dashboards spike again. Harder than before. Nothing changed on your end. The service was healthy. So what knocked it over the second time? Your own services did. Every client that failed during those twenty seconds had been retrying, and the moment the service came back, they all arrived at once. The recovery got flattened by a second wave made entirely of retries. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kashif_manzer/why-your-retries-need-jitter-the-thundering-herd-explained-3eje

## Related notes
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-09-08-write-code-once-use-it-forever-python-functions-explained]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
