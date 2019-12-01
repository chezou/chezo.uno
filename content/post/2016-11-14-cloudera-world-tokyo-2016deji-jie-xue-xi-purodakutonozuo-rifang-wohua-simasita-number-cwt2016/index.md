---
title: "Cloudera World Tokyo 2016で機械学習プロダクトの作り方を話しました #cwt2016"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2016-11-14T23:05:21+00:00
lastmod: 2016-11-14T23:05:21+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
さる11/8に、自社の主催する[Cloudera World Tokyo 2016](http://www.clouderaworldtokyo.com/)で、機械学習プロダクトの作り方について話をしました。

&lt;figure id=&quot;talkshow&quot;&gt;
&lt;span itemscope itemtype=&quot;http://schema.org/Photograph&quot;&gt;&lt;img src=&quot;https://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20161108/20161108182005.jpg&quot; alt=&quot;f:id:chezou:20161108182005j:plain&quot; title=&quot;f:id:chezou:20161108182005j:plain&quot; class=&quot;hatena-fotolife&quot; itemprop=&quot;image&quot;&gt;&lt;/span&gt;
&lt;figcaption&gt;図: Hadoopの生みの親 Doug(&lt;a href=&quot;https://twitter.com/cutting&quot;&gt;@cutting&lt;/a&gt;)と握力王新沼さん(&lt;a href=&quot;https://twitter.com/hiroki_niinuma&quot;&gt;@hiroki_niinuma&lt;/a&gt;)の対談イベントの様子&lt;/figcaption&gt;
&lt;/figure&gt;

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/B8ylsXGU1Awlts&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[大規模データに対するデータサイエンスの進め方 #CWT2016](https://www.slideshare.net/Cloudera_jp/data-science-toward-big-data-cwt2016 &quot;大規模データに対するデータサイエンスの進め方 #CWT2016&quot;)** from **[Cloudera Japan](http://www.slideshare.net/Cloudera_jp)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/Cloudera_jp/data-science-toward-big-data-cwt2016&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

データの民主化の話、データサイエンティストとデータエンジニアの役割分担とチーム構成、機械学習の業務フロー、Cloud Nativeなデータサイエンスといった盛りだくさんの話をしました\*1。

話の中で特に言いたかったことは2つ、P.16のリスクを取ってくれる責任者を捕まえようという話と、P.29の機械学習込みのプロダクトは改善をし続けないと死ぬという話です。 あとは、できるだけ機械学習をしないで、サンクコストが生まれる開始前に撤退ラインを決めておこうということも言いました。

個人的には、今回 Cloudera のエンジニアリングチームと共に[プロダクトの品質を測定](http://www.clouderaworldtokyo.com/session-download/B2-Measuring%20Software%20Quality-%20v2.pdf)しているJuliet([@j\_houg](https://twitter.com/j_houg))の話や、[@tokoroten](https://twitter.com/tokoroten)さんの話も、自分からお願いをしたのですがお互い相補的な話でとても良かったと思います。

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/ypsEOVchFn6g4u&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[データ分析グループの組織編制とその課題 マーケティングにおけるKPI設計の失敗例 ABテストの活用と、機械学習の導入 #CWT2016](https://www.slideshare.net/TokorotenNakayama/kpi-ab-cwt2016 &quot;データ分析グループの組織編制とその課題 マーケティングにおけるKPI設計の失敗例 ABテストの活用と、機械学習の導入 #CWT2016&quot;)** from **[Shinta Nakayama](http://www.slideshare.net/TokorotenNakayama)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/TokorotenNakayama/kpi-ab-cwt2016&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

特にtokorotenさんの話は、データ分析チームのアンチパターンが並んでいます。どれも耳が痛い話です。また、A/Bテストから機械学習にアップリフトモデリングを通じてどうつなげていくかという話もとても面白いです。

3人の話を総合すると、データサイエンティストとデータエンジニアという区分では、こういった人たちが求められているのかなと思っています。

- ビジネスの意思決定をデータから支援する人
- プロダクトの改善を予測モデル含めてデータドリブンで行う人
- データ基盤を作るデータエンジニア

### Cloud Native な話

Cloud Nativeのデータサイエンスの話は、時間の関係でちょっと話足りなかったのですが、同僚の[@tsuyokb](https://twitter.com/tsuyokb)の話を見ていただけると良いと思います。

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/cnkUJMqWQx34c2&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[Cloud Native Hadoop #cwt2016](https://www.slideshare.net/Cloudera_jp/cloud-native-hadoop &quot;Cloud Native Hadoop #cwt2016&quot;)** from **[Cloudera Japan](http://www.slideshare.net/Cloudera_jp)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/Cloudera_jp/cloud-native-hadoop&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

機械学習やデータ分析の文脈で言うと、今までImpalaとかHive on SparkとかはHadoopクラスタを持っている人の持ち物というイメージしかなかったんですが、昨今S3を始めとしたオブジェクトストレージに置かれたデータを直接処理できるようになったのが大きな変化だと思っています。

特に、HiveやImpalaのテーブルさえ作っておけば、S3に直接SQLを投げられるようになったというのは大きな変化かなと思います。[Cloudera Director](http://www.cloudera.com/downloads/director/2-2-0.html)を使うと、一時的なクラスタを上げ下げ増減が簡単にできて、永続化層をS3にするだけという感じになります。 そうすることで、必要なときに必要な量のクラスタを立ち上げて対話的に分析をし、ワークロード決まったらバッチ用に組み替える、なんてことも容易になってきます。

少しずつではありますが、RedshiftやBigQueryに対する第3の選択肢になってくることを期待しています。

\*1:思い返してみると、この手のあるある...辛い...って話MLCTでよくやっていたのであった


