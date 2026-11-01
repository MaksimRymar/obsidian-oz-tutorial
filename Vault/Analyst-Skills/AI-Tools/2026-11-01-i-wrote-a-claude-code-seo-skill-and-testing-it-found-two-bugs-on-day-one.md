---
title: I Wrote a Claude Code SEO Skill, and Testing It Found Two Bugs on Day One
date: '2026-11-01'
source: https://dev.to/jacobpark/i-wrote-a-claude-code-seo-skill-and-testing-it-found-two-bugs-on-day-one-13po
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]'
status: unread
---

> **TL;DR:** Claude Code skills are just folders. A SKILL.md with a name and a description, plus whatever scripts you want the model to run. When the description matches what you asked for, Claude loads the instructions and follows t…

## What’s new and why it matters
Claude Code skills are just folders. A SKILL.md with a name and a description, plus whatever scripts you want the model to run. When the description matches what you asked for, Claude loads the instructions and follows them. That's the whole mechanism, and it's why SEO is a good fit: most on-page checks are deterministic, and a model is much better at explaining a result than at counting characters in a <title> tag. So I wrote one. It checks a single URL for the on-page basics and hands Claude a JSON report to turn into a fix list. Then I ran it against five real pages and one fake one before…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jacobpark/i-wrote-a-claude-code-seo-skill-and-testing-it-found-two-bugs-on-day-one-13po

## Related notes
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]
