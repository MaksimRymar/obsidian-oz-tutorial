---
title: PostgreSQL 19：用 WAIT FOR LSN 实现“读己之写”
date: '2026-11-19'
source: https://dev.to/arthur1988/postgresql-19yong-wait-for-lsn-shi-xian-du-ji-zhi-xie--2147
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-01-postgresql-2f004-error-causes-and-solutions-complete-guide]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-03-20-sql-triggers-for-blocking]]'
- '[[2026-06-25-postgresql-25p03-error-causes-and-solutions-complete-guide]]'
- '[[2026-11-08-sql-for-beginners-ask-your-database-any-question-in-plain-english-like-queries]]'
- '[[2026-10-18-introduction-to-databases-and-sql-with-postgresql-window-functions-joins-ctes-and-subqueries-on-a-simple-hospital-databa]]'
status: unread
---

> **TL;DR:** 在读写分离架构中，应用把写入交给主库，把查询交给备库。但如果备库尚未回放最新写入，用户随后发起的查询就可能看不到自己刚修改的数据。 这也是适合在 写好标智库 讨论的一类数据库工程问题：如何在使用备库承担读取的同时，让用户看见自己刚完成的修改？ PostgreSQL 19 新增的 WAIT FOR LSN 命令，针对的正是这种“读己之写”（read-your-writes）一致性需求。 核心思路：查询前，先等备库追上 WAIT FOR L…

## What’s new and why it matters
在读写分离架构中，应用把写入交给主库，把查询交给备库。但如果备库尚未回放最新写入，用户随后发起的查询就可能看不到自己刚修改的数据。 这也是适合在 写好标智库 讨论的一类数据库工程问题：如何在使用备库承担读取的同时，让用户看见自己刚完成的修改？ PostgreSQL 19 新增的 WAIT FOR LSN 命令，针对的正是这种“读己之写”（read-your-writes）一致性需求。 核心思路：查询前，先等备库追上 WAIT FOR LSN 允许备库上的会话等待，直到备库将预写日志（WAL）回放到指定的日志序列号（LSN），再继续执行后续查询。 应用的处理流程可以拆成两步： 在主库完成写入后，记录对应的 WAL 位置。 后续请求访问备库时，先等待备库回放到该位置，再读取数据。 关键不在于假设复制足够快，而在于给读取设置一个明确的前提： 备库已经回放了这次写入。 使用示例 先在主库上更新数据，并获取当前的 WAL 插入位置： UPDATE movie SET genre = 'Dramatic' WHERE genre = 'Drama' ; SELECT pg_current_wal_insert_lsn ( ) ; 这里应确保写入已经提交，再获取供后续请求使用的位置；例如，按自动提交模式依次执行上述语句。 第二条语句会返回类似 0/0306EE20 的值。应用需要保存这个位置，例…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arthur1988/postgresql-19yong-wait-for-lsn-shi-xian-du-ji-zhi-xie--2147

## Related notes
- [[2026-09-01-postgresql-2f004-error-causes-and-solutions-complete-guide]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-03-20-sql-triggers-for-blocking]]
- [[2026-06-25-postgresql-25p03-error-causes-and-solutions-complete-guide]]
- [[2026-11-08-sql-for-beginners-ask-your-database-any-question-in-plain-english-like-queries]]
- [[2026-10-18-introduction-to-databases-and-sql-with-postgresql-window-functions-joins-ctes-and-subqueries-on-a-simple-hospital-databa]]
