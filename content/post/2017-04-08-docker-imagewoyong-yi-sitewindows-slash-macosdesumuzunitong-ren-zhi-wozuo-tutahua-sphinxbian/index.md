---
title: Docker imageを用意してWindows/macOSでスムーズに同人誌を作った話（Sphinx編）
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2017-04-08 16:47:29+00:00
lastmod: 2017-04-08 16:47:29+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [原稿, docker, sphinx, 執筆, image, 変換, view, tokoroten, macos, 環境]
recommendations: [/post/2017-01-23-gitlab-ciwoshi-tutesphinxnodokiyumentowozi-dong-depdfnibirudosuru/,
  /post/2015-01-11-dockershang-ninbviewerwoli-teteiruby-plus-nyaplotdemiao-itagurahuwogong-you-dekiruyounisitemita/,
  /post/2017-01-22-shu-shi-ru-rinomarkdownwosphinxwoshi-tutehtml-slash-pdfnisuru/]
---
こんにちは、ハイラルに移住したchezouです。最近は、Rから始まりRで終わる言語をよく書いています。

いよいよ明日に迫ってきた[技術書典2](https://techbookfest.org/event/tbf02)ですが、お-13で[技術書供養寺](https://kuyodera.github.io/)として頒布を行います。 内容は、僕の機械学習の実務におけるtipsとfastFMを使った推薦、@tokorotenさんのKickstarterの分析、@hagino3000さんのスプラトゥーンのデータマイニングということで盛り沢山です。初めての同人誌ですが、140ページを超えた薄くない薄い本になりました。

是非買いに来てください！

## tl;dr

- 技術書を書くときに、LaTeXを含んだDocker image使ってCIでビルド出来るようにすると共同執筆が捗るよ

## 前回までのあらすじ

今回は、メンバーがWindowsの人とmacOSの人の混成チームであったこと、全員がPythonに馴染み深い人だったので、reStructuredTextベースのSphinxで書きました。

なお、メンバーの中には一度Jupyter notebookで下書きを書いて、それをnbconvertを使ってrstとして変換する人もいました（賢い）。この辺、Jupyterは元々Pythonのエコシステムなので数式含んだJupyter notebookをrstまで変換できるなら、良い選択肢かもしれません。

SphinxのDocker imageの作り方等は過去に書いているのでそちらを参考にしてください。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2017-01-23-gitlab-ciwoshi-tutesphinxnodokiyumentowozi-dong-depdfnibirudosuru/" data-iframely-url="//iframely.net/zOVIEuy"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

## なぜDocker imageを用意したか？

- 原稿執筆は余計な障害（環境構築とか）が入ると、その対応で燃え尽きる
- 原稿執筆は往々にして〆切ギリギリから開始するので、最短距離を走れるようにしたほうが成功確率が上がる
- OSが異なる環境でのLaTeX周りのトラブルシュートをしたくなかった
- ビルドにコケる原稿のpushが防げた

この目論見はすべて当たりました。実際に、共著者の皆様からはすぐに執筆開始できたとの喜びの声をいただきました。

[追記]

じつはどちらもLinuxで書いていたともいえることがわかりました…

> [@chezou](https://twitter.com/chezou) windowsの中のvmwareの中のubuntuの中のdockerで執筆環境を動かしていたので、Windows環境かと言われると疑問符が……  
>   
> 執筆自体は、ubuntuのhomeをwin-sshfsでwin側にマウントしてterapadでやってましたが。
> 
> — ところてん (@tokoroten) [2017年4月8日](https://twitter.com/tokoroten/status/850621748533907456)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

> [@chezou](https://twitter.com/chezou) おもしろ執筆環境。 [pic.twitter.com/i87mYkGMlV](https://t.co/i87mYkGMlV)
> 
> — ところてん (@tokoroten) [2017年4月9日](https://twitter.com/tokoroten/status/851108783811997696)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

> [@chezou](https://twitter.com/chezou) お、自分は何も見ずにrstが書けるようになった時点でdocker runしてるAmazon Linux上のvimで執筆してました
> 
> — 超循環評価器@中欧放浪中 (@hagino3000) [2017年4月8日](https://twitter.com/hagino3000/status/850670097333186561)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[/追記]

## Sphinxのdocker imageでできたこと

- WindowsでもmacOSでもすぐに書き始められる状況を準備できた
- Gitlab CIを使って、マージされたものをCIでPDFを用意する
- 奥付を作る
- （docker image関係ないけど）re:viewで書きかけていた原稿をreSTに変換できた

奥付については、少しトリッキーなので後述します。

## Sphinxのdocker imageでできなかったこと

- 原稿のグレースケール化（Adobe Acrobatでやった）
- 納得の行くfontの埋め込み（ヒラギノを使うためにmacOSでフォントを埋め込んだ）

Previewのグレースケール化は信用ならないので、グレースケール化には少なくともmacOSだとAcrobatが必須かもしれません。

fontの埋め込みは、IPA系のフォントだとライセンス的に問題なくコンテナ内で埋め込めるのですが、日本語の太字が綺麗にでなかったので結局MacでSphinxをビルドしてヒラギノを埋め込みました。[^1] そのおかげで、tokorotenさんの原稿の画像サイズが少しずれて手直しが入りました。。。dockerベースでフォント埋め込みまでやっていればいけたのに…。無念。

## 奥付の作り方

以外とハマったんですが、以下のgistのように一度citationをflashすれば行けます。 デフォルトでは、citationが必ず最後に来るようになっていますが、それを回避できます

[Sphinxで奥付を足す方法 · GitHub](https://gist.github.com/chezou/acc2417de764c818b62a14ef3b710f07)

## Re:VIEWの書きかけの原稿をreSTに変換できた（相互変換出来る時代に）

実は書きはじめのときに、shirouさんがRe:VIEWの原稿をSphinxの原稿に変換していただきました。ありがとうございました。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fkmuto%2Freview%2Fpull%2F733" title="rstbuilderを追加 by shirou · Pull Request #733 · kmuto/review" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/kmuto/review/pull/733">github.com</a></cite>

何故か手元にあった結構ボリュームのあるRe:VIEWの原稿を変換できて、大体の問題は解決されているのではないかなと思います。

なお、逆向きのSphinxの原稿からRe:VIEWを出力するプラグインもあります。これで、気が変わって別のフォーマットにexport/importが容易になりましたね！

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fshirou%2Fsphinxcontrib-reviewbuilder" title="shirou/sphinxcontrib-reviewbuilder" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/shirou/sphinxcontrib-reviewbuilder">github.com</a></cite>

# おわりに

今回は、shirouさん、shibukawaさん、tk0miyaさんといった#sphinxjpの皆様にお世話になりました。困ったことがあったときに、日本語で聞ける環境があるというのは非常に助かりました。

それでは、明日は秋葉原UDX2階のアキバ・スクエアで僕と握手！

[^1]: ヒラギノは商用利用可能とのことです [http://www.macotakara.jp/blog/support/entry-665.html](http://www.macotakara.jp/blog/support/entry-665.html)


