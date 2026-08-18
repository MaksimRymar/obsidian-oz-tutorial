---
title: 'What Wrong JSON Costs: Chat Model Text and Image Moderation Under One API
  Key'
date: '2026-08-18'
source: https://dev.to/emersonprice3718/what-wrong-json-costs-chat-model-text-and-image-moderation-under-one-api-key-2b7p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** Use one chat model behind one API key, with a strict JSON schema on every call, for both halves of this problem: moderation decisions over marketplace comments, avatars and image uploads, and field extraction from suppli…

## What’s new and why it matters
Use one chat model behind one API key, with a strict JSON schema on every call, for both halves of this problem: moderation decisions over marketplace comments, avatars and image uploads, and field extraction from supplier invoices. That architecture is boring, and boring is the recommendation. The argument worth having is about the operating bill it produces at volume, because the token line is the smallest number on it. The system I have in mind is a mid-size game studio. Players trade skins and accounts in an in-game marketplace, which means user text (listings, comments), user images (avat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emersonprice3718/what-wrong-json-costs-chat-model-text-and-image-moderation-under-one-api-key-2b7p

## Related notes
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
