---
authors: [aki]
categories: [life]
date: '2018-06-18 17:06:01-07:00'
description: この記事は、最近流行りのWork From Sentoで有名なRAKU SPAからお送りしています。
title: 退職します
keywords: [セールスエンジニア, 自分, 仕事, 企業, 外資, コントリビュート, 違い, 日本, エンジニア, 英語]
recommendations: [/post/2016-03-30-zhuan-zhi-simasita/, /post/2017-12-31_2017--------c4901627b12d/,
  /post/2022-01-09-vancouver-engineer-podcast/]
---

この記事は、最近流行りの[Work From Sento](http://blog.nohana.co.jp/article/lets-wfs)で有名な[RAKU SPA](http://rakuspa.com/)からお送りしています。

一部の方にはお伝えしましたが、先週がClouderaでの最終出社でした。2年3ヶ月はあっという間に過ぎて行きました。同僚の [Daisuke Kobayashi](https://medium.com/u/aad6cf2e3329) と [Tatsuo Kawasαki](https://medium.com/u/9fba6aa30d2b) に退職ブログ書いてくださいよと言われたので、初めて書いてみます。


### はじめての外資で働くということ

研究職からWeb系でのソフトウェアエンジニアを経て、いわゆる外資ベンダーでのプリセールスのセールスエンジニアとして今回0からの弱くてニューゲームをさせてもらいました。セールスエンジニアのお仕事は、同僚の [Sho Shimauchi](https://medium.com/u/6dff53967b31) のこの記事がわかりやすいかと思います。

[**セールスエンジニアという仕事 - 科学と非科学の迷宮**  
_現在の自分の肩書である「セールスエンジニア」という仕事がどのようなものか知らない方も多く、毎回説明するのが大変なのでブログ記事にしました。セールスエンジニアという仕事はなかなか馴染みがありませんが、20代後半から30代のITエンジニアの…_shiumachi.hatenablog.com](https://shiumachi.hatenablog.com/entry/2016/06/04/160916 "https://shiumachi.hatenablog.com/entry/2016/06/04/160916")[](https://shiumachi.hatenablog.com/entry/2016/06/04/160916)

ただ、Clouderaのセールスエンジニアのロールは継続的に使っていただくために割となんでもするという感じで裁量も大きく、Field Data Scientistという風に名乗らせていただいて、Spark周りのBig Dataの話とデータ活用の話、それから機械学習の話を幅広くさせていただきました。

おかげさまで、国内外での発表も色々とさせていただきましたが、USのエンジニアブログにも5本ほど執筆させてもらい、[Strata Data Conference Singapore 2017](https://conferences.oreilly.com/strata/strata-sg/public/schedule/detail/62956)での発表や、自社の全エンジニアが集まる社内テックサミットでの発表などかなり自由気ままに活動させていただきました。これも日本の同僚や過去一番働きやすい上司たちのおかげです。

また、[PySparkでNativeコード依存のあるライブラリを使ったUDFをどう展開するかという話](http://blog.cloudera.com/blog/2017/05/create-conda-recipe-to-use-c-extended-python-library-on-pyspark-cluster-with-cloudera-data-science-workbench/)や、[sparklyrのUDFの話](http://blog.cloudera.com/blog/2017/09/how-to-distribute-your-r-code-with-sparklyr-and-cdsw/)なんかもワークアラウンドを見つけたりPR投げたりするという形で業務に関連のあるOSS活動もできたのは良かったです。なので、気づけば社内でも有数のconda職人になっていたかと思います。

もちろん、普通のセールスエンジニアとしての活動もしてました。国内最大級のノード数を持つお客様の、クラスタマイグレーションの支援をしたりもさせていただきました。出来るだけお客様の望む物を噛み砕いてサポートするというように心がけて、多岐にわたって支援させていただくよう努めました。

外資というかアメリカ資本の会社に入ってわかったのは、顔を合わせて一緒に飲んで名前を覚えてもらうことの重要性（Gmailのアイコンで顔を見かけると、MLとかでも助けたくなる）と、その時に興味を持ってもらえるようなコントリビュートを事前に社内で行なっておくことでした。APAC最古参社員のshiumachiや、テックサミットでいつも「お前日本人か、diceはどこにいる？」と聞かれる世界のdiceと共に仕事をしていたときに、自分も会社の中で認知してもらいどんどんコントリビュートしたいと思っていたのですが、それは達成できたと思います。最後の年にはプロダクトのロードマップを議論するProduct road map sessionに、ML系のField代表の一人として議論できたのは貴重な経験をさせてもらったと思っています。

### US企業と日本の企業との違う点・同じ点

US企業との日本の企業との違うところはいろいろ感じましたが、特に以下の3つがありました。

*   英語ができないと死ぬ。が、入社時はしょぼくてもなんとかなる
*   文化の違いから、本物のマイノリティであることを痛感する
*   タイムゾーンの違いが辛い
*   空気読んでくれる人はほぼいないので、成果をとにかく主張する

英語は身内の外資系エンジニアの間で話をしていたのが、とりあえず英検二級くらい入社時にできればなんとかなるのではという話をしていました。英語がある程度できれば、酒を飲んで楽しくテックな話で盛り上がって仲間になれますし、お互いのリージョンでのあるある話でも盛り上がれます。

文化の違いは、以下の過去の記事を読んでもらえばいいと思いますが、とにかく、diversity & inclusion に積極的に取り組んでいても、アメリカ人とその他という当たり前な構図に気づかされることが多かったように思います。日本にいると、日本生まれの日本語話者の男性は当たり前だけどマジョリティで、そういう意味で自分がマイノリティになることはなんだかんだでなかったんだなとハッとしました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2017-07-30_culture-map/" data-iframely-url="//cdn.iframe.ly/BlzCZFO"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

タイムゾーンの違いは、途中から仕事で関わる人にNYCベースの人が増えてからが大変でした。時差13時間はどう頑張ってもお互いがちょっとずつ我慢するしかないので、（自分にとっては）日程調整にも気を使うし面倒だなぁという気持ちでした。とはいえ、結構カジュアルにchatしようぜと言われてHangoutしたりしていたので、JST 21 pmから会議開始とかができればまだ早い方で御の字だなぁと思いながら会話していました。

日本の会社と変わらぬ点としては、以下のようなものがありました。

*   強い人と一緒に働くのは楽しい
*   上司に恵まれると仕事しやすい
*   生存戦略の建て方

自分にとっての生存戦略は今までと変わらず、**（その組織の中で）自分が強いところはどこかというのを見つけてコントリビュートする**ことでした。社内には、HadoopやSpark、Java/Scalaに関しては詳しい人が山のようにいるので、そちらの方面は詳しい人を頼りつつ、PythonとML系の話を掛け算で攻めていくようにしていました。例えば、自分の[英語ブログ](https://blog.chezo.uno/)に [Atsushi Odagiri](https://medium.com/u/8c79ed0955f6)さんの知見を英訳して展開しては社内に共有したのもその一環です。

{{< figure src="0_RRTZy7U2FfIZ7DRu.jpg" title="Photo by [Andhika Soreng](https://unsplash.com/@dhika88?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)" >}}

次は、MLOps系の話に自分で取り組んだり、実際に自分でdeveloperとして手を動かしてプロダクトに貢献したいという思いもあり、セールス寄りの世界から少し離れようと思います。かなりキャッチアップしないと…。とはいえ、頸椎を痛めたこともあり、PCもタブレットもスマホも使うと痛みが走るし、薬のためにアルコールも飲めないので、まずは少し静養しようと思います。

必要な人向けのWish listです。お使いください。 [http://amzn.asia/8eDovxL](http://amzn.asia/8eDovxL)