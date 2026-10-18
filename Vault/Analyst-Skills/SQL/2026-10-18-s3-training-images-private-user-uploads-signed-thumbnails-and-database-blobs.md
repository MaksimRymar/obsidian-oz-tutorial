---
title: 'S3 Training Images: Private User Uploads, Signed Thumbnails, and Database
  Blobs'
date: '2026-10-18'
source: https://dev.to/zekecross3245/s3-training-images-private-user-uploads-signed-thumbnails-and-database-blobs-1m76
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-24-feature-flag-kill-switches-reconstructing-repeated-ai-agent-failures]]'
- '[[2026-10-10-postgres-cleanup-cron-only-vs-queue-workers-for-idempotent-batch-deletes]]'
- '[[2026-10-15-a-vue-upload-workflow-axios-progress-and-private-storage-keys]]'
- '[[2026-10-18-trust-boundaries-store-generated-ai-images-with-temporary-private-downloads]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-18-nodejs-export-authorization-temporary-user-downloads-with-private-object-storage]]'
status: unread
---

> **TL;DR:** Keep the database bill tied to records, not training bytes. TL;DR: put private training artifacts and their derived previews in object storage, keep ownership and retention state in the database, and issue short-lived si…

## What’s new and why it matters
Keep the database bill tied to records, not training bytes. TL;DR: put private training artifacts and their derived previews in object storage, keep ownership and retention state in the database, and issue short-lived signed URLs only after authorization. For a B2B SaaS handling large files, this is the least complex design that gives each artifact a reproducible deletion date without turning database backups and queries into a file-delivery path. Start with the dominant term: retained bytes multiplied by retention time. If ten workspaces each produce 40 GiB of immutable training exports per w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zekecross3245/s3-training-images-private-user-uploads-signed-thumbnails-and-database-blobs-1m76

## Related notes
- [[2026-09-24-feature-flag-kill-switches-reconstructing-repeated-ai-agent-failures]]
- [[2026-10-10-postgres-cleanup-cron-only-vs-queue-workers-for-idempotent-batch-deletes]]
- [[2026-10-15-a-vue-upload-workflow-axios-progress-and-private-storage-keys]]
- [[2026-10-18-trust-boundaries-store-generated-ai-images-with-temporary-private-downloads]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-18-nodejs-export-authorization-temporary-user-downloads-with-private-object-storage]]
