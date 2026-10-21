---
title: 'Modelling Surgical Instrument Sets as Data: A Dilator Set Example'
date: '2026-10-21'
source: https://dev.to/spgmedisafe/modelling-surgical-instrument-sets-as-data-a-dilator-set-example-4bl6
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-10-16-modelling-medical-device-size-variants-as-skus-a-ureteral-stent-example]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-26-python-pandas-dataframe-a-beginners-guide]]'
- '[[2026-03-26-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
status: unread
---

> **TL;DR:** Surgical instruments are often sold as sets, such as a nephrostomy dilator set with ten or more graduated pieces. If you build a catalogue, an inventory tool or a sterile-processing tracker for a hospital, you quickly fa…

## What’s new and why it matters
Surgical instruments are often sold as sets, such as a nephrostomy dilator set with ten or more graduated pieces. If you build a catalogue, an inventory tool or a sterile-processing tracker for a hospital, you quickly face a design question: how do you model a set and its parts so that shortages, substitutions and reorders are easy to handle? Here is a small approach. Separate the set from its members A set is a template, and the physical tray in a store is an instance of that template. Keeping them apart makes it easy to see what is missing. from dataclasses import dataclass , field @dataclas…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/spgmedisafe/modelling-surgical-instrument-sets-as-data-a-dilator-set-example-4bl6

## Related notes
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-10-16-modelling-medical-device-size-variants-as-skus-a-ureteral-stent-example]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-26-python-pandas-dataframe-a-beginners-guide]]
- [[2026-03-26-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
