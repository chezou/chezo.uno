---
title: 楽天モバイルを利用してiPhoneを海外で機種変するとSMS代がかかる
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: [misc]
date: 2023-08-06 16:50:23-07:00
lastmod: 2023-08-06 16:50:23-07:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [楽天モバイル, sms, アクティベーション, 海外, 機種変更, 料金, iphone, imessage, 請求, 回線]
recommendations: [/post/2011-09-25-doitudefonicnopuripeidosimwoshi-tuteguang-potaburuwoshi-sitemita/,
  /post/2022-11-28-cancel-japanese-service/, /post/2011-10-15-imessagewoipadtoiphonedeshi-ifen-kerufang-fa/]
---

## tl;dr

海外で楽天モバイル回線を使用したままiPhoneを機種変更すると、100円×N回の国際SMS料金が請求されるようになりました。

## 詳細

iPhoneを機種変更するときに、iMessage/Facetimeのアクティベーションに失敗し続けることがあります。

特に楽天モバイルでは、楽天回線の圏外でiMessageなどのアクティベーションをしようとすると失敗することが観測されてきました。

アクティベーションがうまくいかない時iPhoneの仕様上 +44 の番号へSMSが自動的に送り続けられます。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://discussions.apple.com/thread/8608970" data-iframely-url="//iframely.net/RDc3t4E"></a></div></div><script async src="//iframely.net/embed.js"></script>

ところで、海外で楽天モバイルを使う際、iPhoneだとSMSの送信や標準電話アプリでの電話の送受信で料金がかかります。

以前はこのアクティベーションのSMSは料金がかからなかったようなのですが、今年4月に機種変更をした際に2カ月遅れで謎の調整金という費目で1月後れで請求されるようになったようです。

この仕様はFAQにも書かれており、サポートに問い合わせてもこのドキュメントが出てくるだけです。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://network.mobile.rakuten.co.jp/faq/detail/00001698/" data-iframely-url="//iframely.net/Q04zQES"></a></div></div><script async src="//iframely.net/embed.js"></script>

![楽天モバイルのドキュメント](image.png)


調べても、ウェブの情報は海外では楽天モバイルが良いという情報しか出てこなかったので、備忘録として書き残しておきます。

2023年8月からpovoが海外ローミングをできるようになったようです。海外での番号維持及びSMSでの多要素認証には(eKYCのハードルを除くと)povoが一番よさそうです。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://povo.jp/service/international_roaming/" data-iframely-url="//iframely.net/rLcnF21?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://www.itmedia.co.jp/mobile/articles/2307/22/news056.html" data-iframely-url="//iframely.net/fPFk2T7?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>