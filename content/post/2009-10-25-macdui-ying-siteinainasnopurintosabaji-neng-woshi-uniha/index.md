---
authors: [aki]
categories: null
date: '2009-10-25 14:56:16-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2009-10-25 14:56:16-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: Mac対応していないNASのプリントサーバー機能を使うには
keywords: [mac, nas, windows, 共有, ドライバ, mp, 印刷, トライ, mac os x, canon]
recommendations: [/post/2009-10-23-windows7gakita-ru-reta-xp-modeshi-sita/, /post/2013-04-14-macnoitunesdeairplaygaxi-garanaishi-niyarubeki1tunokoto/,
  /post/2009-05-31-linkstationnowebakusesutosimplify-music-2-at-iphone/]
---

前々からやりたいと思っていたのだができなかったことだったのだが、今回Windows7を導入にあたってトライしてみたらあっさりできた。基本発想としては、Windows用にsamba経由で共有されているNASなのだから、MacのWindows用プリンタの共有を使ってみたら？という考えだ。  
これが、見事に的中した。

環境は、  
Printer:Canon MP610  
NAS:[**LHD-LAN300**](http://www.logitec.co.jp/products/nas/lhdlan.html)  
Mac OS X  Leopard

1.[Gutenprint](http://gimp-print.sourceforge.net/MacOSX.php)の最新版をインストールする  
2.Macの「プリンタ設定ユーティリティ」から＋ボタンを押し「ほかのプリンタ」を追加する  
3.ネットワーク上で見えるNASのWorkgroupの下にあるプリンタを選び、ドライバはMP610の後ろにGimpprintとか書いてあったと思います。

以上で完了です。最初ドライバが見つからなかったときはどうしようかと思いましたが、意外とすんなりといけました。

参考：  
[Windows XPとMac間でプリンタ共有がうまくできない](http://ziddy.japan.zdnet.com/qa4596446.html)  
[Open the Next: Mac: Windowsマシンの共有プリンタへ印刷する](http://blog.manabii.info/2006/02/mac-windows.html)