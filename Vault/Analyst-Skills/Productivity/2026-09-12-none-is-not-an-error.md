---
title: None Is Not an Error
date: '2026-09-12'
source: https://dev.to/jeffthoensen/none-is-not-an-error-f10
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#productivity'
- '#sql'
- '#tool'
related:
- '[[2026-09-02-mutation-test-your-agent-patch-a-budgeted-sandbox-that-costs-you-nothing]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-07-24-alpha-to-beta-bringing-in-qa]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
status: unread
---

> **TL;DR:** I have a small CLI tool that looks up an MLB player's season stats by name. The lookup used to fail without ever raising anything: if the MLB API had no player matching a name, search_player_id printed "Player not found.…

## What’s new and why it matters
I have a small CLI tool that looks up an MLB player's season stats by name. The lookup used to fail without ever raising anything: if the MLB API had no player matching a name, search_player_id printed "Player not found." and returned None, and it was on whoever called it to check for that and stop. If that check gets missed anywhere in the chain, None gets passed into the next function that expected a real player ID. Testing that old version meant capturing whatever the script printed and asserting on the message, then separately checking that the return value was None. Replacing the print-an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jeffthoensen/none-is-not-an-error-f10

## Related notes
- [[2026-09-02-mutation-test-your-agent-patch-a-budgeted-sandbox-that-costs-you-nothing]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-07-24-alpha-to-beta-bringing-in-qa]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
