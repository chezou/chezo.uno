---
title: "NAS Navigator2が悪さをする@Windows7 64bit"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2009-10-26T21:56:21+00:00
lastmod: 2009-10-26T21:56:21+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
091111追記：解決方法は[こちら](http://wp.me/pvR30-d2)。

一回だけなんですが、Nas Navigator2がRun time errorを出してくれました。

で、調べてみると[こんな記事が  
Note - imatakutin&#39;s Mind Map: NasNavi.exe で Runtime Error!](http://imatakutin.blogspot.com/2008/05/nasnaviexe-runtime-error.html)

どうも、管理者モードでインストールしないとダメみたいです。  
で、改めてアンインストールしようとしたら、それができない。コンパネからもスタートメニューからも、ダメ。BuffaloはWindows7（というか64bit？）対応があまり積極的でないとも聞きます。そろそろio-dataに切り替え時なのかなぁ。

追記：  
ネットワーク上のTera/LinkStationを検索中です　が出て止まりません！NASにも三角アイコンがついてるし……。だめだぁ、こりゃ

さらに追記：  
なぜか、スタート→すべてのプログラム経由でアンインストールできた。下手に互換モードとかにしてもいけないみたい。よくわからん。ダメルコの時代に戻ったのか？


