---
title: My benchmark harness was wrong fourteen ways before it measured anything
date: '2026-09-12'
source: https://dev.to/remdore/my-benchmark-harness-was-wrong-fourteen-ways-before-it-measured-anything-1o6h
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** I built a harness to measure whether reverse proxies buffer Server-Sent Events. The results are in the last post . This post is about the harness, which was wrong in fourteen ways before it produced a single number I wou…

## What’s new and why it matters
I built a harness to measure whether reverse proxies buffer Server-Sent Events. The results are in the last post . This post is about the harness, which was wrong in fourteen ways before it produced a single number I would stand behind. That is not a confession of sloppiness. It is the normal state of measurement code, and the reason it stays wrong is structural: a benchmark harness is the one piece of software whose output nobody can independently check. If your web app returns the wrong price, a user complains. If your harness returns 1.02 instead of 1.00, it goes in a blog post and gets quo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/remdore/my-benchmark-harness-was-wrong-fourteen-ways-before-it-measured-anything-1o6h

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
