---
title: Googleカレンダーの場所情報をGoogleマップに表示する方法
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2011-03-04 22:00:54+00:00
lastmod: 2011-03-04 22:00:54+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [googleカレンダー, yahoo!, カレンダー, url, 地図, xml, 情報, マップ, options, google calendar]
recommendations: [/post/2010-12-17-wu-liao-deiphonenobiao-zhun-karendaniakapera-slash-he-chang-karendawobiao-shi-surufang-fa/,
  /post/2010-02-21-akaperanoibentoqing-bao-tokawotubuyaku-at-acappella-eventnoshi-ifang/,
  /post/2010-01-19-he-chang-toakaperanokarendawogoogle-calendardezuo-tutemita/]
---
[アカペラ/合唱イベントカレンダー](https://www.google.com/calendar/b/0/embed?src=YWNhcHBlbGxhLmV2ZW50QGdtYWlsLmNvbQ&gsessionid=OK)に登録していると、ふとイベント情報の開催地を地図上に表示したくなりました。

探してみると、[こんな記事](http://ouseful.open.ac.uk/blogarchive/012594.html)があってYahoo!pipesを使ってやった人がいるようです。(日本語の紹介記事は[こちら](http://google-mania.net/archives/886))

どうやるかというと、Google CalendarのXMLのアドレス(カレンダー設定のところにあるURL)を[こちらのYahoo! Pipes](http://pipes.yahoo.com/pipes/pipe.info?_id=ddfff253dd131105be36791db9890fc5)につっこみます。  
More Optionsで得られるKMLデータのURLをGoogleマップのクエリに投げるとできあがりです。

[こんな感じ](http://maps.google.co.jp/maps?q=http%3A%2F%2Fpipes.yahoo.com%2Fpipes%2Fpipe.run%3FURL%3Dhttp%253A%252F%252Fwww.google.com%252Fcalendar%252Ffeeds%252Facappella.event%252540gmail.com%252Fpublic%252Fbasic%26_id%3Dddfff253dd131105be36791db9890fc5%26_render%3Dkml)になります。

ただ、Googleマップに表示はしているものの、Googleカレンダーの場所情報から地図情報に変換しているのは米Yahoo!の仕事なためか、精度がよろしくありません。

頑張って、GoogleカレンダーとマップのAPIを使って処理するしかないのでしょうか。。。


