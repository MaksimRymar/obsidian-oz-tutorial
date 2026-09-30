---
title: The Data Was Public. The Agent Path Wasn't. So His Mock Became My Documentation.
date: '2026-09-30'
source: https://dev.to/kenielzep97/the-data-was-public-the-agent-path-wasnt-so-his-mock-became-my-documentation-413a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-25-if-a-list-endpoint-returns-exactly-as-many-rows-as-you-asked-for-you-have-a-bug]]'
status: unread
---

> **TL;DR:** Two commands against the same data. Run them yourself: $ curl -sS --get 'https://u58x3mt0.api.sanity.io/v2025-08-15/data/query/production' \ --data-urlencode 'query=count(*)' { "query" : "count(*)" , "result" :120, "sync…

## What’s new and why it matters
Two commands against the same data. Run them yourself: $ curl -sS --get 'https://u58x3mt0.api.sanity.io/v2025-08-15/data/query/production' \ --data-urlencode 'query=count(*)' { "query" : "count(*)" , "result" :120, "syncTags" :[ "s1:dmd/mg" ] , "ms" :11 } 120 documents, no key, no account. Now the path my agent actually uses: $ curl -sS -o /dev/null -w '%{http_code}\n' \ 'https://api.sanity.io/v1/context/organizations/<ORG>/mcp/self-correcting-systems' 401 Same underlying dataset. One route is publicly queryable. The route my agent takes goes through an authenticated Context MCP endpoint, whic…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kenielzep97/the-data-was-public-the-agent-path-wasnt-so-his-mock-became-my-documentation-413a

## Related notes
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-25-if-a-list-endpoint-returns-exactly-as-many-rows-as-you-asked-for-you-have-a-bug]]
