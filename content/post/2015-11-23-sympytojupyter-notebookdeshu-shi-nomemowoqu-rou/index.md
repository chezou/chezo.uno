---
authors: [aki]
categories: null
date: '2015-11-23 13:02:07-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2015-11-23 13:02:07-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: SympyとJupyter notebookで数式のメモを取ろう
keywords: [packt, 数式, starter, instant, kindle, グラフ, com, メモ, センター試験, アンケート]
recommendations: [/post/2016-12-25-jin-nian-du-ndemian-bai-katutaman-hua-2016nian-bian/,
  /post/2016-12-30-2016nian-mai-tuteyokatutamono-10xuan/, /post/2015-12-29-2015nian-nimai-tuteyokatutawu-matome/]
---

[id:meison\_amsl](http://blog.hatena.ne.jp/meison_amsl/) さんによるSympyの紹介がとてもよい感じだったのですが、Sympy Liveわざわざ使わなくてもJupyter notebook使えるのでは！？と思ったので試してみました。[^1] わざわざ、というと語弊があると思いますが、手元でメモ＋αとして管理するのにはJupyter notebookの方がいいかなと思っています。

<iframe src="https://myenigma.hatenablog.com/embed/2015/11/21/222755" title="Pythonの数式処理ライブラリSymPyをWolfram Alpha(Mathematica, Maxima)の代わりに使う方法 - MyEnigma" class="embed-card embed-blogcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://myenigma.hatenablog.com/entry/2015/11/21/222755">myenigma.hatenablog.com</a></cite>

Sympyは [2015年センター試験数学IAを全てプログラム(Python)で解く - Qiita](http://qiita.com/Akai_Banana/items/b328fe0116d248127a36) でも見ていて、ふーん、凄いなと思っていた程度なのですが、 単純に数式を記述するだけではなく、それを方程式として展開したり微分、積分したりできるのが良いですね。 単に数式をメモするだけならJupyter notebookでLaTex記法で数式を書くことができます。

meison\_amslさんのものを Jupyter notebook で実行しただけのお手軽版はこちらです。

<script src="https://gist.github.com/chezou/af6756cf50bb08a1d6ad.js"> </script><cite class="hatena-citation"><a href="https://gist.github.com/chezou/af6756cf50bb08a1d6ad">gist.github.com</a></cite>

グラフもさくさくっとかけるので、極限求めるついでにグラフ書くとかするととても便利ですね。 （これがあれば、PRMLもらくらく戦えるのかな...）

kindleでも売っているInstant Sympy Starterですが、ちょうどPacktのアンケートに答えたらなんでも$5で買えるキャンペーンがやっていたので、そちらで買いました。 Packtは一度買うとガンガンクーポン来るし、月額定額で読み放題とかもできるみたいなので、Kindleで買うくらいならPacktで買うのも良いかもしれません。

{{< amazon asin="B00CYHB3CG" title="Instant SymPy Starter" >}}

[Instant SymPy Starter](http://www.amazon.co.jp/exec/obidos/ASIN/B00CYHB3CG/chezou-22/)

- 作者: Ronan Lamy
- 出版社/メーカー: Packt Publishing
- 発売日: 2013/05/23
- メディア: Kindle版
- [この商品を含むブログ (1件) を見る](http://d.hatena.ne.jp/asin/B00CYHB3CG/chezou-22)

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fwww.packtpub.com%2Fbig-data-and-business-intelligence%2Finstant-sympy-starter-instant" title="Instant SymPy Starter | PACKT Books" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://www.packtpub.com/big-data-and-business-intelligence/instant-sympy-starter-instant">www.packtpub.com</a></cite>

[^1]: 完全に人の褌で相撲を取るやつですね...