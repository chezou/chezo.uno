---
title: "Docker上にnbviewerを立ててiruby+Nyaplotで描いたグラフを共有できるようにしてみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-01-11T03:19:31+00:00
lastmod: 2015-01-11T03:19:31+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
昨年末に[@domitryさんが書かれた記事](http://domitry.hatenablog.jp/entry/science_with_ruby)でも話題になった、RubyのライブラリMikonとNyaplotで生成したグラフをipython notebookとして社内のGHEでも共有することを目標に、[nbviewer](http://nbviewer.ipython.org/)をlocalのdocker上で立ててみました。

ちなみに、1/10のyokohama.rbでモクモクした成果です。

(今回は手元で検証したため、Macでdocker環境を構築しています。GHEでの検証までは行っていません)

# nbviewerとは

皆さん、[ipython notebook](http://ipython.org/notebook.html)はご存知でしょうか？

ipython notebookは以下の特徴を持ちます。

- 対話的に書いたコードと実行結果が描画されて、それを保存できる
- markdownも書ける
- nbviewerを使えば、notebookが共有できる！
- Python,Ruby,Juliaが対応している

Rubyの例ですがTokyu Ruby会議で発表したスライドを貼っておきます。 kawasaki.rbではipython notebookで[パーフェクトRuby読書会の様子を貼っています](http://kawasakirb.github.io/kawasakirb/2014/12/23/kawasakirb-019-kwskrb/)。

&lt;iframe src=&quot;//www.slideshare.net/slideshow/embed_code/42147157&quot; width=&quot;425&quot; height=&quot;355&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[Recommendation for iruby #tqrk08](//www.slideshare.net/chezou/recommendation-for-iruby &quot;Recommendation for iruby #tqrk08&quot;)** from **[Michiaki Ariga](//www.slideshare.net/chezou)** 

これだけだと魅力がわかりにくいと思うので、実行結果を貼ります。 描画したグラフも共有できるのが大きな魅力だと思います。

&lt;iframe src=&quot;http://nbviewer.ipython.org/github/chezou/iruby-example/blob/master/graph-example.ipynb&quot; width=&quot;640&quot; height=&quot;455&quot;&gt; &lt;/iframe&gt;

もしかすると、Gunosyの粟飯原さんが[以前作られたnotebook](http://nbviewer.ipython.org/gist/shunsukeaihara/dc2552453e1272866e2a)をご覧になった方もいるかもしれません。

また、Mining the Social Web 2nd Editionが[ipynb](http://nbviewer.ipython.org/github/ptwobrussell/Mining-the-Social-Web-2nd-Edition/blob/master/ipynb/_Appendix%20A%20-%20Virtual%20Machine%20Experience.ipynb)を用意していたりします。(コードの教育にも向いていると思います)

この、ブラウザで手軽にipython notebookの結果を見れるようにしているのがnbviewerです。githubで公開されているレポジトリやgistなら特に問題なく静的に再現してくれるのが特徴です。 nbviewerのいいところは、Python, Ruby, Juliaの実行環境がなくてもjsonをレンダーしているだけなのでブラウザで表示できることです。

便利なnbviewer+ipython notebookですが、社内のGHEに使いたい場合は自分でnbviewerを立てなければなりません。 そこで、今回はnbviewerを手元のMacとboot2dockerで動かしてみます。

# Macでdocker

Macでは[boot2docker](http://boot2docker.io/)を使ってVirtualBox上にdockerの環境を立てます。

    brew install boot2docker boot2docker init boot2docker up

## もしboot2docker initに失敗したら

自分の環境のVirtualBoxは古かったので、途中でこんなエラーがでました。

    error in run: Failed to initialize machine &quot;boot2docker-vm&quot;: exit status 1

[こちら](https://github.com/boot2docker/boot2docker/issues/525)を見ると、VirtualBoxのバージョンが古いとダメなようなので、VirtualBoxをアップデート後に

    boot2docker delete boot2docker init

で無事起動しました。

# Jupyter Notebook Viewer

Dokcer上でnbviewerを動かすには、用意されているdocker imageを使えばよいです。

基本的には公式に従えば大丈夫です。[https://github.com/jupyter/nbviewer](https://github.com/jupyter/nbviewer)

基本的にgistやgithubのレポジトリに置いたipynbを表示するのに使うので、予めgithubでapi tokenを取得しておきましょう。

    docker pull jupyter/nbviewer docker run -p 8080:8080 jupyter/nbviewer -e &#39;GITHUB\_API\_TOKEN=YOUR\_API\_TOKEN&#39;

# nbviewerを起動する

    open http://$(boot2docker ip 2\&gt;/dev/null):8080/

これで、あなたのブラウザにdocker上のnbviewerが見れるはずです！

![f:id:chezou:20150111031411p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150111/20150111031411.png &quot;f:id:chezou:20150111031411p:plain&quot;)

以下のURLを入れて試してみました。

[https://github.com/chezou/iruby-example/blob/master/nyaplot-example.ipynb](https://github.com/chezou/iruby-example/blob/master/nyaplot-example.ipynb)

![f:id:chezou:20150111031415p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150111/20150111031415.png &quot;f:id:chezou:20150111031415p:plain&quot;)

Nyaplot 3Dのグラフはマウスでグリグリ動かせるので楽しいですね。

# RubyのMikon+Nyaplotで可視化

さて、Mikonとd3.jsを使ったiruby上の可視化ライブラリNyaplotを使って可視化してみます。

MikonはRubyにおけるpandasのような位置づけで、表形式のデータ操作が得意なライブラリです。いわゆる、Rで有名な[DataFrame](http://cse.naro.affrc.go.jp/takezawa/r-tips/r/39.html)がRubyで扱えるようになります。 NyaplotはJuliaでいうところのGadfly的な位置づけで、グラフの描画ができるライブラリです。面白い事例では地図の可視化とかも出来たりします。

MikonはNMatrixに依存しており、こいつがCBLASなど依存が激しくMacでビルドをするのが大変だったので、こちらも[dockerで環境を作りました](https://registry.hub.docker.com/u/domitry/sciruby-docker/)。

    docker pull domitry/sciruby-docker docker run -i -p 9999:9999 domitry/sciruby-docker:latest open http://$(boot2docker ip 2\&gt;/dev/null):9999/

今回は次のgistを可視化してみました。[https://gist.github.com/chezou/38ddcc79babe34b73f10](https://gist.github.com/chezou/38ddcc79babe34b73f10)

nbviewerで見る場合は[こちら](http://nbviewer.ipython.org/gist/chezou/38ddcc79babe34b73f10)

こんな感じでipython notebookが無事見れるようになりました。

![f:id:chezou:20150111031419p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150111/20150111031419.png &quot;f:id:chezou:20150111031419p:plain&quot;)

# 雑感

今回、GHEでの検証まではしていませんが、概ねGHE上のgistやレポジトリのipython notebookを描画することはできそうな目処が経ちました。

しかし、MikonとNyaplotを使ったグラフ描画は別途サーバサイドで用意する必要がありそうです。 Nyaplot自体は依存関係は薄いのですが、Mikonを使おうと思うとするとNMatrixのビルドが大変だったりするのでdocker上のiruby notebookを立ちあげなければなりません。 この状況だと、手元にあるcsvなどを食わせようとした時は、dockerで立ち上げたipythonサーバにデータを移して食わせる必要があるなど、社内で普及を促すのにハードルが高い印象を受けました。


