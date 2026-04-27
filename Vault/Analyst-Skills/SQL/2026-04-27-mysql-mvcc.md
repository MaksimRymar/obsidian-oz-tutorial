---
title: MySQL 的 MVCC：看不见的“时间机器”怎么帮你躲过脏读和幻读？
date: '2026-04-27'
source: https://dev.to/port_smith_378e5d029689f4/mysql-de-mvcckan-bu-jian-de-shi-jian-ji-qi-zen-yao-bang-ni-duo-guo-zang-du-he-huan-du--3gn5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
- '[[2026-03-22-fetch-and-sort-leaderboard-by-difficulty-and-attempts]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]'
- '[[2026-04-01-mariadb-fulltext-searches-and-transactions]]'
- '[[2026-03-26-simple-mysql-example-for-e-commice]]'
status: unread
---

> **TL;DR:** MySQL 的 MVCC：那台你从没启动过，却一直在为你倒带的“时间机器” 你有没有在图书馆借过一本《数据库原理》？翻开时目录还是旧版，而管理员其实在你借走后悄悄上架了修订版——但你完全不受影响。又或者，多人协同编辑一份文档，每人打开时看到的都是自己那一刻的快照，互不干扰。这并非魔法，而是 MySQL InnoDB 引擎中 MVCC（多版本并发控制）在 quietly work：一台无需你点开、不用你设置、却始终为你精准回溯数据状态的“…

## What’s new and why it matters
MySQL 的 MVCC：那台你从没启动过，却一直在为你倒带的“时间机器” 你有没有在图书馆借过一本《数据库原理》？翻开时目录还是旧版，而管理员其实在你借走后悄悄上架了修订版——但你完全不受影响。又或者，多人协同编辑一份文档，每人打开时看到的都是自己那一刻的快照，互不干扰。这并非魔法，而是 MySQL InnoDB 引擎中 MVCC（多版本并发控制）在 quietly work：一台无需你点开、不用你设置、却始终为你精准回溯数据状态的“隐形时间机器”。 一、快照、版本链与 ReadView：MVCC 的三驾马车 InnoDB 从不只存一行数据的一个版本。每行记录自带两个隐藏字段： trx_id （最后修改该行的事务 ID）和 roll_ptr （指向 undo 日志中前一版本的指针），由此串成一条“版本链”。当事务开启，InnoDB 并不复制整库，而是生成一个轻量级的 ReadView ——相当于为这次查询配了一副“专属眼镜”。它记录三项关键信息：当前活跃事务 ID 列表、最小未提交事务 ID（ min_trx_id ）、最大已分配事务 ID（ max_trx_id ）。后续所有普通 SELECT 都依据这套规则判断：“这个版本，我能不能看见？” 判定逻辑极简：仅当某行版本的 trx_id 小于 min_trx_id ，或等于当前事务 ID，或属于已提交且不在活跃列表中的事务，才对…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/port_smith_378e5d029689f4/mysql-de-mvcckan-bu-jian-de-shi-jian-ji-qi-zen-yao-bang-ni-duo-guo-zang-du-he-huan-du--3gn5

## Related notes
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
- [[2026-03-22-fetch-and-sort-leaderboard-by-difficulty-and-attempts]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]
- [[2026-04-01-mariadb-fulltext-searches-and-transactions]]
- [[2026-03-26-simple-mysql-example-for-e-commice]]
