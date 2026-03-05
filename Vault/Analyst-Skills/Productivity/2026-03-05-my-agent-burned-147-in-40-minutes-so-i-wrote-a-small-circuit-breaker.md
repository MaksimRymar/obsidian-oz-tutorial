---
title: My agent burned $147 in ~40 minutes… so I wrote a small circuit breaker
date: '2026-03-05'
source: https://dev.to/alex_dirochian_59566cbf72/my-agent-burned-147-in-40-minutes-so-i-wrote-a-small-circuit-breaker-6kb
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
related:
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]'
- '[[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]'
- '[[2026-03-02-a-maze-to-solve-when-youre-bored]]'
- '[[2026-03-04-how-i-stopped-my-ai-agents-from-getting-dumber-after-10-turns]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
status: unread
---

> **TL;DR:** I was testing a small agent script last week and it ended up getting stuck retrying a step while streaming responses. It kept calling the API again and again and I didn’t notice for a while. By the time I checked the usa…

## What’s new and why it matters
I was testing a small agent script last week and it ended up getting stuck retrying a step while streaming responses. It kept calling the API again and again and I didn’t notice for a while. By the time I checked the usage it had jumped about $147 in under an hour. After that I wrote a small Python “circuit breaker” that stops requests if a rolling token or cost limit is exceeded. It can also interrupt streaming responses mid-generation. It’s just a single Python file that runs locally. No cloud and no keys leaving your machine. If this might help someone, I shared it here: https://gist.github…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alex_dirochian_59566cbf72/my-agent-burned-147-in-40-minutes-so-i-wrote-a-small-circuit-breaker-6kb

## Related notes
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]
- [[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]
- [[2026-03-02-a-maze-to-solve-when-youre-bored]]
- [[2026-03-04-how-i-stopped-my-ai-agents-from-getting-dumber-after-10-turns]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
