---
title: 'Çağrı sonucu kodlamayı kodla kurmak: İki katmanlı model, santral CDR eşlemesi
  ve kural tablosuyla sonraki deneme'
date: '2026-11-21'
source: https://dev.to/korayyalcin/cagri-sonucu-kodlamayi-kodla-kurmak-iki-katmanli-model-santral-cdr-eslemesi-ve-kural-tablosuyla-2io
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-11-15-multi-touch-attribution-sql-ile-kurmak-temas-tablosu-geriye-bak-penceresi-kredi-modelleri-ve-mutabakat]]'
- '[[2026-11-19-9-gn-boyunca-bist-verisi-iledim-sonucu-u-oldu]]'
- '[[2026-07-18-postgresqlde-yava-sorgular-explain-analyze-ile-zmek]]'
- '[[2026-11-02-sql-serverda-yava-sorgu-nasl-hzlandrlr]]'
- '[[2026-06-14-pep-20]]'
- '[[2026-02-25-yazlmda-yazlm-mimarisinde-veritaban-normalizasyonu-ve-den]]'
status: unread
---

> **TL;DR:** Bir satış ofisinin arama kayıtlarına baktığımda genellikle aynı tabloyla karşılaşıyorum: her çağrının yanında danışmanın seçtiği bir sonuç var, ama "Ulaşılamadı" seçeneği hem telefonun hiç çalmadığı durumları hem meşgul…

## What’s new and why it matters
Bir satış ofisinin arama kayıtlarına baktığımda genellikle aynı tabloyla karşılaşıyorum: her çağrının yanında danışmanın seçtiği bir sonuç var, ama "Ulaşılamadı" seçeneği hem telefonun hiç çalmadığı durumları hem meşgul hattı hem de müşterinin açıp "şimdi müsait değilim" dediği görüşmeleri kapsıyor. Sonra biri "ulaşma oranımız neden düştü" diye soruyor ve kimse cevap veremiyor, çünkü veri aslında üç farklı olayı tek bir kelimeye sıkıştırmış durumda. Ben Koray Yalçın; lead yönetimi, CRM ve pazarlama otomasyonu altyapıları kuruyorum, ağırlıklı olarak gayrimenkul projelerinde reklamdan satış ofis…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/korayyalcin/cagri-sonucu-kodlamayi-kodla-kurmak-iki-katmanli-model-santral-cdr-eslemesi-ve-kural-tablosuyla-2io

## Related notes
- [[2026-11-15-multi-touch-attribution-sql-ile-kurmak-temas-tablosu-geriye-bak-penceresi-kredi-modelleri-ve-mutabakat]]
- [[2026-11-19-9-gn-boyunca-bist-verisi-iledim-sonucu-u-oldu]]
- [[2026-07-18-postgresqlde-yava-sorgular-explain-analyze-ile-zmek]]
- [[2026-11-02-sql-serverda-yava-sorgu-nasl-hzlandrlr]]
- [[2026-06-14-pep-20]]
- [[2026-02-25-yazlmda-yazlm-mimarisinde-veritaban-normalizasyonu-ve-den]]
