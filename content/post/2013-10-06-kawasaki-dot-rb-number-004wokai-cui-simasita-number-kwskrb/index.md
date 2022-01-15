---
title: 'Kawasaki.rb #004を開催しました #kwskrb'
date: 2013-10-06 12:10:10+00:00
subtitle: ''
summary: ''
draft: false
featured: false
authors: [aki]
lastmod: 2013-10-06 12:10:10+00:00
tags: []
projects: []
image: {caption: '', focal_point: '', preview_only: false}
categories: [ruby]
keywords: [sinatra, lt, ws, '39', 形態素解析, kytea, 通信, リアルタイム, バインディング, phpapp]
recommendations: [/post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/,
  /post/2011-09-23-kyteawota-yan-yu-deshi-uratupa-plus-amatome/, /post/2013-08-03-kawasaki-dot-rb-number-002-kai-cui-simasita-number-kwskrb/]
---
9/25(水)にKawsaki.rbの第4回ミートアップを行いました。  
今回は偶数回なので、居酒屋LTの回でした。

例によって、鍋をつつきながらパーフェクトRubyを読みました。  
パーフェクトRubyは「2-1-3 トップレベル」まで行きました。

## LT1: Sinatra Hijackerと （Rack Hijacking API）の紹介 (Minori Tokudaさん)
LT1本目は、Tokudaさん([@snowcrush](https://twitter.com/snowcrush))による[Sinatra Hijacker](https://github.com/minoritea/sinatra-hijacker)のご紹介。

[slideshare id=26556881&doc=sinatrahijacker-130925182715-phpapp01]

Rack Hijacking APIを使って、ソケットを横取りしてSinatraでWebsocketの通信をしよう！というライブラリです。

    require &#39;sinatra/hijacker&#39;class YourApp \< Sinatra::Base register Sinatra::Hijacker websocket &#39;/ws&#39; do ws.onopen{ws.send\_data "hello"} endend

こんなかんじで、シンプルにwebsocketの通信ができるようになります。お手軽ですね。

## LT2: リアルタイム形態素解析 morph-websocket (@chezou)
[slideshare id=26540388&doc=kawasaki04-mw-130925093600-phpapp01]

LT2本目は、自分の[morph-websocket](http://chezou.wordpress.com/2012/11/10/websocket%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%a6%e3%83%aa%e3%82%a2%e3%83%ab%e3%82%bf%e3%82%a4%e3%83%a0%e3%81%ab%e5%bd%a2%e6%85%8b%e7%b4%a0%e8%a7%a3%e6%9e%90%e3%82%92%e3%81%99%e3%82%8bmorph-websocket/ "Websocketを使ってリアルタイムに形態素解析をするmorph-websocketを作ってみた")のご紹介とデモでした。websocketつながりということで紹介させていただきました。

形態素解析器Kyteaをバインディングしてwebsocket使って叩けるようにしましたよ、というお話です。  
KyteaじゃなくてMeCabでもできるんですけど、作ったときはなぜかRubyバインディングがうまく呼べなかったのでKyteaだけにしたという感じでした。

## 次回は
ついに、mameさんによる[quine relay](https://github.com/mame/quine-relay)の解説をしていただけることになりました！  
募集は[Doorkeeper](http://kawasakirb.doorkeeper.jp/)で近日開始する予定です。  
10/23(水)はミューザ川崎 音楽工房に集合だ！
