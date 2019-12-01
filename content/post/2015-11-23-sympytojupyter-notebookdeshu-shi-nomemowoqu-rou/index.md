---
title: "SympyとJupyter notebookで数式のメモを取ろう"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-11-23T21:02:07+00:00
lastmod: 2015-11-23T21:02:07+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
[id:meison\_amsl](http://blog.hatena.ne.jp/meison_amsl/) さんによるSympyの紹介がとてもよい感じだったのですが、Sympy Liveわざわざ使わなくてもJupyter notebook使えるのでは！？と思ったので試してみました。\*1わざわざ、というと語弊があると思いますが、手元でメモ＋αとして管理するのにはJupyter notebookの方がいいかなと思っています。

&lt;iframe src=&quot;http://myenigma.hatenablog.com/embed/2015/11/21/222755&quot; title=&quot;Pythonの数式処理ライブラリSymPyをWolfram Alpha(Mathematica, Maxima)の代わりに使う方法 - MyEnigma&quot; class=&quot;embed-card embed-blogcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://myenigma.hatenablog.com/entry/2015/11/21/222755&quot;&gt;myenigma.hatenablog.com&lt;/a&gt;&lt;/cite&gt;

Sympyは [2015年センター試験数学IAを全てプログラム(Python)で解く - Qiita](http://qiita.com/Akai_Banana/items/b328fe0116d248127a36) でも見ていて、ふーん、凄いなと思っていた程度なのですが、 単純に数式を記述するだけではなく、それを方程式として展開したり微分、積分したりできるのが良いですね。 単に数式をメモするだけならJupyter notebookでLaTex記法で数式を書くことができます。

meison\_amslさんのものを Jupyter notebook で実行しただけのお手軽版はこちらです。

&lt;script src=&quot;https://gist.github.com/chezou/af6756cf50bb08a1d6ad.js&quot;&gt; &lt;/script&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://gist.github.com/chezou/af6756cf50bb08a1d6ad&quot;&gt;gist.github.com&lt;/a&gt;&lt;/cite&gt;

グラフもさくさくっとかけるので、極限求めるついでにグラフ書くとかするととても便利ですね。 （これがあれば、PRMLもらくらく戦えるのかな...）

kindleでも売っているInstant Sympy Starterですが、ちょうどPacktのアンケートに答えたらなんでも$5で買えるキャンペーンがやっていたので、そちらで買いました。 Packtは一度買うとガンガンクーポン来るし、月額定額で読み放題とかもできるみたいなので、Kindleで買うくらいならPacktで買うのも良いかもしれません。

[![Instant SymPy Starter](http://ecx.images-amazon.com/images/I/51OUVFQhi9L._SL160_.jpg &quot;Instant SymPy Starter&quot;)](http://www.amazon.co.jp/exec/obidos/ASIN/B00CYHB3CG/chezou-22/)

[Instant SymPy Starter](http://www.amazon.co.jp/exec/obidos/ASIN/B00CYHB3CG/chezou-22/)

- 作者: Ronan Lamy
- 出版社/メーカー: Packt Publishing
- 発売日: 2013/05/23
- メディア: Kindle版
- [この商品を含むブログ (1件) を見る](http://d.hatena.ne.jp/asin/B00CYHB3CG/chezou-22)

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fwww.packtpub.com%2Fbig-data-and-business-intelligence%2Finstant-sympy-starter-instant&quot; title=&quot;Instant SymPy Starter | PACKT Books&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://www.packtpub.com/big-data-and-business-intelligence/instant-sympy-starter-instant&quot;&gt;www.packtpub.com&lt;/a&gt;&lt;/cite&gt;

\*1:完全に人の褌で相撲を取るやつですね...


