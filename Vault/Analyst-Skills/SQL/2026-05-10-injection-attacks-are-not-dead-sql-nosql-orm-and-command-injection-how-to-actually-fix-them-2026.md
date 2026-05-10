---
title: 'Injection Attacks Are Not Dead: SQL, NoSQL, ORM, and Command Injection — How
  to Actually Fix Them (2026)'
date: '2026-05-10'
source: https://dev.to/mahdi0shamlou/injection-attacks-are-not-dead-sql-nosql-orm-and-command-injection-how-to-actually-fix-them-f89
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
status: unread
---

> **TL;DR:** Mahdi Shamlou here. “Mahdi, I finally launched my e‑commerce site. And don’t worry — I used MongoDB, so no SQL injection. You can’t hack it.” I laughed. Then I asked him to let me try. Within 10 minutes, I bypassed his l…

## What’s new and why it matters
Mahdi Shamlou here. “Mahdi, I finally launched my e‑commerce site. And don’t worry — I used MongoDB, so no SQL injection. You can’t hack it.” I laughed. Then I asked him to let me try. Within 10 minutes, I bypassed his login with a NoSQL injection and pulled out his entire user collection. His face went pale. Moral of the story: “No SQL” does NOT mean “no injection”. Injection is a whole class of attacks — SQL, NoSQL, ORM, command, LDAP, you name it. If you concatenate user input into any kind of query or system command, you’re likely vulnerable. In this guide, I’ll show you: How I hacked my f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mahdi0shamlou/injection-attacks-are-not-dead-sql-nosql-orm-and-command-injection-how-to-actually-fix-them-f89

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
