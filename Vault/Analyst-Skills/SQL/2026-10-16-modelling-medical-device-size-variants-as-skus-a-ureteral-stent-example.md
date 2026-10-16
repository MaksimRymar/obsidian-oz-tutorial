---
title: 'Modelling Medical Device Size Variants as SKUs: A Ureteral Stent Example'
date: '2026-10-16'
source: https://dev.to/spgmedisafe/modelling-medical-device-size-variants-as-skus-a-ureteral-stent-example-5de1
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-26-python-pandas-dataframe-a-beginners-guide]]'
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
- '[[2026-07-29-python-part-2]]'
- '[[2026-09-10-utc-offsets-are-not-integers-a-remote-job-feed-with-575-in-it]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
status: unread
---

> **TL;DR:** Medical device catalogues have a recurring design problem: one product, many size variants. A ureteral stent might come in six diameters, a dozen lengths and three materials, which quickly turns into dozens of SKUs. Here…

## What’s new and why it matters
Medical device catalogues have a recurring design problem: one product, many size variants. A ureteral stent might come in six diameters, a dozen lengths and three materials, which quickly turns into dozens of SKUs. Here is a simple way to model that cleanly so search, filters and imports stay predictable. The shape of the data A stent variant is defined by a few attributes that buyers filter on: diameter in Fr, length in cm and material. Everything else, such as sterility and shelf life, usually belongs to the product, not the variant. from dataclasses import dataclass from itertools import p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/spgmedisafe/modelling-medical-device-size-variants-as-skus-a-ureteral-stent-example-5de1

## Related notes
- [[2026-09-26-python-pandas-dataframe-a-beginners-guide]]
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
- [[2026-07-29-python-part-2]]
- [[2026-09-10-utc-offsets-are-not-integers-a-remote-job-feed-with-575-in-it]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
