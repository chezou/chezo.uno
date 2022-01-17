---
title: 2017年を振り返って
description: 昨年に引き続き、振り返っていきます。
date: '2017-12-31T11:27:50+09:00'
categories: []
keywords: [data, cloudera, science, 家庭, オライリー, 仕事, strata, sparklyr, singapore, 機械学習]
authors: [aki]
recommendations: [/post/2018-06-19_goodbye-cloudera/, /post/2019-12-04-R-and-TD/,
  /post/2016-03-30-zhuan-zhi-simasita/]
---

2017年を振り返って

[昨年](https://chezo.uno/post/2016-12-31-2016nian-wozhen-rifan-tute/)に引き続き、振り返っていきます。

2017年は仕事に家庭に激動の一年だった気がします。もはや、年初の方は覚えていない。。。

#### 初めて薄い本を出したらオライリーから商業誌になった

4月の技術書典2でなぜか初めて同人誌を出すことになりました。そこからあれよあれよというママにトントン拍子でオライリーから続けて電子版で出版となり、気づけば紙の書籍も来年1月に出版されることになりました。

{{< amazon asin="4873118255" title="仕事ではじめる機械学習" >}}

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2017-10-20_oreilly-ml-for-business-cf835ff4c128/" data-iframely-url="//cdn.iframe.ly/tf0JDFS"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

きっかけは、pyspaのチャットでお蔵入りした原稿を供養しようぜといって [ところてん](https://medium.com/u/dcded7eecf08) さん [Takashi Nishibayashi](https://medium.com/u/1f02a92f1898) さん両氏と同人誌を書くことにしたのですが、日頃考えていること、話していることが皆様の手元に届けられてよかったです。特に、機械学習に関連する泥臭いエンジニアリングまわりのところは、最近でこそ話題になるようになりましたが、あまり論文にもならず論点にもならなかったのですが、これが一つの議論のたたき台として使えればなぁと思っています。

#### Strata Data Conference Singaporeで発表した

仕事ではじめる機械学習で整理した機械学習システムのアーキテクチャの話をしました。英語で40分のトークだったのですが、ちょっと時間配分をミスったり慣れないGoogle Slideでやったら時間カウントし忘れてたりバタバタしましたが、発表後に捕まえてもらって議論をさせていただき有益でした。

[Train, predict, and serve: How to put your machine learning model into production](https://conferences.oreilly.com/strata/strata-sg/public/schedule/detail/62956)

とはいえ、スクリプト用意して臨んだらフリースタイルで話せる感じにはならなかったので、今度は歩き回りながら話せるようにしたいです。

じつはStrata NYCも行ったのですが、こちらはオライリーが主催するAIカンファレンスが直前にあったためか、ML・DL系が少なかった印象にあります。なので、個人的にはSingaporeの方がML系の話、特にデプロイやプロダクション関係の話が多くて楽しかったです。

#### 会社の英語ブログデビューをした

デビューしたと思ったら、年間4本と想像していた以上に書いていました。中にはRStudioのエンジニアにレビューしていただいたものもあり、色々レビューの大切さを感じています。会社の英語ブログを書くともれなくネイティブチェックを無料でしてもらえて非常に勉強になりました。

[Analyzing US flight data on Amazon S3 with sparklyr and Apache Spark 2.0 - Cloudera Engineering Blog](http://blog.cloudera.com/blog/2017/02/analyzing-us-flight-data-on-amazon-s3-with-sparklyr-and-apache-spark-2-0/)

[Use your favorite Python library on PySpark cluster with Cloudera Data Science Workbench](http://blog.cloudera.com/blog/2017/04/use-your-favorite-python-library-on-pyspark-cluster-with-cloudera-data-science-workbench/)

[Create conda recipe to use C extended Python library on PySpark cluster with Cloudera Data Science…](http://blog.cloudera.com/blog/2017/05/create-conda-recipe-to-use-c-extended-python-library-on-pyspark-cluster-with-cloudera-data-science-workbench/)

[How to Distribute your R code with sparklyr and Cloudera Data Science Workbench](http://blog.cloudera.com/blog/2017/09/how-to-distribute-your-r-code-with-sparklyr-and-cdsw/)

#### スターが100超えたOSSができた

PDF中のテーブルからPythonのDataFrameを抽出する[tabula-py](https://github.com/chezou/tabula-py)がスター100を超えました。また、v1.0も出すことができて安定稼働したかなと思います。おかげさまで、英語や中国語での紹介記事も書いていただきありがたい限りです。

なお、継続のコツとしては、限られたリソースなので質問系はStackOverflowに流すようにイシューテンプレートを作ること、基礎的な質問はFAQに詰んでテンプレートに従わないイシューはガンガンクローズする運用にしました。

また、sparklyrにした小さいコントリビュートが含まれたものがリリースされたりと、当初思っていたよりはOSS活動できたかな、と思います。

#### 家庭周りの話

相変わらず出張は多いので、妻の負荷をできる限り抑えるようにしたり気晴らしに出かけたりということを心がけてしました。家族旅行は地味に大事なんだなとおもいます。総じてある程度はできたけど、もうちょいやりようがあるのかなと思います。複数の家族が集まってワイワイやるのはとても楽なのでそういう手抜きの機会を増やしたいなぁ。

また、はじめてのワンオペ育児は自分にとってはいい経験となりました。自分がしんがりを務める体験はするとしないとで全然重みが違いますね。

#### 2018年に向けて

家庭と仕事、そして健康を手に入れるための運動のバランスをうまく取りたいなと思います。

特に今年は仕事ではCloudera Data Science Workbenchという新プロダクトが出たこともあり、そちらの支援を全力でしてきました。合わせて社内外の機械学習系の導入に向けて教育やコンサル的な振る舞いをする機会が増えて、Data democratizationをしていくってこういうことだよなぁと思いなかなか楽しかったです。

[Cloudera Data Science Workbenchクイックスタート](https://blog.cloudera.co.jp/getting-started-with-cloudera-data-science-workbench-2329d94221c5)

Cloudera Data Science Workbenchは、k8sとDockerをベースとしたMLやDSの基盤として非常に便利で、コラボレーションのためのツールです。GPUもコンテナに紐付いて起動できるので、sandboxとしても非常に使い勝手が良いです。端的にいうと、Jupyterをgitとかで連携しやすくしたいい感じのものです。

後半は家庭のこともあり、割と一年全力疾走して来た気がするので、来年はもう少しバランスを取りつつ健康を高めていきたいと思います。筋トレとプロテインはちょいちょいと続けているのですが、腰が辛いのでジムに通うなどして運動を行っていけたらと思います。

英語に関しては、相変わらずDMM英会話でほぼ毎日続けています。多少壁を感じて来たのでなんとかしたいところです。

資産運用もそろそろ始めたいと思います。まずはiDeCoからやろう。

### Appendix

最近会社のslideshareアカウントにスライド置くことが多いので、昨年の発表リストを貼ります。

- Big Data Analytics Tokyo
- Data Engineering and Data Analysis Workshop #1
- 人工知能学会 SIG-SWO研究会 42回
- [SIG-SWO-042-InvitedTalk-Ariga](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxzaWdzd28xNXxneDo2ODNmOTg4M2NhMjM4NjI)
- Cloudera World Tokyo 2017
- Strata Data Conference Singapore 2017
