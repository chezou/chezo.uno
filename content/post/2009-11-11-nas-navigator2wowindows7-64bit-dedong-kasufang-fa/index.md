---
authors: [aki]
categories: null
date: '2009-11-11 04:11:25-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2009-11-11 04:11:25-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: Nas Navigator2をWindows7(64bit)で動かす方法
keywords: [実行, exe, nas, mac os x, ショートカット, 管理者, navigator, パケット, スタートアップ, setup]
recommendations: [/post/2009-10-26-nas-navigator2gae-sawosuru-at-windows7-64bit/,
  /post/2009-05-31-linkstationnowebakusesutosimplify-music-2-at-iphone/, /post/2013-04-14-macnoitunesdeairplaygaxi-garanaishi-niyarubeki1tunokoto/]
---

[以前、動かないと言っていたNas Navigator2](https://chezo.uno/post/2009-10-26-nas-navigator2gae-sawosuru-at-windows7-64bit/)ですが、なんとか動かすことに成功しました。グラフィックボードのドライバ関係もあって、再インストールした後に行いました。

1．管理者権限で、setupを実行する  
2.nassvc.exeを管理者権限で実行できるようスタートアップにショートカットを置く

つまり、nassvc.exeがNASの自動実行のためのパケットを出し続けているようです。ただ、管理者でないユーザでの実行は確認していないです。

[Mac OS X 10.6 Snow Leopardの方が大変みたいですね。](http://d.hatena.ne.jp/tadamesi/20090913/p2)Buffaloはちと最近厳しいのかなぁ。