---
title: 機械学習工学研究会の「機械学習基盤 本番適用と運用の事例・知見共有会」を開催しました
subtitle: ''
summary: ''
authors: [aki]
tags: [mlops]
categories: [Machine Learning, MLOps, Conference]
date: 2020-11-10 22:18:19+09:00
lastmod: 2020-11-10 22:18:19+09:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [基盤, 機械学習, 本番, 適用, 運用, 事例, 当日, 知見, 要件, アーキテクチャ]
recommendations: [/post/2020-12-31-2020-review/, /post/2020-07-11-mlse-summer-workshop/,
  /post/2014-08-29-detafen-xi-henoxiang-kihe-ifang-machine-learning-casual-talks-number-2wokai-cui-simasita-number-mlct/]
---


[@masaru_dobashi](https://twitter.com/masaru_dobashi)さん共同で、機械学習工学研究会（MLSE）本番適用のためのインフラと運用WG主催の、「機械学習基盤 本番適用と運用の事例・知見共有会」をオンライン開催しました。

イベントのconnpassは以下のリンクです。
[機械学習基盤 本番適用と運用の事例・知見共有会](https://mlxse.connpass.com/event/187583/)


[@wakame1367](https://twitter.com/wakame1367)さんによるツイートのまとめはこちらです。
[機械学習基盤 本番適用と運用の事例・知見共有会 ツイートまとめ](https://togetter.com/li/1619107)


## YouTubeの動画

YouTube Liveの配信はアーカイブとして見ることができます。

{{< youtube nNFCc3nowfg >}}

## 当日の資料

<p><iframe src="https://docs.google.com/presentation/d/19P_hAZw8W9X1myeV1wuKYVEAHZsOl3-ohcV1E4wug7g/embed?start=false&loop=false&delayms=3000" frameborder="0" width="800" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe></p>

<p><iframe src="https://docs.google.com/presentation/d/1Vc-Sf0hMq5RKBDIDAI0aUdS-YWaiie306WykUG7dtJU/embed?start=false&loop=false&delayms=3000" frameborder="0" width="800" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe></p>

<script async class="speakerdeck-embed" data-id="af1c9b53d63b4e6baa85652793ec4ca9" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

<script async class="speakerdeck-embed" data-id="230d7fccb9314f039a8ab55aaf58c62c" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

<script async class="speakerdeck-embed" data-id="448751cd3ceb43149100f61912248fc0" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

## 感想

今回、僕は企画とCfP系のとりまとめ、当日は配信担当をさせていただきました。当日の司会進行は土橋さんにおまかせをしてしまったのですが、いつもながら質疑応答の仕切り力は素晴らしい限りだなと思いながら聞いていました。

今回のトピックは、機械学習チームが解散したという衝撃的な話からはじまり、NLPを中心とした機械学習基盤、リアルタイム予測基盤、モバイルやエッジ向けの機械学習など多岐にわたる発表が充実していました。
個人的に特に思ったことは、一言に機械学習基盤といっても組織や規模、フェーズに応じたアーキテクチャが採用されているというように感じました。
これはMobility Technologies大西さんの発表で、Kubeflow Pipelinesを選んだ理由に「ブラウザベースでパラメータを入力できること」ということがありました。

{{< tweet user="chezou" id="1324621428235268096" >}}

当たり前ではありますが、システムの要件は組織の体制やビジネス要件に規定され、それが機械学習基盤でも変わらないということが改めて実感できました。

今後も、MLSE 本番適用のためのインフラと運用WGではこうした機械学習基盤のアーキテクチャやパターンを明確にするために、討論会などの活動を続けて行きたいと思います。
