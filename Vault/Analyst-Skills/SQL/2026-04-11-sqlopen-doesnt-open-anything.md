---
title: sql.Open() doesn't open anything
date: '2026-04-11'
source: https://dev.to/areesh_zafar/sqlopen-doesnt-open-anything-50ch
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-25-sql-notebooks-in-vs-code-like-jupyter-but-for-databases]]'
- '[[2026-02-25-finally-stopped-guessing-my-betaflight-pids---heres-what-worked]]'
- '[[2026-03-24-a-day-in-the-life-of-a-data-engineer-real-talk-no-filter]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
status: unread
---

> **TL;DR:** We all know the basic drill of connecting a db in Go: func main (){ //... dsn := flag . String ( "dsn" , "web:password@/demoProject" , "MySQL data source name" ) flag . Parse () db , err := openDB ( * dsn ) if err != nil…

## What’s new and why it matters
We all know the basic drill of connecting a db in Go: func main (){ //... dsn := flag . String ( "dsn" , "web:password@/demoProject" , "MySQL data source name" ) flag . Parse () db , err := openDB ( * dsn ) if err != nil { errorLog . Fatal ( err ) } defer db . Close () //... } func openDB ( dsn string ) ( * sql . DB , error ) { db , err := sql . Open ( "mysql" , dsn ) if err != nil { return nil , err } if err = db . Ping (); err != nil { return nil , err } return db , nil } but do u know what happens under the hood, u might intuitively think its pretty much clear that the sql.Open opens the co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/areesh_zafar/sqlopen-doesnt-open-anything-50ch

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-25-sql-notebooks-in-vs-code-like-jupyter-but-for-databases]]
- [[2026-02-25-finally-stopped-guessing-my-betaflight-pids---heres-what-worked]]
- [[2026-03-24-a-day-in-the-life-of-a-data-engineer-real-talk-no-filter]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
