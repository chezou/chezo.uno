---
title: word2vec可視化するやつをipython notebookから見れるようにした
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2015-02-18 18:45:17+00:00
lastmod: 2015-02-18 18:45:17+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [word, ipython, notebook, 可視化, グラフ, はてなダイアリー, nyaplot, nbviewer, iruby,
  docker]
recommendations: [/post/2015-01-11-dockershang-ninbviewerwoli-teteiruby-plus-nyaplotdemiao-itagurahuwogong-you-dekiruyounisitemita/,
  /post/2014-12-24-juliadeword-countsiteqi-duitakoto-number-juliaac/, /post/2016-10-29_homebrew-----iRuby---------------6a02e5194ff2/]
---
オライリーから出てる、[word2vec本](http://www.oreilly.co.jp/books/9784873116839/)の付録についてくる [id:nishiohirokazu](http://blog.hatena.ne.jp/nishiohirokazu/) さんが書いた可視化のコードがあります。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fd.hatena.ne.jp%2Fnishiohirokazu%2F20140109%2F1389251331" title="word2vecのword-analogyを可視化した - 西尾泰和のはてなダイアリー" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="http://d.hatena.ne.jp/nishiohirokazu/20140109/1389251331">word2vecのword-analogyを可視化した - 西尾泰和のはてなダイアリー</a></iframe>

[word2vecのword-analogyを可視化した - 西尾泰和のはてなダイアリー](http://d.hatena.ne.jp/nishiohirokazu/20140109/1389251331)

これを、ipython notebookから扱えるようにしました。

[Visualizer word2vec data for ipython notebook](https://gist.github.com/chezou/3899461aa550f73854a1)

今回ipython notebookから使えるようにしたのは、厳密には上記のコードではなくて、[こちら](https://github.com/nishio/mycorpus/blob/master/vis.py)のコードなのですが、ある単語の周辺にある単語をPCAで2次元に縮退させて可視化してくれます。

<iframe src="https://nbviewer.ipython.org/gist/chezou/3899461aa550f73854a1/word2vec.ipynb" width="640" height="800"></iframe>

[大きくする](https://nbviewer.ipython.org/gist/chezou/3899461aa550f73854a1/word2vec.ipynb)

ipython notebookに関しての説明は、過去の記事を参照してください。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2015-01-11-dockershang-ninbviewerwoli-teteiruby-plus-nyaplotdemiao-itagurahuwogong-you-dekiruyounisitemita/" data-iframely-url="//iframely.net/9Xh22Us"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

[Docker上にnbviewerを立ててiruby+Nyaplotで描いたグラフを共有できるようにしてみた - once upon a time,](https://chezo.uno/post/2015-01-11-dockershang-ninbviewerwoli-teteiruby-plus-nyaplotdemiao-itagurahuwogong-you-dekiruyounisitemita)

同じ要領で、ベクトルの引き算をした空間の可視化の奴もできると思います。

注意点としては、MacだとBoost.Pythonがsystem Pythonに対して入れなければならず(anacondaだと死にました)、ドはまりしたことでしょうか。 やはり、こうしたグラフをインタラクティブに生成するのはipython notebookの得意領域ですね


