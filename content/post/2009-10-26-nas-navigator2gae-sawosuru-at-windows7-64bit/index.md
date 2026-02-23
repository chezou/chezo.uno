---
authors: [aki]
categories: null
date: '2009-10-26 14:56:21-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2009-10-26 14:56:21-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: NAS Navigator2が悪さをする@Windows7 64bit
keywords: [nas, 追記, ダメ, 下手, note, 積極的, linkstation, exe, 管理者, navigator]
recommendations: [/post/2009-11-11-nas-navigator2wowindows7-64bit-dedong-kasufang-fa/,
  /post/2009-10-23-windows7-64bitwodg33tlmninantokadao-ru-sita/, /post/2016-10-29_homebrew-----iruby---------------6a02e5194ff2/]
---

091111追記：解決方法は[こちら](http://wp.me/pvR30-d2)。

一回だけなんですが、Nas Navigator2がRun time errorを出してくれました。

で、調べてみると[こんな記事が  
Note - imatakutin's Mind Map: NasNavi.exe で Runtime Error!](http://imatakutin.blogspot.com/2008/05/nasnaviexe-runtime-error.html)

どうも、管理者モードでインストールしないとダメみたいです。  
で、改めてアンインストールしようとしたら、それができない。コンパネからもスタートメニューからも、ダメ。BuffaloはWindows7（というか64bit？）対応があまり積極的でないとも聞きます。そろそろio-dataに切り替え時なのかなぁ。

追記：  
ネットワーク上のTera/LinkStationを検索中です　が出て止まりません！NASにも三角アイコンがついてるし……。だめだぁ、こりゃ

さらに追記：  
なぜか、スタート→すべてのプログラム経由でアンインストールできた。下手に互換モードとかにしてもいけないみたい。よくわからん。ダメルコの時代に戻ったのか？