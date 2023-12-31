---
title: Nas Navigator2をWindows7(64bit)で動かす方法
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2009-11-11 12:11:25+00:00
lastmod: 2009-11-11 12:11:25+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [実行, exe, nas, ショートカット, mac os x, 管理者, スタートアップ, navigator, パケット, setup]
recommendations: [/post/2009-10-26-nas-navigator2gae-sawosuru-at-windows7-64bit/,
  /post/2009-10-25-macdui-ying-siteinainasnopurintosabaji-neng-woshi-uniha/, /post/2009-05-16-apple-storegawell-back-soonni-dot-dot-dot/]
---

[以前、動かないと言っていたNas Navigator2](https://chezo.uno/post/2009-10-26-nas-navigator2gae-sawosuru-at-windows7-64bit/)ですが、なんとか動かすことに成功しました。グラフィックボードのドライバ関係もあって、再インストールした後に行いました。

1．管理者権限で、setupを実行する  
2.nassvc.exeを管理者権限で実行できるようスタートアップにショートカットを置く

つまり、nassvc.exeがNASの自動実行のためのパケットを出し続けているようです。ただ、管理者でないユーザでの実行は確認していないです。

[Mac OS X 10.6 Snow Leopardの方が大変みたいですね。](http://d.hatena.ne.jp/tadamesi/20090913/p2)Buffaloはちと最近厳しいのかなぁ。


