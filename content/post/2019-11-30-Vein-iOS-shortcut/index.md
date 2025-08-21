---
title: VeinのiOSショートカット複数URL対応しました
authors: [aki]
summary: Androidの使い勝手を超えてしまった...
tags: [productivity]
date: November 30, 2019 4:16 PM
lastmod: December 9, 2019 3:42 PM
keywords: [ショートカット, 共有, ポスト, 対応, 複数, slack, 同時, twitter, post, facebook]
recommendations: [/post/2015-01-16-fei-enzinianokomiyuniteinislackwodao-ru-sitahua-number-ingress/,
  /post/2023-08-20-removed-slack-from-mobile/, /post/2023-01-10-ios-notification-management/]
---

![](https://images.unsplash.com/photo-1416816901131-9e5eab64c1c1?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

この記事は[pyspaアドベントカレンダー](https://adventar.org/calendars/3896)の10日目です。昨日は[turkyさんのキャンプの話](https://turky-in-the.blogspot.com/2019/12/blog-post.html)でした。

VeinはNextIntが作ってる情報共有プラットフォームです。内輪のコミュニティや会社の中で皆がなにを見てるのかをカジュアルに共有する場所です。

[Vein: コラボレーションのためのソーシャルブックマークサービス](https://introduction.vein.space/)

作った思いはところてんが山のように話してるので見てみてください。

[心理的安全性と、Veinの紹介　Psychological safety and introduction of Vein](https://www.slideshare.net/TokorotenNakayama/veinpsychological-safety-and-introduction-of-vein)

VeinはAndroidアプリしか現状モバイルにはないのですが、iOSはkikuchyさんの作ったショートカットがあります。

[https://twitter.com/kikuchy/status/1089824269175902208?s=21](https://twitter.com/kikuchy/status/1089824269175902208?s=21)

ただ、これはテキストに複数URLが入っているとうまく処理できなかったので改良しました(お前のことだぞ、ニコニコ漫画iOSアプリ！)

これでニコニコ漫画の尊い回をシェアし放題ですね。

[Veinにポスト(共有用、複数対応)](https://www.icloud.com/shortcuts/9231f779851640ab80572407d4af93d2)

また、Veinの隠し便利機能としてpostしたものをSlackに共有するというのができるのですが、僕はfavしたものをSlackのtimes的なチャンネルに流しています。で、いちいちveinにいってfavするのが面倒なのでfav対応のショートカットも作りました。最後のpostするときのパラメータに `vote=true` を入れているだけです。

[Veinにポスト(共有用、複数対応、fav)](https://www.icloud.com/shortcuts/664d86e293584f2fac598d2ab09c6829)

なお、余談ですが、ショートカット編集するとTwitterやFacebookなどショートカット対応アプリは同時に投げれます。Slackは無理でした。

Twitterとの同時投稿はこれを使えば出来ます。なお、Appを選んで差し替えればFacebookとの同時投稿もできます。

[Vein/Twitterにポスト(共有用、複数対応)](https://www.icloud.com/shortcuts/2759cccf677043519e4e29ee76ea4a4c)

明日はなんでも溶かすtaichiさんです。

---

[Back to home](https://memo.chezo.uno/)
