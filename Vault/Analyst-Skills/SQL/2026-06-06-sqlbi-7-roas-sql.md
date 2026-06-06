---
title: 광고 SQL·BI 안티패턴 7가지 — ROAS 보고서를 거짓말로 만드는 SQL 함정
date: '2026-06-06'
source: https://dev.to/hyunseok_jeong_d7cdc52c4f/gwanggo-sqlbi-antipaeteon-7gaji-roas-bogoseoreul-geojismalro-mandeuneun-sql-hamjeong-48gl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-23-the-jwt-deception-stateless-auth-and-the-hybrid-cookie-defense]]'
- '[[2026-04-26-postgres-database-data-types-in-postgres-and-the-write-penalty-2026]]'
- '[[2026-04-07-postgresql-explain-analyze-reading-query-plans-like-a-pro]]'
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
- '[[2026-04-24-machine-to-machine---api-keys-oauth-20-and-the-death-of-10-2026]]'
status: unread
---

> **TL;DR:** "Meta는 ROAS 5.2라는데, GA4는 3.8이고, BI팀이 BigQuery로 다시 뽑은 건 9.6이에요." 어느 회의에서나 흔한 풍경입니다. 셋 다 다른 데이터를 봤다면 차이가 나는 게 당연한데, 진짜 무서운 건 같은 raw event를 두 사람이 SQL로 집계했는데 ROAS가 30% 차이 나는 경우입니다. 거의 모든 경우 원인은 데이터가 아니라 SQL 한 줄 이에요. 이 글은 광고…

## What’s new and why it matters
"Meta는 ROAS 5.2라는데, GA4는 3.8이고, BI팀이 BigQuery로 다시 뽑은 건 9.6이에요." 어느 회의에서나 흔한 풍경입니다. 셋 다 다른 데이터를 봤다면 차이가 나는 게 당연한데, 진짜 무서운 건 같은 raw event를 두 사람이 SQL로 집계했는데 ROAS가 30% 차이 나는 경우입니다. 거의 모든 경우 원인은 데이터가 아니라 SQL 한 줄 이에요. 이 글은 광고 데이터를 SQL로 집계할 때 마케터·BI팀이 반복적으로 빠지는 7가지 안티패턴을 정리합니다. 각각 어떻게 ROAS를 왜곡하는지, 어떻게 잡는지까지. 왜 SQL 한 줄이 ROAS 30%를 바꾸나 광고 데이터는 다른 도메인 데이터와 결이 다릅니다. 한 유저가 같은 캠페인을 4번 보고, 그 사이에 3번 사이트를 들렀다가, 마지막에 다른 디바이스로 구매하는 일이 일상입니다. 이걸 표 한 장으로 만들 때 SQL은 마법을 부려야 합니다. impression·click·event 테이블이 따로 attribution window가 채널마다 다름 같은 user가 cookie·gaid·email_hash로 흩어져 있음 광고비는 매체 통화, 매출은 자사 통화 보고 시점마다 conversion…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hyunseok_jeong_d7cdc52c4f/gwanggo-sqlbi-antipaeteon-7gaji-roas-bogoseoreul-geojismalro-mandeuneun-sql-hamjeong-48gl

## Related notes
- [[2026-04-23-the-jwt-deception-stateless-auth-and-the-hybrid-cookie-defense]]
- [[2026-04-26-postgres-database-data-types-in-postgres-and-the-write-penalty-2026]]
- [[2026-04-07-postgresql-explain-analyze-reading-query-plans-like-a-pro]]
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
- [[2026-04-24-machine-to-machine---api-keys-oauth-20-and-the-death-of-10-2026]]
