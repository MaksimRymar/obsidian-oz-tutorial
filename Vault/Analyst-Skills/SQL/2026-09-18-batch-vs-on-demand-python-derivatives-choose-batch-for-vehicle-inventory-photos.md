---
title: Batch vs On-Demand Python Derivatives — Choose Batch for Vehicle Inventory
  Photos
date: '2026-09-18'
source: https://dev.to/griffinhayes3461/batch-vs-on-demand-python-derivatives-choose-batch-for-vehicle-inventory-photos-ecp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-09-04-pdf-image-asset-extraction-endpoints-auditable-batch-jobs-across-saas-regions]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-11-a-simple-openai-compatible-python-backend-api-for-prompt-to-image-marketing-assets]]'
- '[[2026-09-09-construction-progress-images-metadata-archives-vs-lightweight-python-ocr-reports]]'
status: unread
---

> **TL;DR:** Short answer: use batch processing when every vehicle photo must produce the same channel-specific derivatives; use on-demand processing when the variant set is sparse, unpredictable, or dominated by one-off requests. Fo…

## What’s new and why it matters
Short answer: use batch processing when every vehicle photo must produce the same channel-specific derivatives; use on-demand processing when the variant set is sparse, unpredictable, or dominated by one-off requests. For an automotive inventory feed, the decisive number is not the image API's unit price. It is bytes delivered over the full listing lifetime, followed by the integration and operating work required to keep each marketplace's outputs correct. Start with source count, expected views, derivative dimensions, encoded bytes, regeneration frequency, and retention. If delivery bandwidth…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/griffinhayes3461/batch-vs-on-demand-python-derivatives-choose-batch-for-vehicle-inventory-photos-ecp

## Related notes
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-09-04-pdf-image-asset-extraction-endpoints-auditable-batch-jobs-across-saas-regions]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-11-a-simple-openai-compatible-python-backend-api-for-prompt-to-image-marketing-assets]]
- [[2026-09-09-construction-progress-images-metadata-archives-vs-lightweight-python-ocr-reports]]
