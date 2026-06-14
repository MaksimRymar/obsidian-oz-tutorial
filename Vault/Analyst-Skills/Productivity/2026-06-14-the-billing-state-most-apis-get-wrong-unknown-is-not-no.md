---
title: 'The billing state most APIs get wrong: "unknown" is not "no"'
date: '2026-06-14'
source: https://dev.to/larry_johnson_e014cef9ad9/the-billing-state-most-apis-get-wrong-unknown-is-not-no-o9c
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#productivity'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-26-i-did-the-math-your-serpapi-bill-is-10x-what-it-should-be]]'
- '[[2026-05-20-top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside]]'
- '[[2026-05-13-charge-10-sats-per-crewai-tool-call-in-one-line]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** If you bill per result, there is one design decision that quietly decides whether customers trust you: what you do when you could not get an answer. Most usage-billed APIs collapse the world into two states. The call wor…

## What’s new and why it matters
If you bill per result, there is one design decision that quietly decides whether customers trust you: what you do when you could not get an answer. Most usage-billed APIs collapse the world into two states. The call worked, or it failed. Valid or invalid. Found or not found. That binary is where the trust leaks out, because it hides a third state that happens constantly in the real world: you asked, and the system genuinely could not tell you right now. A concrete example Say you run an email verification endpoint. A customer sends an address, you check it, you bill for the answer. Easy. Then…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/larry_johnson_e014cef9ad9/the-billing-state-most-apis-get-wrong-unknown-is-not-no-o9c

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-26-i-did-the-math-your-serpapi-bill-is-10x-what-it-should-be]]
- [[2026-05-20-top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside]]
- [[2026-05-13-charge-10-sats-per-crewai-tool-call-in-one-line]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
