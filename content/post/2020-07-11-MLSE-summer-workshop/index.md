---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "機械学習工学研究会（MLSE）の夏合宿 2020で本番適用のためのインフラと運用に関する討論会を開催しました"
subtitle: ""
summary: ""
authors: [aki]
tags: [mlops]
categories: ["Machine Learning", MLOps, conference]
date: 2020-07-11T18:00:00+09:00
lastmod: 2020-07-11T18:00:00+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false
---

[@masaru_dobashi](https://twitter.com/masaru_dobashi)さんとMLSEの夏合宿で、本番適用のためのインフラと運用WGの討論会を開催しました。
WGのモチベーションは[MLSEのサイト](https://sites.google.com/view/sig-mlse/wg#h.p_Of4vDn0AZIz-)をご確認ください。

MLSEの夏合宿自体の概要は、[@ysk_moto](https://twitter.com/ysk_moto)さんがまとめてくださった記事がわかりやすいと思います。Discordを中心に130名を超える参加者がオンラインで様々な議論をするというスタイルでした。

[機械学習工学研究会（MLSE）夏合宿　2020に参加しました](https://note.com/ysk_moto/n/n8995227204e1)

実は我々のWGの討論会自体は第一回はオフラインで開催しました。そちらの[まとめはGitHubにあります](https://github.com/mlse-jssst/InfraOpWGProceedings/blob/master/20200210_DiscussionWorkflow/ProceedingOfDiscussionAboutWorkflow.md)。よければ御覧ください。


今回の討論会のまとめは、以下の2つのトピックについて議論をしました。

1. 機械学習における監視・観測とアーキテクチャ例
2. 責任分解とシステム

もう少ししたらGitHubのレポジトリにまとめを上げる予定ですが、その中から興味深かった話題を紹介したいと思います。

## COVID-19の影響は予測モデルを更新し続けることである程度抑制できた

これは、PFNの丸山さんが話題に出してくれたのですが、deeplearning.aiのnewsである[The Batch](https://blog.deeplearning.ai/blog/the-batch-covid-19-infects-ai-learning-from-small-data-generated-music-goes-mainstream-fighting-pandemic-disinformation)や[この記事](https://www.theregister.com/2020/06/23/covid19_pandemic_means_data_from/)でも言及されていた、「COVID-19によって人間の行動が変わってしまって予測に対する影響は出なかったのか？」という問いが投げかけられました。その中で、ある広告系の企業の参加者が、「入力データもモデルも毎日更新しているので、現状は対応できていると考えている。毎日モデルを更新するのが大切」という知見を共有してくれました。

もちろん、劇的に前提条件が変化をする問題ではなかなかそのままのロジックや特徴量が使えないということもありうるとは思いますが、モデルを継続的に学習しつづけることで、変化に追従するというのは長期間機械学習システムを運用していく上でなくてはならないのだと改めて思いました。


## 学習したモデルは、組織のありかたで渡し方はおろか渡せるものも変わる

予測モデルを誰が学習するのか、という話題のなかで、小さなチームでは学習も予測も一人でやるという状況が出たのに対して、日本の大企業では特に[研究開発の会計的な事情](http://hyodo-ao.net/difference)で、研究所で学習したモデルや学習をするためのコードを渡せず仕様書のようなドキュメントで開発部門に渡すしかない、という話が出ました。言われてみればそういうケースもありうるのかと思いつつ、部門の切れ目でAPIを用意するという立て付けも取れるかもしれませんが、研究所で学習や予測APIを提供するといった体力があるところも限られてくるとは思うので、日本の会計や税務的に難しさが発生するのかと、ハッとした瞬間でした。

## モデルのリネージは決めてとなるOSSがない

これは討論会で出た話では有りませんが、実験管理は徐々にOSSで出てきているが、モデルの作成に至るまでのリネージはOSSとしては決定版がないよね、という話が何度か出てきました。もうシャットダウンしてしまったDotscienceではこうした[リネージを可視化する機能](https://docs.dotscience.com/tutorials/provenance/)を持っていましたが、まだOSSでは良いものは私の知る限りではないように思います。
こうしたこともあり、サイバーエージェントではモデルのリネージを管理するためのツールを内製で開発しているそうです。OSSとしてカバーするのは難しいかもしれませんが、各社が自社のサービスの上でのソリューションを提供してくるかもしれません。

## 夏合宿全体を通じた感想

Discordを通じた議論や発表はとても体験としてよかったと思います。特に、人工知能学会のポスターで苦痛だったExcelで書かれPDFで出力されたパスワード付きZoomのリンクをクリックして移動するという地獄の体験をしたあとでは、Go Liveでどういう発表をしているのかもプレビューで覗けますし、軽量な音声だけで議論も進むので活発な議論ができていたのではないかと思います。

ただ、会社のポリシーでP2Pのプロトコルを使っているDiscordのアプリは使えず、会社のMBPでは非力だったためか画面共有の表示が安定してされなかったのは難しいところではありました。GPUマシンでは安定しているので、MBPでは少し厳しいですね。

我々の討論会ではZoomを使って議論をしたのですが、Muralと呼ばれるMiroのようなオンラインホワイトボードも使っていたので、複数のグループに分かれて付箋を貼っていくスタイルでも良かったかもしれません。

ただ、ご多分に漏れずDiscordの参加人数が10人を超えてくると、議論が一本にしかならない関係もあり並列して話をするのは難しい印象でした。

## 最後に

9月頃にWGとして、各社で携わった機械学習基盤の知見共有をするためのオンラインカンファレンスを実施予定です。もう少ししたら、公募を開始しようと思いますので、機械学習システムを構築している話や、構築しようとしたけどうまく行かないといった話をシングルトラックのセッションとして発表していただければと思います。