---
title: Measuring How Cost Scales by Counting Instead of Timing
date: '2026-09-27'
source: https://dev.to/megapixel99/measuring-how-cost-scales-by-counting-instead-of-timing-lp3
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-09-26-a-curve-fitter-that-refuses-to-answer]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-09-20-ten-packages-one-rule-a-check-must-be-able-to-fail]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
status: unread
---

> **TL;DR:** Code: Megapixel99/countfn Every empirical complexity tool I could find on either registry measures elapsed time. PyPI's big-O estimates the class from execution time, and npm's big-o-calculator times growing inputs and r…

## What’s new and why it matters
Code: Megapixel99/countfn Every empirical complexity tool I could find on either registry measures elapsed time. PyPI's big-O estimates the class from execution time, and npm's big-o-calculator times growing inputs and reports the "probable" complexity; neither can refuse to answer. countfn counts operations instead: hand it a function, a ladder of input sizes, and a builder for the inputs, and it reports how each kind of work grows, or refuses. pip install countfn # or: npm install countfn from countfn import measure , describe report = measure ( binary_search , sizes = [ 64 , 128 , 256 , 512…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/megapixel99/measuring-how-cost-scales-by-counting-instead-of-timing-lp3

## Related notes
- [[2026-09-26-a-curve-fitter-that-refuses-to-answer]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-09-20-ten-packages-one-rule-a-check-must-be-able-to-fail]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
