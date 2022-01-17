---
title: 'kawasaki.rb #009を開催しました #kwskrb'
date: 2014-03-01 12:03:51+00:00
subtitle: ''
summary: ''
draft: false
featured: false
authors: [aki]
lastmod: 2014-03-01 12:03:51+00:00
tags: []
projects: []
image: {caption: '', focal_point: '', preview_only: false}
categories: [ruby]
keywords: [pandas, hash, foo, ランキング, org, range, obj, aflc, rb, クラス]
recommendations: [/post/2013-06-29-kawasaki-dot-rb-number-001-di-1hui-mitoatupuwokai-cui-simasita-number-kwskrb/,
  /post/2015-10-12-pyconjp-2015nican-jia-sita-number-pyconjp/, /post/2013-08-03-kawasaki-dot-rb-number-002-kai-cui-simasita-number-kwskrb/]
---
去る2/26(水)に[kawasaki.rb #009](http://kawasakirb.doorkeeper.jp/events/8859)を開催しました。

togetterのまとめはこちらです。  
[kawasaki.rb #009 まとめ #kwskrb - Togetterまとめ](http://togetter.com/li/635478)

## パーフェクトRuby読書会

2-7-4 配列, 2-7-5 ハッシュ, 2-7-6 範囲(Range)をやりました。

Hashでは、自分で作ったクラスをHashのkeyに用いる場合はどうすればいいのか、という話がでました。  
自作クラスに`hash`メソッドと`eql?(other)`メソッドを定義すれば、  
自作クラスでも同値性判定が行われるという確認をしました。  
(やっててよかった、レシピブック&yokohama.rb...)

コードで書くと、こういう感じですね。

    class Fooattr\_reader :a, :bdef initialize(a, b) @a, @b = a, b enddef hash@a%10 + @b%7enddef eql?(obj) @a == obj.a && @b == obj.b endendf1 = Foo.new(1, 2) f2 = Foo.new(1, 2) f1.eql?(f2) # =\> trueh = {} h[f1] = "foo"h[f2] # =\> "foo"

Rangeでは、`(1..-1)`のような負の数までのRangeってなんであるんだろう？という話をしました。  
使用するケースとしては、Arrayにアクセスするとき`ary[1..-1]`というのを渡すよねー、という話になりました。

## LT

### BestGems.org (ぺけみさおさん)

LTは[ぺけみさお](https://twitter.com/xmisao)さんによる [ランキングから見るRubyGems -BestGems.orgのご紹介-](http://www.xmisao.com/presentation/kawasaki_rb_9/index.html#/) と、[@aflc\_jp](https://twitter.com/aflc_jp) さんによるpandasの紹介(資料公開されたら追記します)が発表されました。

ぺけみさおさんの、BestGems.orgはRubyGems.orgを毎日クローリングして、  
DL数の変化を見ているというシンプルながら価値のありそうなアプローチでランキングを作られていました。  
実際にランキング作って分析するのって、楽しいですよね。

ランキングを分析していると[naught](https://github.com/avdi/naught)というgemの人気が上がっているとのことでした。

### pandas紹介するよ(aflc\_jpさん)

aflc\_jpさんのpandasの紹介は、Pythonのデータ分析によく使われるライブラリである  
[pandas](http://pandas.pydata.org/)の基本と使い方のexampleを紹介してもらいました。

[資料](http://aflc.github.io/kawasaki.rb/2-pandas/introduce_pandas.slides.html#/)  
[デモ](http://aflc.github.io/kawasaki.rb/2-pandas/medalists.html)

説明を聞くと、pandasはRでよく使われているDataFrameを扱えるようにしているところが特徴のようで、  
SQL likeにgroupbyして集計をしやすくなっているという話でした。  
例としてはオリンピックのメダルのデータを使って、日本が歴代メダル数を稼いだ種目などを表にしていました。  
Excelに出力することもできるので、分析はpandasでreportingはexcelで、という使い分けができるようです。

改めて実感したのは、IPython notebookは便利だなーということ。  
IJuliaで便利さは実感していたのですが、Rubyの実行もブラウザベースでやれるようになるそうなので、  
kawasaki.rbのパーフェクトRuby読み会でもIPythonベースにしようかなー。

次回は、3/26(水)に開催予定です


