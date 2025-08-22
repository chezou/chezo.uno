---
authors:
- aki
categories: null
date: '2011-03-03 14:00:49-08:00'
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
keywords:
- css
- サイト
- カレンダー
- マシン
- twitter
- 移行
- windows
- 随時
- ほしかっ
- sass
lastmod: '2011-03-03 14:00:49-08:00'
projects: []
recommendations:
- /post/2010-02-21-akaperanoibentoqing-bao-tokawotubuyaku-at-acappella-eventnoshi-ifang/
- /post/2010-12-17-wu-liao-deiphonenobiao-zhun-karendaniakapera-slash-he-chang-karendawobiao-shi-surufang-fa/
- /post/2010-01-19-he-chang-toakaperanokarendawogoogle-calendardezuo-tutemita/
subtitle: ''
summary: ''
tags: []
title: DropboxがHTML公開を簡単にする- @acappella_event関連まとめサイト作成してみた
---

## 何を作ったか？
@acappella\_eventがつぶやいているアカペラ/合唱カレンダーを見やすくはっつけるサイトがほしかったんです。  
あと、Pana Musicaの新刊botがつぶやいている新刊情報も見やすくしたかったんです。

で、ここにできたものがあります。  
[http://dl.dropbox.com/u/171669/acappella.html](http://dl.dropbox.com/u/171669/acappella.html)

[2011/12/10追記]  
現在はこちらに移行しております。(ほとんど同じ物ですが)  
[http://acappella-bot.appspot.com/](http://acappella-bot.appspot.com/)

## なぜ、Dropboxか？
Wordpress.comはiframeやscriptが使えないという安心設計になっているため、google calendarやtwitterのTLウィジェットを貼り付けることができませんでした。

で、それらを見るためのサイトをGoogle App Engine上においてみようかとも思ったのですが、マシンを移行したこともあり面倒だなぁと思っていました。

そんな折に、[この記事](http://www.lifehacker.jp/2010/05/100507dropboxtips.html)を見つけたわけです。簡単に言うと、HTMLをDropboxのPublicフォルダに置くと、公開できるというもの。

**レンタルサーバも要らなければ、広告も入らない。** うまくやれば、 **CSSも使えるんじゃね？** と思い始めてみたわけです。

## できた
以前読んだ、HTML5とCSS3使うと簡単に？サイトが見栄え良くできるという[記事](http://yoppa.org/taumedia10/1695.html)を参考に、もりもり書いていきました。

正直言うと、最近HamlやらSassをSinatraとともに使っていたので、生のコード書くのだるいとか思っていましたが、Windows付属のメモ帳で2時間くらい調べながらかけて書いたらできあがりました。xyzzy入ってないマシンでやるもんじゃないですね。Windows7はUTF-8のファイルがはけるようになったから、勢いでやってしまいました。

ちなみに、カレンダーに情報登録してくださる方は随時募集しておりますので、@chezouまでtwitterでご連絡ください。