---
title: "MacのiTunesでAirPlayが繋がらない時にやるべき1つのこと"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2013-04-14T10:04:52+00:00
lastmod: 2013-04-14T10:04:52+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
先日、WindowsマシンをAirPlayサーバにする[Shairport4wの話を書きました](http://chezou.wordpress.com/2013/01/09/windows%e3%81%a7airplay%e3%82%92%e4%bd%bf%e3%81%86%e3%81%aa%e3%82%89shairport4w/ &quot;WindowsでAirPlayを使うならShairport4w&quot;)が、  
その後[Raspberry piをAirPlayサーバにする方法](http://www.lifehacker.jp/2013/03/130306raspberry_piairplay.html)など各所でAirPlayサーバが盛り上がっています。

しかし、実際に使っていると、iPhoneからは飛ばせるのにMacのiTunesからだとAirPlayサーバにつながらない事態が頻発しました。(AppleTVでも同様でした)

調べてみたところ、どうやらMacのIPv6をオフにすれば良いとのこと。

Macのターミナルをたちあげて

&gt; networksetup -setv6off Wi-Fi

と入力するだけ。

どうやら、AirPlayサーバがIPv4でlistenしているのに、Clientがv6で話かけていることが原因のようです。

でも、この先IPv6オフにしていていいんだろうか。。。

参考URL：

- [もぐてっく：RaspbmcのAirPlayでハマったでござる](http://moguno.hatenablog.jp/entry/2013/01/12/193138)
- [AirPlayの音が途切れる問題の対処法まとめ](http://www.pleiades.or.jp/misc/AirMacExpress/StreamStoppingTrouble.html)
&amp;nbsp;
