# Thema 4 | 日本語・ドイツ語の研究・執筆管理システム v001

**目的**：論文の章構成、文献PDF、根拠原文、検討事項、変更履歴をチャットをまたいでも保持できるZIPとして管理する。

## 初めに必ず読む
1. `05_templates/TEMPLATE_REQUIREMENTS.md` — 章別ページ制限と**AIによる本文生成を提出原稿へ貼り付け禁止**。
2. `04_handover/HANDOFF_CURRENT.md` — 最新状態・次の議題。
3. `04_handover/DECISION_LOG.md`・`OPEN_ISSUES.md` — 決定・未決事項。
4. `01_paper/versions/v001_20261123/ja` と `de` — **全章の研究ノート構成（提出本文ではない）**。
5. `02_literature/catalog/LITERATURE_CATALOG.md` と `evidence/EVIDENCE_INDEX.md` — 16論文と本文根拠。

## 利用手順（毎回の改訂）
- **最新のZIPを次のチャットへ添付**し、`04_handover/RESUME_PROMPT.md`の依頼文と今回の議題を伝える。
- 変更する章の**日本語版・ドイツ語版を章全文で出力**（節だけの差分は納品しない）。双方の出典ID・主張・不確実性を揃える。
- 原著を読んで**本文内の必要な短い原文・PDFページ・印刷ページ・解釈**を根拠カード・台帳に追加。Abstractだけを根拠に引用しない。
- `tools/new_release.py --date YYYY-MM-DD --summary "議題"`で新版を作成し、**旧版は絶対に上書きしない**。新版の章全文を更新する。
- `04_handover/SESSION_LOG_*.md`、`DECISION_LOG.md`、`OPEN_ISSUES.md`、`FUTURE_CHAPTER_FLAGS.md`、`HANDOFF_CURRENT.md`、`CHANGELOG.md`を更新しZIPに同梱する。
- `python tools/validate_system.py`で参照・章・原著の欠落を確認する。

## 保存のルール
- 版は `v001_20261123`, `v002_YYYYMMDD`, ...。同日複数版も連番で区別。
- 最新版は`VERSION.json`で指示。コピーした旧版は変更禁止。
- 文献は固定ID（L01-L16、追加はL17以降）で管理。原著不在のL07/L10/L14を「検証済」と書かない。
- 正式な提出原稿は学生本人が作成し、署名・AI使用規則に整合させる。

## 現段階
現在の各章は**完全な章別アウトライン**であり、論文本文や研究結果を完成させたものではない。実験課題、尺度、サンプル、倫理は未確定。生成した文章を提出論文にそのまま組み込まない。
