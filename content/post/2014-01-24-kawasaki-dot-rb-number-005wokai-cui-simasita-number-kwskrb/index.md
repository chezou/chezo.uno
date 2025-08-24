---
authors: [aki]
categories: [ruby]
date: '2014-01-24 14:05:31-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2014-01-24 14:05:31-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: 'Kawasaki.rb #005を開催しました #kwskrb'
keywords: [quine, relay, 言語, 解説, problem, mametter, お金, プログラミング, 制限, rb]
recommendations: [/post/2022-06-18-kawasaki rb 9 years reflection/, /post/2016-08-23-chuan-qi-rubyhui-yi-01wokai-cui-simasita-number-kwsk01/,
  /post/2013-10-06-kawasaki-dot-rb-number-004wokai-cui-simasita-number-kwskrb/]
---

大分たってしまいましたが、2013/10/23にKawasaki.rb #005を行いました。

[@mametter](https://twitter.com/mametter) さんによる[quine-relay](https://github.com/mame/quine-relay)の話をしていただきました。  
quine-relayとは50言語<sup id="fnref-1648-lang"><a href="#fn-1648-lang" rel="footnote">1</a></sup>が次々に次の言語を生成し、一周してRubyに戻ってくるというコードであります。

togetterによるまとめはこちらになります。  
[http://togetter.com/li/581020](http://togetter.com/li/581020)

肝心のスライドは、諸般の事情[^problem]により公開できなさそう、ということですが、  
Quineの解説は以下の資料が詳しいです。

[http://www.slideshare.net/mametter/ruby-2012](http://www.slideshare.net/mametter/ruby-2012)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/HSa6r0tKylPW2z" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/mametter/ruby-2012" title="Ruby を用いた超絶技巧プログラミング（夏のプログラミングシンポジウム 2012）" target="_blank">Ruby を用いた超絶技巧プログラミング（夏のプログラミングシンポジウム 2012）</a> </strong> from <strong><a href="//www.slideshare.net/mametter" target="_blank">mametter</a></strong> </div>

ポイントとしては、"いかに次の言語の文字列をprintするか"というところが大きいようです。  
特に、エスケープが増えてしまうと、様々な言語の制限(主に文字数制限)に引っかかってしまい実行できなくなるという問題があるようで、takesakoさんの[ppencode](http://www.namazu.org/~takesako/diary/?date=20050831)やら文字列圧縮などを使い工夫することで、それらをうまく回避しているとのことです。

また、内部では[code-gen.rb](https://github.com/mame/quine-relay/blob/master/src/code-gen.rb)で次の言語でのprint文を書けば、順番に生成するようになっているので、言語を増やしたいとかいう人はpull-requestを送るといいと思います。(D言語とかJSXとか、TypeScriptとか...)  
なお、言語の選定基準はDebianのapt-getで導入できる言語、というのを想定していたとのことです。(が、MacではhomebrewがClojureのサポートを打ち切った等の問題が有り、VMでやるのが良さそうです。)

なお、quine-relayは経済効果をも生み出していたようで（！）、Quoraだかredditだかで「quine-relayの解説したらお礼にお金を払うよ！」と言っていた人に解説をした人がいくばくかのお金をもらっていたそうです。  
(もちろん、mameさんにはなんのお金も渡っていないですよ)

  

* * *
  

1.   
有名なBrainfuckやWhitespaceに始まり、果てはVerilogとかINTERCALとか！  
[^problem] :  様々な[争いの種](http://twitter.com/mrkn/status/392974009199259648)が含まれるため ↩