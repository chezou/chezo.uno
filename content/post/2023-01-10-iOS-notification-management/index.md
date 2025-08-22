---
authors:
- aki
date: '2023-01-10 16:58:00-08:00'
keywords:
- 通知
- モード
- 集中
- アプリ
- オフ
- gmail
- slack
- ログアウト
- パーソナル
- 機能
lastmod: '2023-01-10 17:20:00-08:00'
recommendations:
- /post/2023-08-20-removed-slack-from-mobile/
- /post/2016-11-26-icloudnokarendanilai-ruibentosupamuwobi-kerutamenoshe-ding-bian-geng/
- /post/2015-01-16-fei-enzinianokomiyuniteinislackwodao-ru-sitahua-number-ingress/
summary: iOS15からの集中モードを利用した休暇中の通知管理について
tags:
- iOS
- Notification
title: iOSでの休暇中の仕事の通知管理
---

![](https://images.unsplash.com/photo-1504507926084-34cf0b939964?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

iOS15から集中モードが加わって、その中でもパーソナル集中モードというのがあったので、年末年始の休暇に試してみた。

簡単に言うと、パーソナル集中モードでは業務用のアプリからの通知をオフにできるというのが一番のメリットだ。

以下の記事に大まかな概要が書いてあってわかりやすい。

[iOS 15新機能「集中モード」とは？おやすみモードやマナーモードとの違いなど紹介](https://time-space.kddi.com/mobile/20220202/3256)

Androidではwork profileがあるので、[それを使えばいいのでもうちょっとスマートにできる](https://support.google.com/work/android/answer/7029561?hl=ja)が、iOSではごちゃまぜの世界観なのがとても厳しいと思っていたところだった。

実際に試してみた結果、いくつかの問題が出てきた。

1. GmailやSlackなど仕事でもプライベートでも使っているアプリで通知がコントロールしきれない
2. 通知を知らせないアプリに指定しても、対応していないため突き抜けてくる（Confluence、お前のことだぞ）

2個目は仕方がないので通知を完全にオフにして心の平穏を保つことにした。別にAtlassianアプリからの通知はSlack連携とかもしてるし不要だと気づいた。

1個目は、Gmailに関しては一応アカウントごとに通知をオフする機能があったので、それでオフにした。ただし、これだと「すべての受信トレイ」で突き抜けてくるので、ぐっと堪える必要がある。正直、気持ち悪い。

Slackについては、通知のスヌーズはあるけれど、これやってもバッジの数がぐんぐん成長してmentionを受けるたびに数が増えてきて気持ちが悪いので、サポートに問い合わせたところ、その組織からsign outしてください、とのことだった。そうですか、と思いながらサインアウトしたけど、機能要望は出しておいた。

Gmailもすべての受信トレイのバッジ出すならログアウトするほうがいいのかもしれない。でも、毎週末ログアウトしてサインインするのはとてもじゃないけれどやってられない。

なお、Apple製のメール、カレンダーなどのアプリはアカウントごとにフィルターする機能がある（のに今気づいた）ので、これを設定すれば通知が来なくなりそうだ。

[「集中モードフィルタ」はどう活用するの? - いまさら聞けないiPhoneのなぜ](https://news.mynavi.jp/article/20221014-iphone_why)

Android版Apple Musicといい、iOS版Google Podcastといい、相手のプラットフォームだと痒いところに手が届かなくなるのは、宿命なのだろう。

サードパーティ製のアプリは、気になるようであれば都度サインアウトして復帰時にサインインするしかやはりなさそうである。ただし、某社のように休日に対応しないとレイオフが走るような会社の人には使えないだろう。

---

記事が気に入ったらbuymeacoffeeでサポートしていただけると嬉しいです

[chezou is a podcaster and technical blogger and open source developer](https://www.buymeacoffee.com/chezou)

---

[Back to home](https://memo.chezo.uno/)