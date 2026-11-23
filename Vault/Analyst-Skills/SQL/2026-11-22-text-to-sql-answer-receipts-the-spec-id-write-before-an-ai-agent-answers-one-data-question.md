---
title: 'Text-to-SQL answer receipts: the spec I''d write before an AI agent answers
  one data question'
date: '2026-11-22'
source: https://dev.to/prachitparikh/text-to-sql-answer-receipts-the-spec-id-write-before-an-ai-agent-answers-one-data-question-1jm2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#presentations'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** Picture a sales director typing into the new AI data assistant on a Monday morning: "What was revenue last month?" A number comes back in four seconds. $8,550. Clean, confident, no caveats. She pastes it into a deck for…

## What’s new and why it matters
Picture a sales director typing into the new AI data assistant on a Monday morning: "What was revenue last month?" A number comes back in four seconds. $8,550. Clean, confident, no caveats. She pastes it into a deck for the 10 AM leadership call. Finance's number for the same month is $5,550. Nobody wrote bad SQL. The agent's query ran. It joined nothing it shouldn't have, and it didn't make up a table. It picked one reasonable reading of "revenue last month" out of at least five, and it didn't tell anyone it had picked. In the fixture below, those five readings range from $5,550 to $8,550, a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prachitparikh/text-to-sql-answer-receipts-the-spec-id-write-before-an-ai-agent-answers-one-data-question-1jm2

## Related notes
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
