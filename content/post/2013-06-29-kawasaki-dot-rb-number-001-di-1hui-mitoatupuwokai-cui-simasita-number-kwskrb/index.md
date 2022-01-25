---
title: 'Kawasaki.rb  #001 第1回ミートアップを開催しました #kwskrb'
date: 2013-06-29 04:06:14+00:00
subtitle: ''
summary: ''
draft: false
featured: false
authors: [aki]
lastmod: 2013-06-29 04:06:14+00:00
tags: []
projects: []
image: {caption: '', focal_point: '', preview_only: false}
categories: [ruby]
keywords: [hash, gc, ruby, hadoop, 遅い, python, 拡張, kawasaki, doorkeeper, 内容]
recommendations: [/post/2013-08-03-kawasaki-dot-rb-number-002-kai-cui-simasita-number-kwskrb/,
  /post/2014-03-01-kawasaki-dot-rb-number-009wokai-cui-simasita-number-kwskrb/, /post/2015-11-08-tinysegmenter-dot-jlwogotobi-jiao-sitefu-ketatosi-tutararuo-zhe-gazui-shi-hua-sitekureta/]
---
6/26にKawasaki.rbの第1回ミートアップを開催しました。

## [Kawasaki.rb #001](http://kawasakirb.doorkeeper.jp/events/4115)

## 
ありそうで以外となかった、川崎でのRubyの勉強会です。  
初心者からコアな人までざっくばらんに話が出来ればと思って始めました。  
Doorkeeperの参加者を見ていただくとわかるのですが、予想以上に豪華な顔ぶれでhomeなはずなのに、ドキドキが止まりませんでした。(参加者の2割近くコミッターとか！！！)

当日、NKT77さんとたるいさん([@taru](http://twitter.com/taru))にトークをしてもらいました。

@kishimaさんによるtogetterまとめは[こちら](http://togetter.com/li/525981)。

## 01. NKT77さん 「Hadoop with Ruby-僕がPythonを選んだ理由」
このタイトル自体は僕が付けた釣り仮題なのですが、内容としてはRubyをHadoop Streamingで使うときにHashが遅いという事例の紹介でした。([モリスさんを釣ってしまって](http://b.hatena.ne.jp/entry/kawasakirb.doorkeeper.jp/events/4115)恐縮したのはここだけの話)

[slideshare id=23692953&doc=20130630kawasaki-130630003650-phpapp01]  
(2013/07/04 資料を追加しました)

ざっくりまとめると

- Hadoop streamingでRubyを使うときに、Stringで100万程度のkeyのHashを作ると結構遅い
- HashのLookupも非線形に速度が増えている
- Pythonにしたら10倍速くなった(AWSのEMR料金も10分の1に！)
という内容です。しかし、AWSのおかげで処理時間=お金に換算できる世界になったのが、改めてインパクトが大きいですね...。

なお、HashがPythonと比較して遅い原因としては、

1. GC
2. Hash関数がsiphashなため
3. rehashの際の閾値がRubyの方が保守的
といった理由が考えられるとのことでした。(間違いがあればご指摘ください)
## 02. たるいさん(@taru) 「メモリアロケーションからみた拡張ライブラリに大切なこと」
[slideshare id=23517958&doc=random-130626101518-phpapp02]

資料を見ていただければ内容はわかると思います。

- 初めての拡張ライブラリの作り方
- ArrayがGCされないようにRB\_GC\_GUARD()しましょう
- GC.stress = trueすると、GC強制的に走らせて再現しにくいバグを潰せる
- NKT77さんが報告していたGCのせいでHashが遅いのはtrunkでは改善しました！(凄い！)
最後の、Hashの速度向上については田中哲さんも確認されたようです。


{{< tweet user="tanaka_akr" id="350600581003485184" >}}


当日は散々、「Rubyの集まりじゃないのかよ！」とか「Pythonを宣伝する場所かよ！」とか突っ込まれていましたが、これで皆さん安心してHadoop StreamingでRubyを使ってもらえますね。

今後は、初心者にやさしいネタも考えつつ進めて行きたいと思います。（いらないのかな？)

次回は、7/24(水)に居酒屋LT(というか焼肉LT)をやりますので、準備ができましたら有る方はメーリングリストとDoorkeeperで告知しますので、興味があれば登録していただければと思います。


