---
title: RBAC SQL table create
date: '2026-09-13'
source: https://dev.to/yyt0901/rbac-sql-table-create-2ii7
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-04-15-example-of-e-commice-sql-in-that-specilises-in-the-food-industry]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-simple-mysql-example-for-e-commice]]'
- '[[2026-03-24-sql-example]]'
- '[[2026-03-29-ca-40---alter-tables]]'
- '[[2026-03-29-create-tables]]'
status: unread
---

> **TL;DR:** the core is: User ↔ Role ↔ Permission 表结构总览 sys_user 用户表 sys_role 角色表 sys_permission 权限表（菜单/按钮/接口） sys_user_role 用户-角色关联表（多对多） sys_role_permission 角色-权限关联表（多对多） 1. sys_user CREATE TABLE `sys_user` ( `id` bigint NOT NULL…

## What’s new and why it matters
the core is: User ↔ Role ↔ Permission 表结构总览 sys_user 用户表 sys_role 角色表 sys_permission 权限表（菜单/按钮/接口） sys_user_role 用户-角色关联表（多对多） sys_role_permission 角色-权限关联表（多对多） 1. sys_user CREATE TABLE `sys_user` ( `id` bigint NOT NULL COMMENT '用户ID' , `username` varchar ( 50 ) NOT NULL COMMENT '登录账号' , `password` varchar ( 100 ) NOT NULL COMMENT '密码（加密存储，如BCrypt）' , `nickname` varchar ( 50 ) DEFAULT NULL COMMENT '昵称' , `avatar` varchar ( 255 ) DEFAULT NULL COMMENT '头像' , `phone` varchar ( 20 ) DEFAULT NULL COMMENT '手机号' , `email` varchar ( 100 ) DEFAULT NULL COMMENT '邮箱' , `gender` tinyint DEFAULT NULL COMME…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yyt0901/rbac-sql-table-create-2ii7

## Related notes
- [[2026-04-15-example-of-e-commice-sql-in-that-specilises-in-the-food-industry]]
- [[2026-03-26-create-tables]]
- [[2026-03-26-simple-mysql-example-for-e-commice]]
- [[2026-03-24-sql-example]]
- [[2026-03-29-ca-40---alter-tables]]
- [[2026-03-29-create-tables]]
