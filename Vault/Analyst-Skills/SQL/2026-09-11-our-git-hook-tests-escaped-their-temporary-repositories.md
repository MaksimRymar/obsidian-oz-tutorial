---
title: our git hook tests escaped their temporary repositories
date: '2026-09-11'
source: https://dev.to/arian_gogani1/our-git-hook-tests-escaped-their-temporary-repositories-232k
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-18-after-3-years-of-redis-we-were-testing-ai-agent-memory-expiry-wrong]]'
- '[[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]'
status: unread
---

> **TL;DR:** our pre-push check failed 13 tests. the bigger problem was that some of those tests had changed the repository they were supposed to protect. this happened in Nobulex, the project i maintain. the investigation, fix and t…

## What’s new and why it matters
our pre-push check failed 13 tests. the bigger problem was that some of those tests had changed the repository they were supposed to protect. this happened in Nobulex, the project i maintain. the investigation, fix and this write-up used AI assistance. the tests create temporary Git repositories and run fixture commands inside them. we treated the subprocess working directory as the boundary. that assumption broke when the suite ran from a Git hook in an isolated worktree. Git had exported GIT_DIR into the hook's environment. the test process inherited it. changing cwd to a temporary directory…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arian_gogani1/our-git-hook-tests-escaped-their-temporary-repositories-232k

## Related notes
- [[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-18-after-3-years-of-redis-we-were-testing-ai-agent-memory-expiry-wrong]]
- [[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]
