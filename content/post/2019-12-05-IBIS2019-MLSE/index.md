---
title: IBIS 2019の機械学習工学企画セッションに登壇しました
subtitle: ''
summary: ML in productionの課題について話しました
authors: [aki]
tags: [mlops]
categories: [Machine Learning, MLOps, conference]
date: 2019-12-05 00:24:00+09:00
lastmod: 2019-12-05 00:24:00+09:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [工学, 先生, 表現, shima, 機械学習, shift, スライド, 学習, effect, '2019']
recommendations: [/post/2018-05-17_MLSE-kickoff/, /post/2020-07-11-MLSE-summer-workshop/,
  /post/2014-08-29-detafen-xi-henoxiang-kihe-ifang-machine-learning-casual-talks-number-2wokai-cui-simasita-number-mlct/]
---


この記事は、[機械学習工学アドベントカレンダー2019](https://qiita.com/advent-calendar/2019/mlse)の5日目です。

こんにちは、chezouです。先日、PFNの比戸さんにお声がけいただきIBIS 2019という日本で最大の理論系機械学習のワークショップで、[3日目の「機械学習工学」の企画セッション](http://ibisml.org/ibis2019/%e4%b8%89%e6%97%a5%e7%9b%ae%ef%bc%9a%e3%83%97%e3%83%ad%e3%82%b0%e3%83%a9%e3%83%a0%e8%a9%b3%e7%b4%b0/)に「継続的改善をし続けるための機械学習基盤の課題」というタイトルで発表しました。理論系のワークショップというのは知っておりアウェイ感半端なく、[数式もないという煽り](https://repose.hatenadiary.jp/entry/2019/11/27/083823)も受けましたが、なんとか実務者の皆様に届いてくれたのではないかと思っています。

[Challenges for Machine Learning Systems toward Continuous Improvement](https://docs.google.com/presentation/d/1T8JF6h_DFnBAWz8LJvK0miFWsVovKyP0BDuXk3cVo2Q/edit?usp=drivesdk)

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTbIOwmdWnnQWVkoMm0a5z6dg0UGCmuvDHGztsl_6krNn2gh-IOFl7Lo4-D_fFqzlyL-RtqemHolupn/embed?start=false&loop=false&delayms=3000" frameborder="0" width="720" height="434" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

Machine Learning in productionに対する9つの課題は、世の中にまだまだ整理されているものではなく難産だったので色々と議論ができればと思っています。9つの課題とdotscienceのLuke Marsden氏によるReproducible, Accountable, Collaborative, Continuousという[4つのマニフェストの話](https://docs.google.com/presentation/d/17RWqPH8nIpwG-jID_UeZBCaQKoz4LVk1MLULrZdyNCs/edit#slide=id.g6ad50e93e5_0_59)を元に整理してみたのですが、どのような課題と抽象化を行っているのか、そしてそれがどういう嬉しさがあるのかへの理解の一助となればと思います。

## Concept drift?

「学習時と予測時の分布の違いを検出するデータバリデーションが大事」という話をしました。で、この「学習時と予測時の分布の違い」というのを"Concept drift"という表現を使って説明をしたのですが、 shima__shima先生からもご指摘をいただき、どうも違うのではないかということで色々と調べたり議論をしていました。Concept driftは英語圏では雑に[このニュアンスを表現するのに使われており](https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/)、特に産業界ではそれでいいかなという表現であるという認識です。ただ、もともとはストリームデータに対するdriftという定義があるようです。

人によっては"Covariate shift"(共変量シフト)や"Domain shift"という表現をするということから、Covariate Shiftがいいのかなと思っていましたが、"Delayed effect"という表現が時間的な変化に対する表現としてよいようです。ただ、個人的にはスライドでも書いたように光の変化は時間変化というよりは仮定する前提条件が覆された例だと思っているため、Delayed effectも少し狭いかなと思っていました。

なお、GoogleはTensorFlow Extendedの論文中で"training-serving skew"という表現を使っています。

以下、shima__shima先生の説明が参考になるかと思います。

{{< tweet user="shima__shima" id="1201801576949538816" >}}

{{< tweet user="shima__shima" id="1201802162482737152" >}}

## 機械学習工学セッションの他の発表

他の発表は、NIIの石川先生による機械学習工学とテストの話 ([スライド](http://ibisml.org/ibis2019/files/2019/12/slide_ishikawa.pdf))、STORIA法律事務所の柿沼先生の機械学習と知財の話([スライド](http://ibisml.org/ibis2019/files/2019/12/slide_kakinuma.pdf))でした。

石川先生の機械学習を工学として捉え直したときの説明や、adversarial testなどテストの最近の状況は自分自身追いかけられていなかったのでとても良かったです。

柿沼先生はAI模擬裁判などでご存知の方も多いと思いますが、先生の知財の話は学習済みモデル含めたシステムの権利は受託したベンダーか発注者のどちらにあるのか、という話も面白く、実践的で知見に富んだ話でした。ぜひML関係者はスライドを読むと良いと思います。また、柿沼先生への比戸さんの質疑から派生した議論をメールでさせていただいたのですが、機会があったら公開したいと思っています。
