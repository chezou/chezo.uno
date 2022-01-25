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
keywords: [websocket, sinatra, lt, ws, kytea, morph, 通信, バインディング, phpapp, doc]
recommendations: [/post/2012-11-10-websocketwoshi-tuteriarutaimunixing-tai-su-jie-xi-wosurumorph-websocketwozuo-tutemita/,
  /post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/, /post/2011-09-23-kyteawota-yan-yu-deshi-uratupa-plus-amatome/]
---
9/25(水)にKawsaki.rbの第4回ミートアップを行いました。  
今回は偶数回なので、居酒屋LTの回でした。

例によって、鍋をつつきながらパーフェクトRubyを読みました。  
パーフェクトRubyは「2-1-3 トップレベル」まで行きました。

## LT1: Sinatra Hijackerと （Rack Hijacking API）の紹介 (Minori Tokudaさん)
LT1本目は、Tokudaさん([@snowcrush](https://twitter.com/snowcrush))による[Sinatra Hijacker](https://github.com/minoritea/sinatra-hijacker)のご紹介。

[slideshare id=26556881&doc=sinatrahijacker-130925182715-phpapp01]

Rack Hijacking APIを使って、ソケットを横取りしてSinatraでWebsocketの通信をしよう！というライブラリです。

    require 'sinatra/hijacker'class YourApp \< Sinatra::Base register Sinatra::Hijacker websocket '/ws' do ws.onopen{ws.send\_data "hello"} endend

こんなかんじで、シンプルにwebsocketの通信ができるようになります。お手軽ですね。

## LT2: リアルタイム形態素解析 morph-websocket (@chezou)
[slideshare id=26540388&doc=kawasaki04-mw-130925093600-phpapp01]

LT2本目は、自分の[morph-websocket](https://chezo.uno/post/2012-11-10-websocketwoshi-tuteriarutaimunixing-tai-su-jie-xi-wosurumorph-websocketwozuo-tutemita/)のご紹介とデモでした。websocketつながりということで紹介させていただきました。

形態素解析器Kyteaをバインディングしてwebsocket使って叩けるようにしましたよ、というお話です。  
KyteaじゃなくてMeCabでもできるんですけど、作ったときはなぜかRubyバインディングがうまく呼べなかったのでKyteaだけにしたという感じでした。

## 次回は
ついに、mameさんによる[quine relay](https://github.com/mame/quine-relay)の解説をしていただけることになりました！  
募集は[Doorkeeper](http://kawasakirb.doorkeeper.jp/)で近日開始する予定です。  
10/23(水)はミューザ川崎 音楽工房に集合だ！
