---
title: A Small State Machine for Leave Approval Policy
date: '2026-10-02'
source: https://dev.to/sourcebento/a-small-state-machine-for-leave-approval-policy-2cej
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-08-06-batch-moderation-for-existing-posts-and-comments-bulk-llm-classification-jobs]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-scheduled-daily-report-email-backend-property-renewal-guarantees-with-cron-and-queues]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** Separate request lifecycle from eligibility rules, balance accounting, approval authority, and recorded exceptions. A leave request looks like a form with two buttons until the rules become interesting. An employee chang…

## What’s new and why it matters
Separate request lifecycle from eligibility rules, balance accounting, approval authority, and recorded exceptions. A leave request looks like a form with two buttons until the rules become interesting. An employee changes teams while a request is pending. Two requests compete for the same balance. A manager approves an exception, then somebody changes the dates. If those cases are handled through scattered conditionals, the application gradually loses a coherent answer to a basic question: what did this approval authorize? This article was drafted with AI assistance, then fact-checked and edi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sourcebento/a-small-state-machine-for-leave-approval-policy-2cej

## Related notes
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-08-06-batch-moderation-for-existing-posts-and-comments-bulk-llm-classification-jobs]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-scheduled-daily-report-email-backend-property-renewal-guarantees-with-cron-and-queues]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
