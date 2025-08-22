---
authors: [aki]
categories: [ruby]
date: '2013-10-06 04:10:03-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2013-10-06 04:10:03-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: 'Kawasaki.rb #003を開催しました #kwskrb'
keywords: [mruby, ruby, kishima, 数値計算, numpy, デモ, fortran, メソッド, scipy, js]
recommendations: [/post/2014-09-21-rubykaigixing-tutekimasita-and-rubyhirobade-shen-nai-chuan-rubyhui-yi-01-gao-zhi-ltsitekimasita-number-rubykaigi-number-rubyhiroba-number-kana01/,
  /post/2022-06-18-kawasaki rb 9 years reflection/, /post/2014-01-24-kawasaki-dot-rb-number-006-wokai-cui-simasita-number-kwskrb/]
---

大分遅くなりましたが、去る8/28(水)にKawasaki.rbの第3回ミートアップを開催しました。

この回では、新しい試みとして[パーフェクトRuby](http://gihyo.jp/book/2013/978-4-7741-5879-2?ard=1381056613)の読書会を行いました。  
本が販売されてから間もなかったのですが、会場いらっしゃった方の15名くらいが本を持っているというすごい状況になりました。

また、2本のプレゼンも非常に盛り上がりました。

[@yumu19](https://twitter.com/yumu19)さんにまとめていただいたtogetterは[こちら](http://togetter.com/li/555597)。

## パーフェクトRuby読書会

## 
まずは1章から突っ込みながら読んでいくことに。  
途中でサンプルクラス中でputsメソッドをpustとtypoした時に、「pustメソッドを定義すれば行ける！」という展開があるなど非常にRubyらしさを満喫できました。  
やはり前々から聞いていましたが、Rubyの全くの初心者向けというよりも、多少触っているけど色々知りたい！という人が読者層なんだなーという事を再確認しました。
## 

## @gotokenさんによるNumRuのお話
LLで数値計算といえば、PythonのNumPyが有名ですが、それを参考に作られたNumRuというRubyのライブラリがあります。  
これは、FORTRANを裏で扱うことでRubyでも数値計算が高速に処理できるというもの(だと理解しています)。

NumRuが一番分かりやすく詳細に書かれているのは、[この回のるびま](http://magazine.rubyist.net/?0006-RLR)でしょう。  
Pythonのmatplotlibみたいに色々描画をすることもできるようです。

ただ、NumRuという名前があまり浸透していないのは、おそらく「[電脳クラブライブラリ](http://www.gfd-dennou.org/arch/dcl/)」の名前空間としてNumRuという名前を用いているだけというのが大きいのかなー、というのと、地球惑星シミュレーションの人たちがメインで使っているので汎用的に使えるのかがあまりわからないところと、FORTRAN系のインストールが結構骨だというところでしょうか。。。

特に、FORTRAN周りのインストールはNumPy,SciPyあたりでも結構ハマるのですが、NumRuのHomebrewのFormulaをごとけんさんが作ろうとされたようですが、当日には間に合わず...。期待しております。

GSLとかもあるんですけど、このへんはNumPy,SciPyなどとの比較を行ったり、エコシステムが回るようになっていくと、Rubyで数値計算をするという話が増えるんじゃないかなー、と思っています。

## @kishimaさんによるmrubyとwebrubyのお話
[@kishima](https://twitter.com/kishima)さんによる、mrubyとwebrubyのお話をしていただきました。  
お忙しい中発表していただき感謝です。

内容は、mrubyの紹介とwebrubyの説明、TokyuRuby会議で使った抽選アプリのデモを見せていただきました。

(2013/10/30 スライドを追加しました！)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/5tRaZhfuS37pio" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/kishima7/mruby-kishima" title="Introduction of mruby &amp; Webruby script example" target="_blank">Introduction of mruby &amp; Webruby script example</a> </strong> from <strong><a href="//www.slideshare.net/kishima7" target="_blank">kishima7</a></strong> </div>

[webruby](https://github.com/xxuejie/webruby)の説明は、[kishimaさんご自身による説明](http://d.hatena.ne.jp/machaut/20130624/1372089582)がわかりやすいですが、Emscriptenを使ってブラウザ上でmrubyを動かそうというものです。  
LLVM,clangを経由してではありますが、JSとmrubyがつながるなんて胸が熱くなりますね。

デモは、webrubyとenchant.jsを使ったものになります。Tokyuの時のデモが以下のツイートで紹介されていたのでお試しください:)

[https://twitter.com/kishima/status/350969504219660288](https://twitter.com/kishima/status/350969504219660288)