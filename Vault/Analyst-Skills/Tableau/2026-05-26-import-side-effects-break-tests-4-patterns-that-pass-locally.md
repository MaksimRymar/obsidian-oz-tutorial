---
title: 'Import Side Effects Break Tests: 4 Patterns That Pass Locally'
date: '2026-05-26'
source: https://dev.to/tildalice/import-side-effects-break-tests-4-patterns-that-pass-locally-3704
domain: Tableau
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#tableau'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-07-pytest-fixtures-that-actually-scale-patterns-from-2-years-of-python-ci-pipelines]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
status: unread
---

> **TL;DR:** The Test That Passed on My Laptop But Failed in CI Your test suite runs green locally. You push to CI. The build fails with AttributeError: module 'app.config' has no attribute 'DATABASE_URL' . You run the exact same tes…

## What’s new and why it matters
The Test That Passed on My Laptop But Failed in CI Your test suite runs green locally. You push to CI. The build fails with AttributeError: module 'app.config' has no attribute 'DATABASE_URL' . You run the exact same test locally again — still passes. This isn't a flaky test or a race condition. It's an import side effect, and it only shows up when test execution order changes. Import side effects are code that runs at module import time and modifies global state. In development, you usually import modules in the same order every time. Your IDE loads them, your manual test runs load them, and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tildalice/import-side-effects-break-tests-4-patterns-that-pass-locally-3704

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-07-pytest-fixtures-that-actually-scale-patterns-from-2-years-of-python-ci-pipelines]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
