---
title: The Arabic PDF bug was never in my code — it was the library version
date: '2026-08-19'
source: https://dev.to/support_confileo_ce7442eb/the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version-8a9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
status: unread
---

> **TL;DR:** In my last post I wrote about why Arabic comes out of PDF extraction in reverse word order. A commenter asked the obvious follow-up question, and it is the one I want to answer properly: Did you end up running a full bid…

## What’s new and why it matters
In my last post I wrote about why Arabic comes out of PDF extraction in reverse word order. A commenter asked the obvious follow-up question, and it is the one I want to answer properly: Did you end up running a full bidi pass, or approximating with run-level heuristics? That mixed-direction case is usually where the heuristics fall apart. Neither. And that turned out to be the whole point. What I thought the problem was The naive mental model goes like this: the PDF stores glyphs in the order they were painted, painting for RTL text runs right-to-left, so extraction hands you a line that read…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/support_confileo_ce7442eb/the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version-8a9

## Related notes
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
