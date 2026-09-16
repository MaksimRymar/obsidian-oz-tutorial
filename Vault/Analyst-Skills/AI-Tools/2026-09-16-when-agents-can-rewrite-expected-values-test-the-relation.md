---
title: When Agents Can Rewrite Expected Values, Test the Relation
date: '2026-09-16'
source: https://dev.to/datacpp_8185/when-agents-can-rewrite-expected-values-test-the-relation-1k7c
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
status: unread
---

> **TL;DR:** Agent patches fail a common class of tests without failing the product. The suite still reports green. The expected value moved with the code. A merge gate that stores answers in the same tree the agent can edit is not a…

## What’s new and why it matters
Agent patches fail a common class of tests without failing the product. The suite still reports green. The expected value moved with the code. A merge gate that stores answers in the same tree the agent can edit is not a gate. It is a mirror. The durable alternative is a metamorphic relation: a rule that ties two executions together without naming the correct output. The agent can rewrite helpers, comments, and even nearby tests. It cannot satisfy the relation by editing a literal. That is the conclusion this article starts from, and the rest is a workflow to make it checkable. Why golden file…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/when-agents-can-rewrite-expected-values-test-the-relation-1k7c

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
