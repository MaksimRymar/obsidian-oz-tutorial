---
title: 【完全無料・サーバーレス】AWS Lambda FastAPI で作る「お出かけホテル検索マップ」の手順
date: '2026-10-09'
source: https://dev.to/_ad122393ca44f5a698b1/wan-quan-wu-liao-sabaresu-aws-lambda-fastapi-dezuo-ruochu-kakehoterujian-suo-matupu-noshou-shun-bj3
domain: Python
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-14-build-a-rest-api-in-10-minutes-with-fastapi-and-python]]'
- '[[2026-07-29-python-part-2]]'
- '[[2026-02-28-delete-itemsid-removing-data-from-your-api-with-fastapi]]'
- '[[2026-08-21-save-10-hours-a-week-with-oxygen-data-automation]]'
- '[[2026-09-28-detect-500-errors-in-server-logs-with-python-in-10-lines]]'
- '[[2026-07-14-serverless-python-deploying-fastapi-to-google-cloud-run-with-docker]]'
status: unread
---

> **TL;DR:** こんにちは！今回は、自宅の重いサーバーや有料のホスティング環境を使わず、AWS Lambdaの永年無料枠を活用して、ほぼ完全無料（サーバー代0円）で動くホテル検索マップアプリを個人開発したので、その仕組みと作り方をシェアしたいと思います。 hotel map フロントエンドの地図操作から、バックエンドのPython（FastAPI）、そして安全に公開するためのセキュリティ対策までギュッとまとめました。 このアプリで実現したこと・アーキテ…

## What’s new and why it matters
こんにちは！今回は、自宅の重いサーバーや有料のホスティング環境を使わず、AWS Lambdaの永年無料枠を活用して、ほぼ完全無料（サーバー代0円）で動くホテル検索マップアプリを個人開発したので、その仕組みと作り方をシェアしたいと思います。 hotel map フロントエンドの地図操作から、バックエンドのPython（FastAPI）、そして安全に公開するためのセキュリティ対策までギュッとまとめました。 このアプリで実現したこと・アーキテクチャ 地図上で中心地を選ぶと、その周辺にあるホテルを自動で検索して一覧・マップ表示してくれるアプリです。 フロントエンド: HTML / JavaScript （Google Mapsをインタラクティブに操作） バックエンド: Python 3.11 ＋ FastAPI インフラ（ホスティング）: AWS Lambda（関数URL）＋ Mangum 外部API: SerpAPI（Google Hotels） 「サーバーレス」構成にすることで、アクセスがないときの維持費は完全0円。個人開発のサービス公開やポートフォリオにぴったりの構成です。 実装のポイントとハマりどころ 今回の開発でこだわったポイントや、実際に躓きやすいポイントをいくつか紹介します。 ① 重いSDKを排除し、requests 直叩きで軽量化 AWS Lambdaで動かす際、パッケージ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_ad122393ca44f5a698b1/wan-quan-wu-liao-sabaresu-aws-lambda-fastapi-dezuo-ruochu-kakehoterujian-suo-matupu-noshou-shun-bj3

## Related notes
- [[2026-05-14-build-a-rest-api-in-10-minutes-with-fastapi-and-python]]
- [[2026-07-29-python-part-2]]
- [[2026-02-28-delete-itemsid-removing-data-from-your-api-with-fastapi]]
- [[2026-08-21-save-10-hours-a-week-with-oxygen-data-automation]]
- [[2026-09-28-detect-500-errors-in-server-logs-with-python-in-10-lines]]
- [[2026-07-14-serverless-python-deploying-fastapi-to-google-cloud-run-with-docker]]
