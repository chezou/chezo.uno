---
title: 'Kawasaki.rb #005を開催しました #kwskrb'
date: 2014-01-24T22:05:31.000Z
subtitle: ''
summary: ''
draft: false
featured: false
authors:
  - aki
lastmod: 2014-01-24T22:05:31.000Z
tags: []
projects: []
image:
  caption: ''
  focal_point: ''
  preview_only: false
categories:
  - ruby
---
大分たってしまいましたが、2013/10/23にKawasaki.rb #005を行いました。

[@mametter](https://twitter.com/mametter) さんによる[quine-relay](https://github.com/mame/quine-relay)の話をしていただきました。  
quine-relayとは50言語&lt;sup id=&quot;fnref-1648-lang&quot;&gt;&lt;a href=&quot;#fn-1648-lang&quot; rel=&quot;footnote&quot;&gt;1&lt;/a&gt;&lt;/sup&gt;が次々に次の言語を生成し、一周してRubyに戻ってくるというコードであります。

togetterによるまとめはこちらになります。  
[http://togetter.com/li/581020](http://togetter.com/li/581020)

肝心のスライドは、諸般の事情[^problem]により公開できなさそう、ということですが、  
Quineの解説は以下の資料が詳しいです。

[http://www.slideshare.net/mametter/ruby-2012](http://www.slideshare.net/mametter/ruby-2012)

ポイントとしては、&quot;いかに次の言語の文字列をprintするか&quot;というところが大きいようです。  
特に、エスケープが増えてしまうと、様々な言語の制限(主に文字数制限)に引っかかってしまい実行できなくなるという問題があるようで、takesakoさんの[ppencode](http://www.namazu.org/~takesako/diary/?date=20050831)やら文字列圧縮などを使い工夫することで、それらをうまく回避しているとのことです。

また、内部では[code-gen.rb](https://github.com/mame/quine-relay/blob/master/src/code-gen.rb)で次の言語でのprint文を書けば、順番に生成するようになっているので、言語を増やしたいとかいう人はpull-requestを送るといいと思います。(D言語とかJSXとか、TypeScriptとか...)  
なお、言語の選定基準はDebianのapt-getで導入できる言語、というのを想定していたとのことです。(が、MacではhomebrewがClojureのサポートを打ち切った等の問題が有り、VMでやるのが良さそうです。)

なお、quine-relayは経済効果をも生み出していたようで（！）、Quoraだかredditだかで「quine-relayの解説したらお礼にお金を払うよ！」と言っていた人に解説をした人がいくばくかのお金をもらっていたそうです。  
(もちろん、mameさんにはなんのお金も渡っていないですよ)

  

* * *
  

1.   
有名なBrainfuckやWhitespaceに始まり、果てはVerilogとかINTERCALとか！  
[^problem] : &amp;nbsp;様々な[争いの種](http://twitter.com/mrkn/status/392974009199259648)が含まれるため&amp;nbsp;↩  


