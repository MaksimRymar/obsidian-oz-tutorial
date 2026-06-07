---
title: 'XTK: A Symbolic Expression Toolkit for Term Rewriting'
date: '2026-06-07'
source: https://dev.to/queelius/xtk-a-symbolic-expression-toolkit-for-term-rewriting-cei
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-05-12-i-built-rust-style-adts-in-30-lines-of-python-pattern-matching-works]]'
- '[[2026-03-12-how-to-validate-spanish-nif-nie-cif-and-iban-in-python]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
- '[[2026-05-26-i-built-a-diagnostic-toolkit-for-pytorch-because-i-was-tired-of-guessing-why-models-fail]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-03-19-i-built-visual-execution-tools-for-sql-and-python---heres-why]]'
status: unread
---

> **TL;DR:** XTK (Expression Toolkit) is a Python library for symbolic computation through rule-based term rewriting. You define pattern-skeleton pairs, and the engine rewrites expressions by matching and substituting until it reache…

## What’s new and why it matters
XTK (Expression Toolkit) is a Python library for symbolic computation through rule-based term rewriting. You define pattern-skeleton pairs, and the engine rewrites expressions by matching and substituting until it reaches a normal form. I built this because I kept wanting a lightweight term rewriting system that wasn't Mathematica. Something I could embed in other projects, extend with custom rules, and use from the command line. Quick Start The fastest way to try it is the interactive REPL: pip install xpression-tk python3 -m xtk.cli xtk> ( + 2 3 ) xtk> /rewrite Rewritten: 5 xtk> ( define squ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/queelius/xtk-a-symbolic-expression-toolkit-for-term-rewriting-cei

## Related notes
- [[2026-05-12-i-built-rust-style-adts-in-30-lines-of-python-pattern-matching-works]]
- [[2026-03-12-how-to-validate-spanish-nif-nie-cif-and-iban-in-python]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
- [[2026-05-26-i-built-a-diagnostic-toolkit-for-pytorch-because-i-was-tired-of-guessing-why-models-fail]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-03-19-i-built-visual-execution-tools-for-sql-and-python---heres-why]]
