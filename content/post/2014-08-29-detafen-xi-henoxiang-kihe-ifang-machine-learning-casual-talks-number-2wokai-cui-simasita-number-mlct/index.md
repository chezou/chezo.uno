---
authors:
- aki
categories: null
date: '2014-08-29 15:07:00-07:00'
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
keywords:
- 機械学習
- 活用
- 素人
- データ
- ポイント
- 業務
- 比戸
- グノシー
- pfi
- deep learning
lastmod: '2014-08-29 15:07:00-07:00'
projects: []
recommendations:
- /post/2014-06-07-machine-learning-casual-talks-wokai-cui-simasita-number-mlct/
- /post/2017-10-20_oreilly-ml-for-business-cf835ff4c128/
- /post/2017-08-03_oss--------------48807bbbf13f/
subtitle: ''
summary: ''
tags: []
title: 'データ分析への向き合い方~Machine Learning Casual Talks #2を開催しました #MLCT'
---

先週火曜日に [Machine Learning Casual Talks #2](http://mlct.connpass.com/event/8036/) を開催しました。  
発表は、グノシー関さん、PFI比戸さん([@sla](https://twitter.com/sla))、[@motivic\_](https://twitter.com/motivic_)さん、カメリオから柴田さん、[@SamuraiT01](https://twitter.com/SamuraiT01)さんに発表頂きました。  
発表していただいた皆さん、Yahoo!Japanの[@qluto](https://twitter.com/qluto)さんはじめお手伝いいただいた皆さん、本当にありがとうございました！

togetterのまとめ([★](http://togetter.com/li/711785))

[2014/08/30追記]  
Gunosy関さんのスライドが落ちていたので追加しました。

# tl;dr

- 仮説なきデータ分析はやめよう
- 施策の価値を人手で検証して、必要に応じて機械学習を使おう

## 詳細

今回は、[@PENGUINANA\_](https://twitter.com/PENGUINANA_)さんが「機械学習とKPI」というテーマを所望されていたので、それで各スピーカーにお話いただきました。  
お互い示し合わせていなかったのに、Lean StartupのMVPの話を中心に話を組み立てていたのが非常に興味深かったです。  
特に、グノシーの創業者の一人関さんが「B to Cサービスの現場から考える機械学習活用」という発表をされたのですが、  
  
普段からクックパッド社内でも考える内容に非常にマッチしていて(機械学習をやるやらないは別にして)、データを活かす上での心づもりとして有益な情報でした。

<iframe allowfullscreen="true" allowtransparency="true" frameborder="0" height="596" id="talk_frame_115621" mozallowfullscreen="true" src="//speakerdeck.com/player/e0dba2400f2b0132e46c5af3d0e731c5" style="border:0; padding:0; margin:0; background:transparent;" webkitallowfullscreen="true" width="710"></iframe>

ポイントとしては以下の三点です。

- 機械学習の精度と、ユーザー価値は別物である
- まずは施策の価値を人手で作って(MPV)、検証後機械学習を適用する
- 仮説がなければKPIを追いかけても意味が無い

もう一つ、PFIの比戸さんの発表も、データを扱う人なら必見の内容です。

ビール大好きな人のコメントが的を射ています。

> このページ、機械学習に限らずデータほげほげ系であるあるすぎて、ウッってなるなｗ [http://t.co/wfOy3ngfrc](http://t.co/wfOy3ngfrc)
> 
> — tagomoris (@tagomoris) [2014, 8月 27](https://twitter.com/tagomoris/status/504443365681688576)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<iframe src="https://www.slideshare.net/slideshow/embed_code/38372284" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[あなたの業務に機械学習を活用する5つのポイント](https://www.slideshare.net/shoheihido/5-38372284 "あなたの業務に機械学習を活用する5つのポイント")** from **[Shohei Hido](http://www.slideshare.net/shoheihido)** 

  **[あなたの業務に機械学習を活用する5つのポイント](https://www.slideshare.net/shoheihido/5-38372284 "あなたの業務に機械学習を活用する5つのポイント")** from **[Shohei Hido](http://www.slideshare.net/shoheihido)** 

## LT

### @motivic\_ さん「素人がDEEP LEARNINGと他の機械学習の性能を比較してみた」

<iframe src="https://www.slideshare.net/slideshow/embed_code/38373205" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[素人がDeep Learningと他の機械学習の性能を比較してみた](https://www.slideshare.net/motivic/machine-learning-causal-talk-2-lt "素人がDeep Learningと他の機械学習の性能を比較してみた")** from **[motivic](http://www.slideshare.net/motivic)** 

どう見ても素人詐欺です、本当にありがとうございました

### @samurai01T さん「カメリオの記事の本文抽出」

内容もさることながら、初心者向けの機械学習おすすめ本の提示がよかったです。[わかパタ](http://www.amazon.co.jp/dp/4274131491)は読みやすくていい本ですね。

本文抽出といえば、 [@shuyo](https://twitter.com/shuyo) さんのExtractContent([slide](http://www.slideshare.net/shuyo/web-using-crf),[Ruby1.9対応版](https://github.com/mono0x/extractcontent))を使っていた記憶が蘇りました。

### Akira Shibataさん「カメリオ精度向上に使った学習アプローチ」

最適化手法は古典的な方法を使っているそうなのですが、特徴的なのがクラウドワークスを使ってラベルを収集していること。  
USだとAmazon Mechanical Turkを使うのが一般的に行われているのですが、日本でマイクロタスクを出して機械学習の正解データを作っているというのは感慨深いものを感じました。

## まとめ

グノシー関さんの「数値は神である」、PFI比戸さんの「機械学習は苦しい」という話に表されるように、機械学習を「つかう」という点にフォーカスした会でしたが、機械学習をしない人にとっても、どうデータと向きあえばいいのか、というエッセンスが凝縮されていました。  
僕自身も聞いていて"Lean Analytics"にあった、「行動に移せない指標は意味が無い」という話を具体的にした話を聞けて、局所最適解に陥らないデータ活用について考えさせられました。