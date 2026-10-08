---
title: The refund arrived after the payout, so the fix was two nullable columns and
  no code
date: '2026-10-08'
source: https://dev.to/daniel_pertu/the-refund-arrived-after-the-payout-so-the-fix-was-two-nullable-columns-and-no-code-69a
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
status: unread
---

> **TL;DR:** CogniPrep pays creators a commission when someone buys through their code. The policy is published in our terms, and you can read it on cogniprep.app/terms , section 7.2: Commission accrues only when a payment completes,…

## What’s new and why it matters
CogniPrep pays creators a commission when someone buys through their code. The policy is published in our terms, and you can read it on cogniprep.app/terms , section 7.2: Commission accrues only when a payment completes, and is reversed if that payment is later refunded or charged back Payouts are made manually, in batches, to the payout email you gave us Those two lines are comfortable next to each other right up to the moment the order changes. Refund before the payout and the reversal is a status change on a row nobody has been paid for. Refund after the payout and the money has already lef…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/the-refund-arrived-after-the-payout-so-the-fix-was-two-nullable-columns-and-no-code-69a

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
