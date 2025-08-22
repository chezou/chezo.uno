---
authors: [aki]
categories: [conference]
date: '2018-05-16 22:03:57-07:00'
description: タイトル通り日本ソフトウェア科学会の研究会、機械学習工学研究会キックオフシンポジウムに登壇しました。@bonotake さんから声をかけられた時はカジュアルに受けたのですが、蓋を開けてみれば大御所の方々ばかりで恐縮しながらの発表でした。
title: 機械学習工学研究会キックオフシンポジウムに登壇しました
keywords: [機械学習, システム, データ, 人工知能, ai, スキーマ, tfx, systems, 予測, ポイント還元]
recommendations: [/post/2017-10-20_oreilly-ml-for-business-cf835ff4c128/, /post/2014-08-29-detafen-xi-henoxiang-kihe-ifang-machine-learning-casual-talks-number-2wokai-cui-simasita-number-mlct/,
  /post/2019-12-05-ibis2019-mlse/]
---

タイトル通り日本ソフトウェア科学会の研究会、[機械学習工学研究会キックオフシンポジウム](https://sig-mlse.wixsite.com/kickoff)に登壇しました。[@bonotake](https://twitter.com/bonotake) さんから声をかけられた時はカジュアルに受けたのですが、蓋を開けてみれば大御所の方々ばかりで恐縮しながらの発表でした。

僕の発表内容としては、書籍「仕事ではじめる機械学習」の話からデプロイパターンの話と、機械学習特有の難しさはどこから来るのかという話をしました。

[**仕事ではじめる機械学習**  
_Amazonで有賀 康顕, 中山 心太, 西林 孝の仕事ではじめる機械学習。アマゾンならポイント還元本が多数。有賀 康顕, 中山 心太, 西林…_amzn.to](https://amzn.to/2GpxzEY "https://amzn.to/2GpxzEY")[](https://amzn.to/2GpxzEY)

時間が20分だというのに資料を一通り作った後に気づいて、かなり表層的にさらっとしか話をしませんでしたが、詳しい方からすると当たり前の話しかできませんでした。

#### 話しきれなかったこと

お気づきの方は、参考文献等を見てわかるかと思いますが、機械学習特有の難しさという話は、主に以下の3つからピックアップしてきた話になります。

[**Hidden Technical Debt in Machine Learning Systems**  
_Eletronic Proceedings of Neural Information Processing Systems_papers.nips.cc](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems")[](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems)

[**TFX: A TensorFlow-Based Production-Scale Machine Learning Platform - Google AI**  
_We present TensorFlow Extended (TFX), a TensorFlow-based general-purpose machine learning platform implemented at…_ai.google](https://ai.google/research/pubs/pub46484 "https://ai.google/research/pubs/pub46484")[](https://ai.google/research/pubs/pub46484)

[**_My model has higher BLEU, can I ship it?_**  
My model has higher BLEU, can I ship it?www.lucypark.kr](https://www.lucypark.kr/docs/2017-acml/#/ "https://www.lucypark.kr/docs/2017-acml/#/")[](https://www.lucypark.kr/docs/2017-acml/#/)

個人的には、どれも語り尽くされた感があるところはあったのですが、特にTFXの論文がプラットフォームの話だけではなく、典型的な機械学習の問題をどのようにシステムとして回避しているかという話が詰まっていて良かったので改めて補足したいと思います。。

例えば、「入力データのスキーマを作ってチェックする」という話が書いてあるのですが、ここでいうスキーマとは、カテゴリ値の種類を列挙したり、期待される統計値の幅を予め記述しておくというJSONSchema的なspecに近いものです。特に学習時のデータの分布と予測時の分布が極端に異なるということは往々にしてあるのですが、それをデータのスキーマでvalidationすることでアラートを上げてコントロールするというのは目からうろこでした。

また、予測結果を他部門の人が使うエピソードがあるのですが、その中で「締切に追われるエンジニアは、サクッと使えるものは使ってしまうものである」みたいなことが書いてあって、ですよねーと一人頷いていました。

3つ目のLucy Parkさんの発表資料は、Joel test for better Machine learning systemsというサブタイトルの通り、何をクリアすればいいかできていないとまずいかという11の質問項目を提案しています。

> Do you keep your data versioned as well as your code?

> Do you have an experiment database?

> Do you have specified evaluation metrics?

> Do the evaluation datasets match the needs of your users?

> Can you reproduce your experiments in one step?

> Do you have up-to-date documents?

> Do you have the best computational resources money can buy?

> Do you have tools to test model training?

> Do you have tools to interpret your models?

> Can you easily replace a component of your algorithm?

> Does your team have a clear vision?

詳細はスライドを見ていただければと思うが、この中でデータのバージョン管理をしてる？という話が出ていたが、これはまだベストプラクティスがないよねという話がスライドでもされています。

少量データであれば、なんとでもなるのだが規模が大きくなってきて、かつ変更が入るようなデータをどう保持するのかというのは、自分でも気になって社内で議論したことがあるのですが、いわゆるDWHに入っているようなデータは、[BiTemporal modeling](https://en.wikipedia.org/wiki/Bitemporal_Modeling) (日本語だと[こちらの記事](http://matsu-chara.hatenablog.com/entry/2017/04/01/110000)がわかりやすい)という方法を使えば逐一スナップショットをとるのではなく、変更を管理できるという方法を教えてもらいました。

一方で、[DVC](https://blog.dataversioncontrol.com/data-version-control-tutorial-9146715eda46)のようにgit likeにデータのバージョンを管理する方法というのも提案されていて、バイナリのデータはこちらのほうが良さそうだと思っています。

機械学習の予測では、一度異常が起きた時の原因究明が難しく、問題の切り分けのためにソースコードを遡るだけでなく、学習データ自身やモデル自身を遡る必要があるためここの話は非常に実用上重要になってくると思います。

あとは、バージョン管理をするのと同時に、依存関係を記述するモデルのリネージが重要になってくるだろう話もしました。モデルのリネージの話はまだこれといったツールがあるわけではないのですが、予測結果を利用してさらに別のプロダクトを作るというケースがあるように、何がどの結果をつかっているのかというのを可視化できるツールというのが、今後機械学習に依存したプロダクトが増えるに連れて重要度を増すでしょう。

#### 機械学習システムにどういう立場で関わるか？

パネルディスカッションなどを通じて感じていたのは、機械学習システムを作る人が誰でどう関わるのかというのが人によって大きく異なるというのを改めて感じました。

いわゆるコンサルやSIとして係る場合、発注者と受注者の関係が発生します。この場合、要件定義を先にして…のようにウォーターフォールで客が作りたがるという話が出ていましたし、ソフトウェア工学的にもそうした立場に立った意見が目立ったのかなと思います。

そこに関しては、発注者自身が受け入れ要件を理解して定義できないといけないよね、などという話も出ましたが、幸いにして日本語だと機械学習システムのプロジェクトの進め方関連の書籍が拙著以外にも出ているので、そういった立場の方々はぜひ一度読むとよいのではないでしょうか。

[**人工知能システムを外注する前に読む本~ディープラーニングビジネスのすべて~**  
_Amazonで坂本 俊之の人工知能システムを外注する前に読む本~ディープラーニングビジネスのすべて~。アマゾンならポイント還元本が多数。坂本…_amzn.to](https://amzn.to/2IqEH9M "https://amzn.to/2IqEH9M")[](https://amzn.to/2IqEH9M)

[**人工知能システムのプロジェクトがわかる本 企画・開発から運用・保守まで (AI & TECHNOLOGY)**  
_Amazonで本橋 洋介の人工知能システムのプロジェクトがわかる本 企画・開発から運用・保守まで (AI & TECHNOLOGY)。アマゾンならポイント還元本が多数。本橋…_amzn.to](https://amzn.to/2Ktuciw "https://amzn.to/2Ktuciw")[](https://amzn.to/2Ktuciw)

個人的には、データドリブンなプロダクトを作るという観点では、ドメイン知識を持っている人が一番強いと思っており、最初はがっつり機械学習のシステム構築を支援するけれど、段々と発注側の人を育てる方向にシフトをしていき、最終的には内製化できるのが理想的ではないかと考えています。

機械学習が詳しい人の強みとしては、「どういう問題の切り出し方をしたら、機械学習で解けるか」というところだと思っています。この問題定義は、なかなか場数を踏まないとできるようになるのは難しく、そこをお手伝いすることが僕自身も多いです。それ以外のどう手を動かすかといった知見を少しずつトランスファーしていくのが、継続的に改善を必要とする機械学習システムでは良い形なのではないかと思います。

思った以上にCI,CDの話が出てこなくて、「ん？」と思っていたのですが、改善をし続けるという話が自社内でやれるかどうかでスピード感も変わってくるのかなという観点を得ることができました。

最後になりますが、司会の丸山先生や登壇者の皆様、500人規模の大規模な運営をしていただいたスタッフの皆様ありがとうございます。交流会でも非常に濃密な議論が出来てとても楽しかったです。