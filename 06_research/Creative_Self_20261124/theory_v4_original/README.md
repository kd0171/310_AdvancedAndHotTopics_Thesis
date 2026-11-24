# Creative Self 理論体系・文献資料 v4

2026-11-24。研究の理解と検討のための資料。提出原稿ではない。前回のJussupow資料を拡張し、これまでの九原著と追加六原著の該当箇所を照合した。

## 内容
- `Theory_Guide.md/.tex/.pdf`：体系的解説、比較、原著研究の測定、評価者比較への示唆。
- `Evidence_Ledger.md/.tex/.pdf`：63個の根拠ID（J, K, B, I, A, V, Z, L, R, G, M, S, H, P, E）、短い原文抜粋・訳・掲載ページ・PDFページ・用途、文献索引、未確認事項。
- `figures/`：Graphviz DOTによる概念関係図と概念パス図、PDFとSVG。分類・理論上の関係を描画したもの。推定されたSEMや媒介効果ではない。
- `sources/`：これまで提供された13原著、前に提供されたJussupow最終版、Karwowski第19章抜粋（ユーザー提供PDFからの抜粋）。原著PDFは内容を変更していない。ファイル名の先頭が根拠ID。KarwowskiのPDFページ番号だけ、台帳では提供書籍全体の番号を維持する。抜粋PDFのページ = 書籍全体PDFページ - 417 = 書籍上のページ - 395。例：p. 397は全体PDF419、抜粋PDF2。Baumeisterの該当箇所はスキャン画像を目視確認。
- `header.tex`：PandocからLaTeX生成用ヘッダー。本文.texは単独コンパイルできる形に生成済み（図ファイルは相対パス）。

## 再生成
Graphviz、Pandoc、XeLaTeX、Noto Serif CJK JP、Noto Sans CJK JP、Liberation Serifを使用。フォントファイルは収録しない。

```sh
for f in figures/*.dot; do dot -Tpdf "$f" -o "${f%.dot}.pdf"; dot -Tsvg "$f" -o "${f%.dot}.svg"; done
for f in Theory_Guide Evidence_Ledger; do
  pandoc "$f.md" -s --from=markdown+raw_tex --to=latex -V documentclass=article -V papersize=a4 -V geometry:margin=21mm -V fontsize=11pt -V mainfont='Liberation Serif' -V colorlinks=true -V linkcolor=blue -V urlcolor=blue -H header.tex -o "$f.tex"
  xelatex -interaction=nonstopmode -halt-on-error "$f.tex"
  xelatex -interaction=nonstopmode -halt-on-error "$f.tex"
done
```

## 未検証事項
Jussupowオンライン付録は出版社PDFにアクセスできなかった。本文のA1/E3等への参照と各尺度候補の原著の区別を維持した。v4では追加6原著の該当箇所を確認。Goffmanは提供版1956年（Jussupow引用は1959年）。その他未提供文献は引き続き二次的な引用用途のみ。前回の付録に由来するとされた質問文・点数・尺度出典は未確認のままなので確定扱いにしない。

## 改訂履歴
v3: 7原著の読解、Karwowskiとの比較の拡張、Baumeisterの三基盤、Leary & Kowalskiの二成分モデルと防衛的自己呈示、Valsesia・Zhang・Louieの測定の区別、Reif・Amabileの研究位置づけ、40根拠ID、文献取得リスト、原著PDFと再現可能な図を追加。

- v4: 追加6原著、23根拠ID、Manningの引用文脈の修正、Schultze & BrooksのAIへの適用限界、Harvey & Berryの三形態、Pierceの所有感形成経路、Inzlichtの努力理論、理論境界図を追加。
