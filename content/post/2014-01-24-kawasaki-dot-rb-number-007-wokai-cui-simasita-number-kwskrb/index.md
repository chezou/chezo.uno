---
authors:
- aki
categories:
- ruby
date: '2014-01-24 14:05:53-08:00'
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
keywords:
- category
- create
- text
- train
- line
- tagger
- self
- segment
- file
- def
lastmod: '2014-01-24 14:05:53-08:00'
projects: []
recommendations:
- /post/2022-06-18-kawasaki rb 9 years reflection/
- /post/2016-08-23-chuan-qi-rubyhui-yi-01wokai-cui-simasita-number-kwsk01/
- /post/2015-01-25-shen-nai-chuan-rubyhui-yi-wokai-cui-simasita-number-kana01/
subtitle: ''
summary: ''
tags: []
title: 'kawasaki.rb #007 を開催しました #kwskrb'
---

2013/12/18にkawasaki.rbの第7回を開催しました。  
この会から、(同じミューザ川崎内ですが)NTT-ATさんに会場をお借りするようになりました。

第6回で、居酒屋LTをやることを挫折したので、毎月会議室でミートアップを行うようになりました。

togetterのまとめはこちら  
[http://togetter.com/li/606572](http://togetter.com/li/606572)

パーフェクトRubyは、2.6のモジュールまでやりました。

## chezou "Active ModelとNaive Bayesを仲良くする baby\_faceを使ってみた"

[http://www.slideshare.net/chezou/merone-upload-29446373](http://www.slideshare.net/chezou/merone-upload-29446373)

[yoshiori さんが作ったBabyFace](http://yoshiori.github.io/blog/2013/12/09/babyface-gem/)というGemを使ったサンプルアプリとして[Merone](https://github.com/chezou/merone)を作りました。  
BabyFaceはActiveModelなどとナイーブベイズ分類器とをつなぎ合わせることができる便利なGemです。  
なんてことはない、投稿したテキストが、DQかモンハンかSkyrimかを判定するだけの簡単なアプリです。  
最初はHerokuに上げておこうと思ったのですが、無料で使うにはDBのレコード数の制限が厳しいとかあったので、localで動かしたものでデモをしました。

ポイントとしては、学習が

    def self.create\_with\_train(text, category) e = Entry.create(comment: text) method = "train\_#{category}".intern e.baby\_face.send(method) enddef self.open\_and\_create(file, category) line = 0 open(file) do |f| while l = f.gets next if l.nil? || l.chomp!.empty? break if line == 10000 line += 1 create\_with\_train(l, category) endendend

これくらいで簡単にかけることと、日本語の分かち書きには[TinySegmenter](https://github.com/6/tiny_segmenter)を使いました。これならmecab&bindingのインストールとか要らない！便利！とか思っていたら、今どきはhomebrewでサクッとはいるんですね。。。

    def segment(text) @tagger ||= TinySegmenter.new @tagger.segment(text, ignore\_punctuation: true)end

## [@suginoy](https://twitter.com/suginoy)さんの"自分のほしいものをどんどんつくろうよ"という話

いつもblogにはお世話になっている、suginoyさんの、Railsだと簡単にWebアプリケーション書けるんだから、自分のほしいものを皆どんどんつくろうよ、というお話。

- Rubyのカンファレンスサイトをscrapingしてきて、podcastにしちゃえ
- [reijiro](http://knsmr.github.io/reijiro/)をゴニョゴニョしている
- suicaの使用履歴とかをRailsで管理できるようにしてます

などなど、いい話でした。

懇親会では、Kanagawa Ruby会議やりたいですなー、とか盛り上がりました。