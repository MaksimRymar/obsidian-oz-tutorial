---
title: My security test was green for six weeks because it could not turn red
date: '2026-08-28'
source: https://dev.to/guidondor/my-security-test-was-green-for-six-weeks-because-it-could-not-turn-red-4b0m
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
status: unread
---

> **TL;DR:** I had a SQL test that logged in as two users and checked that neither could read the other's rows. It ran on every push. It was green for about six weeks. Then I broke an assertion on purpose, just to watch it fail. It d…

## What’s new and why it matters
I had a SQL test that logged in as two users and checked that neither could read the other's rows. It ran on every push. It was green for about six weeks. Then I broke an assertion on purpose, just to watch it fail. It didn't fail. It threw a type error on the line that builds the failure message. Every check in that file had been passing into a branch that had never once executed. The line The test collects failures into an array and raises at the end: DECLARE fails text [] : = '{}' ; ... IF v_int <> 1 THEN fails : = fails || 'own profile not visible' ; END IF ; IF v_int <> 0 THEN fails : = f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/guidondor/my-security-test-was-green-for-six-weeks-because-it-could-not-turn-red-4b0m

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
