---
title: 'SQLite as my CMS: three gates that stop me shipping broken static sites'
date: '2026-11-21'
source: https://dev.to/jun_liu_ca219b73a8f1489b5/sqlite-as-my-cms-three-gates-that-stop-me-shipping-broken-static-sites-555c
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** I run a bilingual site — English and Chinese, 170+ long articles, all static HTML. No CMS, no admin panel, no React. The only "database" is a single SQLite file sitting in the repo, and a PHP CLI turns it into a dist/ fo…

## What’s new and why it matters
I run a bilingual site — English and Chinese, 170+ long articles, all static HTML. No CMS, no admin panel, no React. The only "database" is a single SQLite file sitting in the repo, and a PHP CLI turns it into a dist/ folder that gets uploaded. This is not a "look how clever my stack is" post. It is a list of the things that broke, and the specific gates I added so they stop breaking. If you generate any volume of content into static HTML, most of this will apply to you regardless of language. Why SQLite and not a CMS The first version used a headless CMS. It lasted about three weeks. The prob…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jun_liu_ca219b73a8f1489b5/sqlite-as-my-cms-three-gates-that-stop-me-shipping-broken-static-sites-555c

## Related notes
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
