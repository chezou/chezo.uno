---
title: OSSベースの機械学習が強い理由
description: 英語版はこちら。
date: '2017-08-03T03:29:59+09:00'
categories: [machine_learaning, OSS]
keywords: [論文, 機械学習, アルゴリズム, 時代, 実装, アカデミア, deep learning, 投稿, 先端, フレームワーク]
authors: [aki]
recommendations: [/post/2017-05-26_public-dataset/, /post/2014-08-29-detafen-xi-henoxiang-kihe-ifang-machine-learning-casual-talks-number-2wokai-cui-simasita-number-mlct/,
  /post/2017-10-20_OReilly-ml-for-business-cf835ff4c128/]
---

_英語版は_[_こちら_](https://chezo.uno/blog/2017-08-03_why-oss-based-machine-learning-is-good-3ab45a1a5e52/)_

TensorFlowの登場以降、OSSベースの機械学習の盛り上がりは加速しています。Kerasの作者の[François Chollet](https://twitter.com/fchollet)さんの言葉が、この状況を非常に端的に表しています。これだけでも十分だとは思いますが、この記事では、なぜオープンソースの機械学習が強いのか、最近のどういった流れがあるのかを整理したいと思います。

### tl;dr

*   機械学習やDeep Learningのフレームワークが充実してきた
*   論文が査読前に公開され、他社も簡単にアルゴリズムの検証ができるようになった
*   多くのプレーヤーの参戦により、アカデミアでの機械学習の研究がレッドオーシャン化した
*   他社にないアルゴリズムで一発勝負、実装は秘密、というアプローチが厳しい

### 牧歌的な時代

5年前10年前の世界では、先端の機械学習に取り組んでいるのは大学などの研究室、大企業の研究所や一部の先進的な企業がほとんどでした。特に、ラベル付きのデータ量は現在よりも少なく、アルゴリズムを突き詰めて性能を向上させたり、特徴量エンジニアリングを頑張って性能を改善したりしていました。

この時代の先端の機械学習は、特に大学を中心としたアカデミアの人たちが国際会議に投稿をし、それが査読を通ったものが共有されるという形でした。実装が共有されることは今ほど多くはなく、各研究者は先行研究をスクラッチから再実装するということが多かったように思います。早くて半年、場合によっては1年以上のサイクルで新しいアルゴリズムがでてくるという時代でした。

オープンソースの機械学習ライブラリ/フレームワークとしては、古くはWekaのような機械学習用のライブラリを使う人もいれば、scikit-learnも[2010年にリリース](https://en.wikipedia.org/wiki/Scikit-learn)されましたが、今ほど多くのソフトウェアエンジニアの間ではメジャーではなかったように思います。どちらかというとlibsvmやliblinearなど単一/少数のアルゴリズムのものが多く使われていた時代でした。

### 変化の激しい時代

2017年の現在では、機械学習に取り組む人は10年前に比べれば圧倒的に増えたのはみなさんもご存知のとおりだと思います。アカデミアが中心だった時代から、データを持つ企業の人達にも広がってきました。特に、機械学習に取り組んだことのないソフトウェアエンジニアにも身近な存在になったと感じています。私の主催しているkawasaki.rbでも今まで業務で機械学習に取り組んだことのない人が、Deep Learningに取り組み始めたという話を聞いて驚きました。この背景には、やはり企業が機械学習に使えるデータを貯めることが一般的になったこと、そして優れた機械学習フレームワークが増えたこと、GPUによるDeep Learningの効率的な計算が可能となったことなどが挙げられます。

TensorFlow, Chainer, MXNet, Caffe2, PyTorchなどの数々のDeep Learningのフレームワークだけでなく、XGBoost, Lightgbmなどkaggleで流行って使われるようになったオープンソースのライブラリも多いです。当然、scikit-learnも複数のアルゴリズムを試すフレームワークとして当然使えるものになっています。

### オープンな論文の盛り上がり

こうしたは流れを支えているのは、一つは機械学習のコンペティションサイトの[kaggle](https://www.kaggle.com/)と、もう一つは[arxiv](https://arxiv.org/)と呼ばれるオープンな論文を投稿する場所の存在があります。（arxivは査読プロセスが入っていないため質が担保されておらず、それを論文と呼んでいいのか、などの議論はありますが、ここでは論文スタイルのドキュメントをざっくり論文と呼びます）

以下の記事に、arxivに投稿された機械学習関連（特にDeep Learning）の論文投稿数について記述があります。こちらの記事によれば、機械学習関連の論文の投稿数が、2017年には5年前に比べて4倍以上になっているという指摘がされています。

<script async src="https://static.medium.com/embed.js"></script><a class="m-story" href="https://karpathy.medium.com/a-peek-at-trends-in-machine-learning-ab8a1085a106">A Peek at Trends in Machine Learning</a>

arxivの論文は、（査読がないこともあり）日々新しい論文が投稿されます。つまり、Google、Facebook、Microsoftなどの先端の取り組みが、査読前にどんどん論文として公開されています。これは、特に1年や半年単位で目標を設定して取り組むような従来型の大企業の中央研究所にとっては、機械学習の先端のアルゴリズム自体を研究開発するのはかなりのチャレンジになってきていると感じています。これについては「ただ部品を足しているだけ」という批判もありますが、牧歌的な時代のスピード感から目まぐるしく変わってきているのは明らかです。

最近では、日夜新しいarxivの論文を読み漁る人のために、新着論文をより良くチェックするための[ariXiv Times](https://arxivtimes.herokuapp.com/)という取り組みもされています。

<script async src="https://static.medium.com/embed.js"></script><a class="m-story" href="https://medium.com/@arxivtimes/arxivtimes%E3%81%AE%E3%83%80%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%BC%E3%83%89%E3%82%92%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%81%97%E3%81%BE%E3%81%97%E3%81%9F-4f2f7190b7e8">arXivTimesのダッシュボードをリリースしました</a>

### オープンな論文が加速するオープンソースの機械学習

今年の3月にDeep Forestという論文がarxivで公開され、”Deep Learningよりも性能が良い”という主張もあって話題になりました。日本でもQiitaに訳が公開されるなど話題になったので記憶に残っている人もいるかと思います。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://arxiv.org/abs/1702.08835v4" data-iframely-url="//cdn.iframe.ly/kjxpnMP"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

実はこの論文で提案された手法は、論文が出た日（2017/2/28）の約一週間後（2017/3/5）にはR実装がでてきて、その後Python実装も出てきました。このやり取りは、以下のLightGBMのissueでなされ、論文の再現性がないのではないか（謳われているような性能が出なかった）という話になりました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/microsoft/LightGBM/issues/331" data-iframely-url="//cdn.iframe.ly/bve0cNQ?card=small"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

arxivで公開された論文のOSS実装が1週間後には実装が出てきてコミュニティの議論が始まる、というスピードの時代になっている象徴的な出来事です。

また、会議によっては論文投稿時に実装を公開することが求められる国際会議も増えてきていると聞きます。

### 雑感

機械学習のアルゴリズム自体を考えることは非常に重要な仕事です。そして、オープンな論文、コンペティション、そしてOSS化されるという流れの加速、そこから得られた新しい知見を素早くビジネスへ適用するのがとても速くできる時代になりました。

個人的には、アルゴリズムそのものよりも、それをビジネスに活かすにはどうすればいいか、というところにフォーカスすることのほうが楽しい時代になってきたのでは、とも思います。

この状況を翻って言うと、「自社だけができる特別な機械学習のアルゴリズム」というのを押し出していくのはうまくいかない時代に入ったともいえます。（もちろん、アカデミアの人たちはデータを用意できればこうした最先端の取り組みを今後も推し進めていくでしょうが）企業1社で、Google、Facebook、Microsoftなど世界の多くの最先端の人たちよりも素晴らしいアルゴリズムが素早く出せる理由は何でしょうか？それが、オープンソースベースの機械学習の強い理由でしょう。

アカデミアでは昔から「[巨人の肩に乗る](https://ja.wikipedia.org/wiki/%E5%B7%A8%E4%BA%BA%E3%81%AE%E8%82%A9%E3%81%AE%E4%B8%8A)」という言葉が知られていますが、先行研究という巨人に乗って次に進むということを示しています。オープンソースベースの機械学習でも、「巨人の肩に乗る」ということが顕著になってきています。
