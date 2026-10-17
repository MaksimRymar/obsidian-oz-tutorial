---
title: Check that a package exists before your AI agent installs it
date: '2026-10-17'
source: https://dev.to/martenfitz/check-that-a-package-exists-before-your-ai-agent-installs-it-4l9k
domain: Tableau
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#tableau'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-11-how-to-export-google-play-reviews-to-csv-for-any-app-and-country]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-10-05-daylight-left-an-offline-sunset-clock-that-tells-you-where-to-go-before-dark]]'
- '[[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]'
- '[[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]'
status: unread
---

> **TL;DR:** AI coding assistants are good at writing code and surprisingly confident about package names. Every so often they suggest one that does not exist. Attackers have noticed: they register the names models tend to invent and…

## What’s new and why it matters
AI coding assistants are good at writing code and surprisingly confident about package names. Every so often they suggest one that does not exist. Attackers have noticed: they register the names models tend to invent and wait for someone to run the install command. The practice now has a name, "slopsquatting", next to the older typosquatting. If an agent in your workflow runs npm install or pip install on its own, one cheap check closes most of that gap: before installing, ask the registry whether the package is real, how old it is, and whether anything is known to be wrong with it. What to lo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/martenfitz/check-that-a-package-exists-before-your-ai-agent-installs-it-4l9k

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-11-how-to-export-google-play-reviews-to-csv-for-any-app-and-country]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-10-05-daylight-left-an-offline-sunset-clock-that-tells-you-where-to-go-before-dark]]
- [[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]
- [[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]
