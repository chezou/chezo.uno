---
title: "Websocketを使ってリアルタイムに形態素解析をするmorph-websocketを作ってみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2012-11-10T04:11:51+00:00
lastmod: 2012-11-10T04:11:51+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
[![morph-websocket画面](morph-websocket.png)](morph-websocket.png) morph-websocket画面

WebSocketを使ってリアルタイムに形態素解析結果を出力する、morph-websocketを作りました。

テキストボックスに入力すると、リアルタイムで形態素解析結果が出力されます。

ソースコードは、いつものようにgithubに置きました。

[https://github.com/chezou/morph-websocket](https://github.com/chezou/morph-websocket)

思いついたので、勢いで作りました。今まで、バッチ的にまとめて処理をしていたものに対して、リアルタイムで解析結果が変われば、何か見える世界が変わるかなーと思ったのですが、そんなに変わりませんでした。変わったのは寝る時間だけか。

最初はMeCabを使おうと思ったのですが、0.994のrubyバインディングがCreateModelできない現象にぶち当たって諦めました。なので、[Mykytea-ruby](http://chezou.wordpress.com/2011/07/15/kytea%e3%82%92ruby-python%e3%81%8b%e3%82%89%e4%bd%bf%e3%81%88%e3%82%8bmykytea%e3%82%92%e4%bd%9c%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/ &quot;KyTea:京都テキスト解析ツールキット をRuby, Pythonから使えるMykyteaを作ってみた&quot;)とRuby使ってます。

あ、ついでにMykyteaがKyTea 0.4.2に対応しました。

参考URL:

- [Nihitok BLOG: rubyのgem「em-websocket」を使ったらいとも簡単にwebsocketを導入できた。](http://nihitok.blogspot.jp/2011/08/rubygemem-websocketwebsocket.html)
- [jQueryを使って テキストボックスに打ち込んだ文字を リアルタイムで取得する方法 | LogicA](http://nihitok.blogspot.jp/2011/08/rubygemem-websocketwebsocket.html)

