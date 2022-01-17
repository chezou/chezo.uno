---
title: wordpress.comからはてなブログにお引っ越ししました
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-12-01 00:28:46+00:00
lastmod: 2014-12-01 00:28:46+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [syntax, 置換, highlight, wordpress, はてなダイアリー, 移行, 記法, はてなブログ, julia, 引っ越し]
recommendations: [/post/2012-11-12-pawapointonise-dukesitasosukodowojian-dan-nitie-rufang-fa/,
  /post/2015-09-23-mecab-dot-jlwojulia-v0-dot-4-0-rc2nidui-ying-sita/, /post/2015-12-25-julia-tokyo-number-5wokai-cui-simasita-number-juliatokyo/]
---
Markdownで書くのが辛くてwordpress.comからお引っ越ししました。 期待していたJuliaのsyntax highlihgtが無くて切ないです。

Tokyuのあれとか書こうと思っていたのですが、irubyの良さについては真面目に書こうと思います。

基本的に参考にしたのはこのサイトです。

- [Wordpressからはてなブログへ移行 - Deutschina&#39;s Tech Diary](http://deutschina.hatenablog.com/entry/2013/07/06/180717)

まさか、syntax highlightを移行するためにはてなダイアリーを経由しないといけないとか、はてなダイアリーの作成場所が巧妙に小さく分かりにくくされていたりとか、はてダ作ると緑スターもらえたりとか辛かったです。

1. wordpress.comからエクスポート
2. MT形式に変換
3. syntax highlightをsuper pre記法に置換(エディタで色々なパターン見つけて置換)
4. はてダにimport
5. はてなブログに移行
6. slideshareとかツイートの独自記法を見つけて悲しくなる(←今ここ)

本当は6も一括置換すればよかったんですが、3からループするのはもういやだなぁと諦めました...。 Juliaのsyntax highlightが欲しければQiitaに書くか、Gist貼ればいいんですね！


