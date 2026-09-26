---
title: NL-to-SQL tools will happily DROP your table. Screen the output.
date: '2026-09-26'
source: https://dev.to/lixingliangsy/nl-to-sql-tools-will-happily-drop-your-table-screen-the-output-42mi
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
status: unread
---

> **TL;DR:** I gave an NL-to-SQL tool a fairly boring request once: "show me the ten most recent orders." It produced a clean query. I was pleased. Then, mostly as a joke, I asked it to "clean up the orders table" and watched it prod…

## What’s new and why it matters
I gave an NL-to-SQL tool a fairly boring request once: "show me the ten most recent orders." It produced a clean query. I was pleased. Then, mostly as a joke, I asked it to "clean up the orders table" and watched it produce a DELETE FROM orders with no WHERE clause. Not a joke anymore. That's the whole problem with natural-language-to-SQL in one paragraph. The model is good at translating intent into SQL, and it is equally good at translating bad intent, or a vague sentence, into something destructive. The fix that actually works I don't trust an LLM to review its own SQL. What I trust is a du…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lixingliangsy/nl-to-sql-tools-will-happily-drop-your-table-screen-the-output-42mi

## Related notes
- [[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
