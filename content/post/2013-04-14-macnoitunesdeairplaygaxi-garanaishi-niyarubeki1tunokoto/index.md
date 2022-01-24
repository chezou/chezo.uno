---
title: MacのiTunesでAirPlayが繋がらない時にやるべき1つのこと
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2013-04-14 10:04:52+00:00
lastmod: 2013-04-14 10:04:52+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [airplay, サーバ, mac, オフ, ターミナル, raspberry pi, 対処法, この先, client, appletv]
recommendations: [/post/2013-01-09-windowsdeairplaywoshi-unarashairport4w/, /post/2015-11-02-amazon-fire-tv-stickwomai-tutaraapple-tv-plus-chromecast-tiyotutoninatuta/,
  /post/2009-10-25-macdui-ying-siteinainasnopurintosabaji-neng-woshi-uniha/]
---
先日、WindowsマシンをAirPlayサーバにする[Shairport4wの話を書きました](https://chezo.uno/post/2013-01-09-windowsdeairplaywoshi-unarashairport4w/)が、
その後[Raspberry piをAirPlayサーバにする方法](http://www.lifehacker.jp/2013/03/130306raspberry_piairplay.html)など各所でAirPlayサーバが盛り上がっています。

しかし、実際に使っていると、iPhoneからは飛ばせるのにMacのiTunesからだとAirPlayサーバにつながらない事態が頻発しました。(AppleTVでも同様でした)

調べてみたところ、どうやらMacのIPv6をオフにすれば良いとのこと。

Macのターミナルをたちあげて

> networksetup -setv6off Wi-Fi

と入力するだけ。

どうやら、AirPlayサーバがIPv4でlistenしているのに、Clientがv6で話かけていることが原因のようです。

でも、この先IPv6オフにしていていいんだろうか。。。

参考URL：

- [もぐてっく：RaspbmcのAirPlayでハマったでござる](http://moguno.hatenablog.jp/entry/2013/01/12/193138)
- [AirPlayの音が途切れる問題の対処法まとめ](http://www.pleiades.or.jp/misc/AirMacExpress/StreamStoppingTrouble.html)
 
