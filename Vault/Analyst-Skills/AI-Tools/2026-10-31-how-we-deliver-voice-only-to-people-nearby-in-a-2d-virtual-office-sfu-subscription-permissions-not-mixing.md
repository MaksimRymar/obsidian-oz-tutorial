---
title: How we deliver voice only to people nearby in a 2D virtual office (SFU subscription
  permissions, not mixing)
date: '2026-10-31'
source: https://dev.to/hotoriplace/how-we-deliver-voice-only-to-people-nearby-in-a-2d-virtual-office-sfu-subscription-permissions-40nl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-14-agents-for-humans-an-agent-that-refuses-to-guess-what-your-letter-says]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** In our 2D virtual office, voice reaches only nearby people because the media server refuses to forward it to anyone else. The app server works out who is near whom and gives each speaker a list of allowed listeners. Each…

## What’s new and why it matters
In our 2D virtual office, voice reaches only nearby people because the media server refuses to forward it to anyone else. The app server works out who is near whom and gives each speaker a list of allowed listeners. Each speaker's client passes that list to LiveKit, our SFU, as track subscription permissions, so nothing is mixed on the server and a modified listening browser cannot pull a voice it was not given. An SFU (selective forwarding unit) forwards each person's tracks instead of combining them. The stack here is a Python (FastAPI) WebSocket server, a React and Phaser client, and self-h…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hotoriplace/how-we-deliver-voice-only-to-people-nearby-in-a-2d-virtual-office-sfu-subscription-permissions-40nl

## Related notes
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-14-agents-for-humans-an-agent-that-refuses-to-guess-what-your-letter-says]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
