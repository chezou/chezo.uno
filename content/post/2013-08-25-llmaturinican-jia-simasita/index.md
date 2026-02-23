---
authors: [aki]
categories: null
date: '2013-08-25 15:05:14-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2013-08-25 15:05:14-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: LLまつりに参加しました
keywords: [ll, 勉強会, アンチパターン, セッション, トラック, プレゼンテーション, deploy, 参加, 開催, メリット]
recommendations: [/post/2022-06-18-kawasaki rb 9 years reflection/, /post/2016-08-23-chuan-qi-rubyhui-yi-01wokai-cui-simasita-number-kwsk01/,
  /post/2014-12-31-2014nian-wozhen-rifan-tute/]
---

年に一度の軽量言語のイベント、LLまつりに行ってきました。

[LLまつり - Lightweight Language Matsuri](http://ll.jus.or.jp/2013/)

過去にも、LL Planet,Decadeと参加してきましたが、今年は初めてのマルチトラックになりました。

Ruby Kaigiもそうだったのですが、複数トラックあるのは良し悪しあるなぁというのが正直なところでした。  
狭い方の会場が埋まってしまったりとか、裏番組が盛り上がっているのがTwitterで流れてくるとしまった！と思ったりとか(笑)

参加したのは、以下の3つのセッションを聞きました。

- 午前のプレゼンテーショントラック
- とびだせ！LL〜リアル世界をプログラミングする〜
- Infrastructure as LL
個人的に印象に残ったのは、[よしおかさん](https://twitter.com/hyoshiok)の勉強会アンチパターンとInfrastructure as LLでした。

## 勉強会アンチパターン
内容は下記のサイトに詳しいですが、勉強会を主催・発表していく上でどうやったら継続的に開催できるか、というのがテーマ。

[勉強会アンチパターン #llmatsuri - by shigemk2](http://d.hatena.ne.jp/shigemk2/20130824/1377310877)

アンチパターンに入るのがラスト3分とか、色々突っ込みどころは大きかったですが、  
個人的には、

- 勉強会勉強会というメタな勉強会(というかカンファレンス？)がある
- 「月に300以上のIT勉強会が開催している。その成功・失敗を共有できたらいいのでは」
- いかに価値を創造するか？
という点に共感、というか考えさせられました。

「開催/発表/参加コストよりメリットのほうが上回らないと続かない」という指摘もごもっともで、  
いかにコストを下げるか/メリットを上げるかを考えていくのは大事だなーと。

ちょうど、[Kawasaki.rb](https://sites.google.com/site/kawasakirb/)を始めたこともあり、継続的に続けていけたらと思います。

## Infrastructure as LL
伊藤直也([@naoya\_ito](https://twitter.com/naoya_ito))さんと、ペパボの黒田([@lamanotrama](https://twitter.com/lamanotrama))さん、クックパッドの成田([@mirakui](https://twitter.com/mirakui))さんによる、Chefやpuppetなどを中心としたDevOpsの話。

特に印象に残ったのは、伊藤直也さんの

> 「昔、10台くらいのサーバにdeployをしてくれる人がいたが、typoとか繰り返すと怒られるのが嫌でdeployしづらくなった」

という経験から、DevOpsの流れを求めていたという話がある中で、

> 「今は、逆にInfra側が(流行に乗って)Chefとかを導入することが目的になって、Devとの距離ができているのではないか？原点を見失ってはいけない」

という指摘が、本質は何か？ということを考え続けて進めていくのが大事だと、改めて気付かされました。  
誰が何を求めているのか？嬉しくなるのか？ということですよね。

結局、その流れで考えると、開発者にとってはHerokuのようなPaaS的なインフラを意識しないでデプロイできる環境がが求められていて、@sora\_hさんがその環境を作っているなど、世の中としても方向に向かっているようです。

ちなみに、「入門Chef Solo」は5000部売れていて、おそらく日本で一番売れてる技術書の電子書籍では？とのことでした。

## まとめ
今年は、チュートリアルセッションやプレゼンテーショントラックなど多様なセッションがあり、例年よりも偏らずに幅広い話が聞けて楽しめました。