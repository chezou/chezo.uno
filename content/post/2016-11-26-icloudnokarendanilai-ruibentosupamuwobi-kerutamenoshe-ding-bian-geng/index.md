---
authors: [aki]
categories: null
date: '2016-11-26 05:17:55-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2016-11-26 05:17:55-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: icloudのカレンダーに来るイベントスパムを避けるための設定変更
keywords: [icloud, カレンダー, 通知, 設定, 削除, png, spam, 招待, calendar, メール]
recommendations: [/post/2010-12-17-wu-liao-deiphonenobiao-zhun-karendaniakapera-slash-he-chang-karendawobiao-shi-surufang-fa/,
  /post/2023-01-10-ios-notification-management/, /post/2011-03-03-dropboxgahtmlgong-kai-wojian-dan-nisuru-at-acappella-eventguan-lian-matomesaitozuo-cheng-sitemita/]
---

最近、めちゃくちゃicloudのカレンダーにレイバンのスパムが来るようになってうざいので、通知されないように回避するためのicloudの設定方法を書いておく。

# 1. PCのブラウザでiCloud.com へ行きカレンダーを開く

![](20161126130933.png)

# 2. 左下の歯車から環境設定を開く

![](20161126130701.png)

# 3. 「詳細設定」の「イベント参加依頼の受信方法」の設定を「xxxx@yyyy.comへメールを送信」にする

![](20161126130707.png)

この設定にすると、設定したメールアドレスに通知が来るのでメールを削除するだけになる。

# 補足

追加された予定を通知しないように削除するには、icloudに新規カレンダーを追加してそちらに移動してから、カレンダーごと削除すると招待した輩に通知をすることなく消せる
![](20161126131353.png)

## 参考サイト

[Many iCloud users receiving spam Calendar &amp; Photo Sharing invitations, here’s how to fix](https://9to5mac.com/2016/11/09/icloud-photo-sharing-and-calendar-spam)
[Preventing Spam iCloud Calendar Invites](https://astralbodi.es/2016/11/25/preventing-spam-icloud-calendar-invites/)
[iPhone、MacのiCloudカレンダーに大量のスパム招待が来たときの対処法 - だがそれがいい](http://www.dagasorega-e.net/entry/iphone-mac-spam-calender">www.dagasorega-e.net)