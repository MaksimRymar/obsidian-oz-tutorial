---
title: '"OpenAI-compatible" is a spectrum, not a boolean — here''s an 11-check conformance
  suite'
date: '2026-09-10'
source: https://dev.to/seven7763/openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite-2mhj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-25-openai-compatible-apis-are-great-until-streaming-breaks-what-i-check-before-switching-providers]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
status: unread
---

> **TL;DR:** Two endpoints both say "OpenAI-compatible" on the tin. You point your app at the first one and everything works. You point it at the second one and everything works too — for about a week. Then a streamed tool call comes…

## What’s new and why it matters
Two endpoints both say "OpenAI-compatible" on the tin. You point your app at the first one and everything works. You point it at the second one and everything works too — for about a week. Then a streamed tool call comes back with arguments split across chunks in a way your accumulator didn't expect, your JSON parser throws inside a retry loop, and the retry loop hammers the endpoint because the error body doesn't have the field your backoff code reads. Nothing lied to you. "OpenAI-compatible" was never a boolean. It's a surface area, and every implementation covers a different subset of it. I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/seven7763/openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite-2mhj

## Related notes
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-25-openai-compatible-apis-are-great-until-streaming-breaks-what-i-check-before-switching-providers]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
