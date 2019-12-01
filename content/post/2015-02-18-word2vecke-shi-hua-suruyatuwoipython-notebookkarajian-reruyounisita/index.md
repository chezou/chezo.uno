---
title: "word2vec可視化するやつをipython notebookから見れるようにした"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-02-18T18:45:17+00:00
lastmod: 2015-02-18T18:45:17+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
オライリーから出てる、[word2vec本](http://www.oreilly.co.jp/books/9784873116839/)の付録についてくる [id:nishiohirokazu](http://blog.hatena.ne.jp/nishiohirokazu/) さんが書いた可視化のコードがあります。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fd.hatena.ne.jp%2Fnishiohirokazu%2F20140109%2F1389251331&quot; title=&quot;word2vecのword-analogyを可視化した - 西尾泰和のはてなダイアリー&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;a href=&quot;http://d.hatena.ne.jp/nishiohirokazu/20140109/1389251331&quot;&gt;word2vecのword-analogyを可視化した - 西尾泰和のはてなダイアリー&lt;/a&gt;&lt;/iframe&gt;

[word2vecのword-analogyを可視化した - 西尾泰和のはてなダイアリー](http://d.hatena.ne.jp/nishiohirokazu/20140109/1389251331)

これを、ipython notebookから扱えるようにしました。

[Visualizer word2vec data for ipython notebook](https://gist.github.com/chezou/3899461aa550f73854a1)

今回ipython notebookから使えるようにしたのは、厳密には上記のコードではなくて、[こちら](https://github.com/nishio/mycorpus/blob/master/vis.py)のコードなのですが、ある単語の周辺にある単語をPCAで2次元に縮退させて可視化してくれます。

&lt;iframe src=&quot;http://nbviewer.ipython.org/gist/chezou/3899461aa550f73854a1/word2vec.ipynb&quot; width=&quot;640&quot; height=&quot;800&quot;&gt;&lt;/iframe&gt;

[大きくする](http://nbviewer.ipython.org/gist/chezou/3899461aa550f73854a1/word2vec.ipynb)

ipython notebookに関しての説明は、過去の記事を参照してください。

&lt;iframe src=&quot;http://chezou.hatenablog.com/embed/2015/01/11/031931&quot; title=&quot;Docker上にnbviewerを立ててiruby+Nyaplotで描いたグラフを共有できるようにしてみた - once upon a time,&quot; class=&quot;embed-card embed-blogcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;a href=&quot;http://chezou.hatenablog.com/entry/2015/01/11/031931&quot;&gt;Docker上にnbviewerを立ててiruby+Nyaplotで描いたグラフを共有できるようにしてみた - once upon a time,&lt;/a&gt;&lt;/iframe&gt;

[Docker上にnbviewerを立ててiruby+Nyaplotで描いたグラフを共有できるようにしてみた - once upon a time,](http://chezou.hatenablog.com/entry/2015/01/11/031931)

同じ要領で、ベクトルの引き算をした空間の可視化の奴もできると思います。

注意点としては、MacだとBoost.Pythonがsystem Pythonに対して入れなければならず(anacondaだと死にました)、ドはまりしたことでしょうか。 やはり、こうしたグラフをインタラクティブに生成するのはipython notebookの得意領域ですね


