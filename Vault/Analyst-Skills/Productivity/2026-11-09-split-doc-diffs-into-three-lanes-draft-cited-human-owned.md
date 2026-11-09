---
title: 'Split Doc Diffs Into Three Lanes: Draft, Cited, Human-Owned'
date: '2026-11-09'
source: https://dev.to/github_7727/split-doc-diffs-into-three-lanes-draft-cited-human-owned-1gi2
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-26-review-cost-per-section-decides-who-drafts-it-a-stop-rule-for-model-assisted-docs]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-05-if-a-doc-claim-cannot-compile-do-not-let-a-model-draft-it]]'
status: unread
---

> **TL;DR:** The expensive question in model-drafted documentation is not whether the prose reads well; it is which paragraphs a named human is accountable for after merge. If you cannot answer that from the pull request alone, revie…

## What’s new and why it matters
The expensive question in model-drafted documentation is not whether the prose reads well; it is which paragraphs a named human is accountable for after merge. If you cannot answer that from the pull request alone, review turns into archaeology and nobody signs anything. This workflow answers it mechanically: three lanes, a lane map keyed by section, and a diff check that refuses to let a model touch accountability-bearing text before a reviewer opens the page. The failure this fixes Consider an illustrative scenario rather than a reported incident: a nightly job drafts prose for docs/install.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/github_7727/split-doc-diffs-into-three-lanes-draft-cited-human-owned-1gi2

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-26-review-cost-per-section-decides-who-drafts-it-a-stop-rule-for-model-assisted-docs]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-05-if-a-doc-claim-cannot-compile-do-not-let-a-model-draft-it]]
