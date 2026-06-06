---
title: GA4 + BigQuery로 ROAS 파이프라인 직접 만들기 — 플랫폼 대시보드 못 믿을 때
date: '2026-06-06'
source: https://dev.to/hyunseok_jeong_d7cdc52c4f/ga4-bigqueryro-roas-paipeurain-jigjeob-mandeulgi-peulraespom-daesibodeu-mos-mideul-ddae-4f9m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-06-06-sqlbi-7-roas-sql]]'
- '[[2026-04-28-arrayjoin-in-clickhouse-why-your-rows-are-duplicating-and-how-to-control-it]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-05-07-post-de-teste---recursos-do-blog]]'
- '[[2026-06-03-sql-for-developers-the-practical-guide-2026]]'
status: unread
---

> **TL;DR:** "Meta는 ROAS 5.2라는데, GA4는 3.8이고, BigQuery 우리 자체 집계는 4.5예요. 어느 게 맞는 거죠?" — 데이터 분석가가 회의에서 이런 답을 내놓으면 마케터는 멘붕이에요. 사실 셋 다 다른 데이터·다른 정의로 답하고 있어서 모두 틀리지 않아요. 이 글은 그 혼란을 끝내는 가장 깔끔한 답 — GA4 → BigQuery 익스포트로 직접 ROAS 파이프라인을 만드는 4단계…

## What’s new and why it matters
"Meta는 ROAS 5.2라는데, GA4는 3.8이고, BigQuery 우리 자체 집계는 4.5예요. 어느 게 맞는 거죠?" — 데이터 분석가가 회의에서 이런 답을 내놓으면 마케터는 멘붕이에요. 사실 셋 다 다른 데이터·다른 정의로 답하고 있어서 모두 틀리지 않아요. 이 글은 그 혼란을 끝내는 가장 깔끔한 답 — GA4 → BigQuery 익스포트로 직접 ROAS 파이프라인을 만드는 4단계 SQL 입니다. 플랫폼 ROAS는 추정, GA4 UI는 가공된 요약. BigQuery raw event는 원천이다. 직접 SQL을 써야 비로소 우리 데이터가 된다. 왜 직접 만들어야 하나 플랫폼·도구별 ROAS의 한계: 출처 장점 한계 Meta/Google Ads UI 실시간, 캠페인 분해 쉬움 last-click + view-through, 본인 플랫폼 광고만 GA4 UI 채널 통합, last-click 또는 data-driven 표본 추출 적용, 14개월 보관, 수정 불가 BigQuery raw export 원천 데이터, 무한 보관, 자유 정의 SQL 직접 짜야 함 자체 파이프라인의 진짜 가치는 "플랫폼이 안 보여주는 정의"를 자유롭게 만들 수 있다는 거예요. "브랜…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hyunseok_jeong_d7cdc52c4f/ga4-bigqueryro-roas-paipeurain-jigjeob-mandeulgi-peulraespom-daesibodeu-mos-mideul-ddae-4f9m

## Related notes
- [[2026-06-06-sqlbi-7-roas-sql]]
- [[2026-04-28-arrayjoin-in-clickhouse-why-your-rows-are-duplicating-and-how-to-control-it]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-05-07-post-de-teste---recursos-do-blog]]
- [[2026-06-03-sql-for-developers-the-practical-guide-2026]]
