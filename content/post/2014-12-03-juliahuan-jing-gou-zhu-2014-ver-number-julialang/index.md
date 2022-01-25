---
title: 'Julia環境構築 2014 ver. #julialang'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-12-03 00:05:00+00:00
lastmod: 2014-12-03 00:05:00+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [julia, ijulia, anaconda, ipython, lighttable, repl, apt, '2014', install,
  chezou]
recommendations: [/post/2015-12-10-julianoqing-bao-woshou-ji-situdukeruniha/, /post/2015-09-23-mecab-dot-jlwojulia-v0-dot-4-0-rc2nidui-ying-sita/,
  /post/2014-07-05-number-juliatokyo-01de-julia100ben-notuku-wofa-biao-sitekimasita/]
---
[Julia Advent Calendar 2014](http://qiita.com/advent-calendar/2014/julialang) 3日目の記事です。

1日目、2日目の記事を読んで、とりあえず試してみよう！と思った人のためのお話です。

Macに移って久しいのでWindows, Linuxの事情は薄くなりますがご勘弁を。

# 事前知識

Juliaはまだまだ鋭意開発中の言語なので、変化が激しいです。 割とStableを使ってる人が少ないかもしれません。なので、Stableの導入の仕方とNightly buildsの入れ方を書いておきます。

自分はv0.4(Nightly builds)を使ってます。 少なくとも、2014年には0.2系以前を試す必要は無いと思います。

# 入れるもの

- Julia
- anaconda
- IJulia
- LightTable(IDEが欲しければ)

# Julia

## Windows

[バイナリをダウンロード](http://julialang.org/downloads/)するのが一番手軽です。

StableもNightlyもこれでいいでしょう。

## Mac

### お手軽に試すには

[バイナリをダウンロード](http://julialang.org/downloads/)するのが一番手軽です。

`/Applications/Julia-0.X.X*.app/Contents/Resources/julia/bin/julia` に`~/bin/`以下にシンボリックリンクを貼るなどして、PATHを通しておくとよいでしょう。

### Homebrew

[github](https://github.com/JuliaLang/julia)からcloneしてビルドするのも良いですが、[homebrew](https://github.com/staticfloat/homebrew-julia/)から入れるのが楽です。

    $ brew update $ brew tap staticfloat/julia $ brew install julia

Nightlyを入れるには

    $ brew install julia --HEAD

でOKです。

gccとかを更新した時は、[arpack-juliaとopenblas-juliaを削除する](http://qiita.com/chezou/items/136959635463a918b8be)と良いでしょう。

## Ubuntu

### Stable

PPAを使ってaptで取得できるようにするのが楽です。

    $ sudo add-apt-repository ppa:staticfloat/juliareleases $ sudo add-apt-repository ppa:staticfloat/julia-deps $ sudo apt-get update $ sudo apt-get install julia

14.10からは普通に`apt-get install julia`で入るようです

> [@chezou](https://twitter.com/chezou) Julia は Ubuntu 14.10 で普通に apt-get できるし、いずれ追加するつもりですよ
> 
> — Yusuke Endoh (@mametter) [2014, 11月 11](https://twitter.com/mametter/status/532174800970461186)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
### Nightly

    $ sudo apt-add-repository ppa:staticfloat/julianightlies $ sudo apt-add-repository ppa:staticfloat/julia-deps $ sudo apt-get update $ sudo apt-get install julia

## RHEL/CentOS系

RHEL系はEPEL使えば行けるそうです

# IJulia/anaconda

IJuliaはIPythonをベースにしたブラウザ上で動くJuliaの対話環境です。ガッツリパフォーマンスチューニングしたい人には向かないですが、グラフ書いたり分析したい人には適しています。 また、LightTableなどのエディターで実行結果を表示する時にも必要になるので入れておくのが良いでしょう。

IPythonの環境を入れるのがだるいので、Pythonの環境がまだないよ/こだわりないよって人は、anacondaを使うと良いでしょう。 MacでもシステムPythonだとIPythonのバージョンが古いとかなんとか色々はまるので、anacondaにしておくのが良いでしょう。

少し前のですが下記のサイトやIJulia本家の記述が参考になりますが、こちらにも簡単にまとめておきます。

<iframe src="https://hatenablog.com/embed?url=http%3A%2F%2Fd.hatena.ne.jp%2Fisobe1978%2F20131128%2F1385646377" title="IPython(Anaconda)とIJuliaが凄すぎる件 - アドファイブ日記" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="http://d.hatena.ne.jp/isobe1978/20131128/1385646377">IPython(Anaconda)とIJuliaが凄すぎる件 - アドファイブ日記</a></iframe>

[IPython(Anaconda)とIJuliaが凄すぎる件 - アドファイブ日記](http://d.hatena.ne.jp/isobe1978/20131128/1385646377)

<iframe src="https://hatenablog.com/embed?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2FIJulia.jl" title="JuliaLang/IJulia.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="https://github.com/JuliaLang/IJulia.jl">JuliaLang/IJulia.jl</a></iframe>

[JuliaLang/IJulia.jl · GitHub](https://github.com/JuliaLang/IJulia.jl)

1. [anacondaをダウンロード](http://continuum.io/downloads)して入れる
2. IJuliaを入れる

    Pkg.add("IJulia")

anacondaが入っていればこれで大丈夫なはずです。後は下記でIJuliaを起動後、適当なノートブックを作って試しましょう。

    $ ipython notebook --profile julia

便利なショートカットはこちら

<iframe src="https://hatenablog.com/embed?url=http%3A%2F%2Fd.hatena.ne.jp%2Fakamegane%2F20120409%231333983569" title="ipython 0.12 の notebook" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="http://d.hatena.ne.jp/akamegane/20120409#1333983569">ipython 0.12 の notebook</a></iframe>

[ipython 0.12 の notebook - akameganeの日記](http://d.hatena.ne.jp/akamegane/20120409#1333983569)

# LightTable (optional)

emacsやvimでjuliaのプラグインを入れるのも良いと思いますし、IDE的なものが欲しいよという人はLightTableを使うといいです。 補完もできて、Cmd+Enterで実行結果も確認できます。

[Sublime-IJulia](https://github.com/quinnj/Sublime-IJulia)もあるようですが使ったことがありません。

<iframe src="https://hatenablog.com/embed?url=http%3A%2F%2Fqiita.com%2Fchezou%2Fitems%2F5070bde5dc6647e55af3" title="Lightable - LightTable + JewelでJuliaの環境を作る - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="http://qiita.com/chezou/items/5070bde5dc6647e55af3">Lightable - LightTable + JewelでJuliaの環境を作る - Qiita</a></iframe>

[Lightable - LightTable + JewelでJuliaの環境を作る - Qiita](http://qiita.com/chezou/items/5070bde5dc6647e55af3)

## ちなみに

JuliaのREPLは実はかなり強力で、対話的に開発したいだけならREPLだけで良いという人もいます。

> すごい大事な話を忘れていた。これがJuliaのREPLの補完力です [#JuliaTokyo](https://twitter.com/hashtag/JuliaTokyo?src=hash) [pic.twitter.com/Ns5FqG6j80](http://t.co/Ns5FqG6j80)
> 
> — chezou (@chezou) [2014, 7月 5](https://twitter.com/chezou/status/485465372695339009)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

> juliaのREPL凄い便利。タブを押すとこういう奴らがいることがわかるが、何が凄いかって `∛ 8`で2.0って返ってくる所 [pic.twitter.com/LQwOV6t2tQ](http://t.co/LQwOV6t2tQ)
> 
> — chezou (@chezou) [2014, 6月 23](https://twitter.com/chezou/status/480941416533610496)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

僕自身は、なんだかんだでREPL+SublimeTextで書くことが多いです。

明日は再びbicycle1885さんです。


