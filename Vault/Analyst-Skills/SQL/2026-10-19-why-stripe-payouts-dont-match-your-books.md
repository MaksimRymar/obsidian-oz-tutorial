---
title: Why Stripe payouts don't match your books
date: '2026-10-19'
source: https://dev.to/akarazhev/why-stripe-payouts-dont-match-your-books-3aoa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-19-three-way-reconciliation-as-a-data-integrity-check-for-law-firm-trust-accounts]]'
- '[[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** In this synthetic September example, the ledger records €115,824.69 of net Stripe activity — sales less refunds and fees. The bank shows €112,327.70 in Stripe deposits. The gap is €3,496.99, and nothing in the books says…

## What’s new and why it matters
In this synthetic September example, the ledger records €115,824.69 of net Stripe activity — sales less refunds and fees. The bank shows €112,327.70 in Stripe deposits. The gap is €3,496.99, and nothing in the books says where it went. One number cannot explain it, because it is not one problem. In this demo it is eight kinds of difference with opposite signs: €3,347.78 is a payout that reached the bank after the month-end cutoff, and the rest is €684.51 of negative and €535.30 of positive differences between the ledger and Stripe, which mostly cancel out. Reconcile level by level, not in one…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/akarazhev/why-stripe-payouts-dont-match-your-books-3aoa

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-19-three-way-reconciliation-as-a-data-integrity-check-for-law-firm-trust-accounts]]
- [[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
