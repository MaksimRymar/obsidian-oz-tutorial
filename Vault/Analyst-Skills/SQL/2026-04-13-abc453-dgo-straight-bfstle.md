---
title: 【ABC453 D】Go Straight 復習メモ：BFSの状態管理とTLE対策
date: '2026-04-13'
source: https://dev.to/iwamutsu256/abc453-d-go-straight-fu-xi-memobfsnozhuang-tai-guan-li-totledui-ce-1eb2
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-25-stanford-is-teaching-the-world-to-code-for-free]]'
- '[[2026-03-01-stop-writing-python-without-type-hints-heres-how-to-start]]'
- '[[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-22-day-1-of-my-90-days-ai-journey-setting-up-the-perfect-environment]]'
- '[[2026-02-24-beginner-friendly-guide-sum-of-root-to-leaf-binary-numbers---problem-1022-c-python-javascript]]'
status: unread
---

> **TL;DR:** まずは結論から。 この問題は単純なBFSではなく、 「直前の移動方向」も状態に含めて管理する 必要があった。 また、Pythonで実装する場合、訪問管理に set() を使うとTLEになるため、 3次元配列による定数倍の高速化 が必須だった。 コンテスト中に考えたこと 幅優先探索（BFS）または深さ優先探索（DFS）で解けそう。 しかし、前回動いた方向に依存するマス（ o や x ）がある。 そのため、単純に「一度通ったマスを候補から消…

## What’s new and why it matters
まずは結論から。 この問題は単純なBFSではなく、 「直前の移動方向」も状態に含めて管理する 必要があった。 また、Pythonで実装する場合、訪問管理に set() を使うとTLEになるため、 3次元配列による定数倍の高速化 が必須だった。 コンテスト中に考えたこと 幅優先探索（BFS）または深さ優先探索（DFS）で解けそう。 しかし、前回動いた方向に依存するマス（ o や x ）がある。 そのため、単純に「一度通ったマスを候補から消す」というやり方はできなさそう。 どうやってそれを解決するか分からず、時間切れ……。 経路復元のやり方についても分からなかった。 解説をみて：状態の持ち方と経路復元 解説を確認して、以下の2点に気づいた。 状態の再定義 位置 (y, x) に加えて、 「前回進んだ方向」 を保持することで、マスの進入制限をクリアしつつ同じ状態を回避できることが分かった。 経路復元のアプローチ 別で配列（ prevs ）を作成し、木構造のようにループ毎に「どこから来たか」と「その向き」が分かればできるはず。 実装としては、queueの探索ごとに配列に現在のノード（親のインデックスと移動方向を含む）を追加してインデックスを増やしていく。そして、キューに追加するタイミングで現在のインデックスも一緒に保持しておくと、ゴールから逆走して「どこから来たか」が辿れるようになる。 失…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/iwamutsu256/abc453-d-go-straight-fu-xi-memobfsnozhuang-tai-guan-li-totledui-ce-1eb2

## Related notes
- [[2026-03-25-stanford-is-teaching-the-world-to-code-for-free]]
- [[2026-03-01-stop-writing-python-without-type-hints-heres-how-to-start]]
- [[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-22-day-1-of-my-90-days-ai-journey-setting-up-the-perfect-environment]]
- [[2026-02-24-beginner-friendly-guide-sum-of-root-to-leaf-binary-numbers---problem-1022-c-python-javascript]]
