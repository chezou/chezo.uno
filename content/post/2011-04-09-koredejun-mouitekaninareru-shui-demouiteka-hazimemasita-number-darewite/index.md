---
title: "これで君もウィテカーになれる！？「誰でもウィテカー」はじめました #darewite"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2011-04-09T22:01:23+00:00
lastmod: 2011-04-09T22:01:23+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
20110409追記：Whitacre氏が改めて[来日すると連絡いただいた](http://twitter.com/hanagoro/status/56563103596412928)そうです！[福島にも](http://twitter.com/hanagoro/status/56563939382804481)！

最近、日本の演奏会でもよく演奏される人気の合唱作曲家、[Eric Whitacre](http://twitter.com/ericwhitacre)。先日公開された、Virtual Choir 2.0でもおなじみですね。

そんなEric Whitacreになりきれる、「誰でもウィテカー」という何の役にも立たないTwitterサービスを始めました。  
使い方は簡単。  
[http://bit.ly/darewite](http://bit.ly/darewite) にアクセスしてツイートするだけ。そうすると、Whitacreの口癖である"Woo hoo!"というノリノリワードをツイートできます。さらに、クライアント名が「誰でもウィテカー」になります。

[http://twitter.com/chezou/status/56543442930638848](http://twitter.com/chezou/status/56543442930638848)

使用例：

- 明日は給料日だぜ Woo hoo!
- 今度のTED Talksに呼ばれちゃったぜ Woo hoo!
- うちの娘が可愛すぎてやばい Woo hoo!
- クリスマスは彼女と過ごすぜ。画面から出てきてくれないけどな Woo hoo!
- 「誰ウィテ」でツイートしてたら、ドンドン合唱曲のイメージがわいてきて作曲しまくりだぜ Woo hoo!
え、本当に口癖かって？ほらね。使ってるでしょ  
[http://twitter.com/ericwhitacre/status/56526873529819136](http://twitter.com/ericwhitacre/status/56526873529819136)

え？Virtual Choir 2.0を知らないって？この動画を早く見るんだ！

{{< youtube 6WhWDCw3Mng >}}

## 

本当に口癖か調べてみた今回、「誰でもウィテカー」を作るにあたって、「最近、よくウィテカーは"Woo hoo!"って連呼してるよな。ReplyもWoo hoo!だけのとかあるし」という直感からウィテカーになりきるには"Woo hoo!"といえば良い！ということになりました(笑)

本当にWhitacreの口癖が"Woo hoo!"か調べてみました。

今回は、Pythonとnltkを使って最近200ツイートを調べてみました。すると、驚くことにbi-gram(2語)の頻度を見てみると

> Woo hoo! 10  
> Virtual Choir 9  
> of the 6  
> to the 6  
> Choir 2.0 5  
> one of 5  
> with the 5  
> I could 4  
> and I 4  
> at the 4

なんと言うことでしょう、"Virtual Choir"よりも"Woo hoo!"の方が頻度が高いではありませんか！

ちなみに、uni-gram(1語)を見てみると、

> the 61  
> I 46  
> ";-)" 42  
> you 29  
> a 28

第3位に";-)"という顔文字が(絵文字に変換されてしまうため""でくくっています)。この顔文字も使えば大丈夫。特に、適当なReplyをしたいときに

> @XXXXXX  ";-)"

を使えば完璧です。

ちなみに、tri-gram(3語)の頻度を見ると、安心の結果が出ています。

> Virtual Choir 2.0 5  
> tell you how 4  
> Wish I could 3  
> the Virtual Choir 3

## まとめ
WhitacreになりきれるWebサービス、「誰でもウィテカー」を始めました。  
ウィテカーになりきるには、"Woo hoo!"と";-)"を使えばOK！
## 参考URL

- [「※この発言は個人の見解であり、所属する組織の公式見解ではありません」をリリースしました - 床のトルストイ、ゲイとするとのこと](http://d.hatena.ne.jp/mirakui/20110220/1298213272)(Twitter@Anywhereの参考にさせていただきました)
- [Twitter＠Anywhereの使い方WordPress編  |  wpxtreme](http://wpxtreme.jp/how-to-use-twitter-at-anywhere-with-wordpress)  
(Twitter@Anywhereの参考にさせていただきました)
- [Python Hack-a-thon #3に参加しました - nokunoの日記](http://d.hatena.ne.jp/nokuno/20100123/1264239192)  
(NLTKの参考にさせていただきました)

