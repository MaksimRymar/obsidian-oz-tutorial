---
title: Turn any web page into typed JSON with an LLM and a JSON Schema (Python)
date: '2026-10-27'
source: https://dev.to/swillz/turn-any-web-page-into-typed-json-with-an-llm-and-a-json-schema-python-1n9l
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
status: unread
---

> **TL;DR:** Writing CSS selectors for every site you want data from gets old fast, and the selectors break when the site changes its markup. For many jobs (a product list, an events page, a team page) it's simpler to give an LLM the…

## What’s new and why it matters
Writing CSS selectors for every site you want data from gets old fast, and the selectors break when the site changes its markup. For many jobs (a product list, an events page, a team page) it's simpler to give an LLM the page text and a schema and let it fill in the fields. The naive version (paste the HTML, ask for JSON) works in a demo and fails in production: the output shape drifts, links vanish, and long pages blow through the context window. This post shows a version that holds up, using a real page you can try: the Travel category of books.toscrape.com , a sandbox site built for scrapin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/swillz/turn-any-web-page-into-typed-json-with-an-llm-and-a-json-schema-python-1n9l

## Related notes
- [[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
