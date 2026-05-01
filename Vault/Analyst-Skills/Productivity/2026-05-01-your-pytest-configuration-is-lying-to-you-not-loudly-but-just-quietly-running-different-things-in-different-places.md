---
title: Your pytest configuration is lying to you. Not loudly but just quietly running
  different things in different places.
date: '2026-05-01'
source: https://dev.to/michle/your-pytest-configuration-is-lying-to-you-not-loudly-but-just-quietly-running-different-things-in-4m2k
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-03-06-why-your-chaos-experiments-are-probably-wasting-time-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** Picture this. A test starts failing in CI. You pull the branch locally, run the suite, and it passes. You dig in for twenty minutes before realising the CI run has --capture-screenshots=failed and yours doesn't, so the s…

## What’s new and why it matters
Picture this. A test starts failing in CI. You pull the branch locally, run the suite, and it passes. You dig in for twenty minutes before realising the CI run has --capture-screenshots=failed and yours doesn't, so the screenshot that would have told you exactly what broke exists in CI, but you never thought to check because your local run gave you nothing. Or the reverse: you add --plus-email to your CI command to get the report delivered after each run, forget to strip it out of the local config, and now every developer on the team is getting email on every local test run. These aren't drama…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michle/your-pytest-configuration-is-lying-to-you-not-loudly-but-just-quietly-running-different-things-in-4m2k

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-03-06-why-your-chaos-experiments-are-probably-wasting-time-and-how-to-fix-it]]
