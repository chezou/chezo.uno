---
title: '「夏真っ盛り！Spark + Python + Data Science祭り」を開催しました＆Ibisを紹介しました #summerDS'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2016-07-26 17:27:38+00:00
lastmod: 2016-07-26 17:27:38+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [レコメンド, ibis, spark, pandas, ラボ, エンジン, チューニング, sql, dmm, .com]
recommendations: [/post/2016-07-12-jupyterkaraspark-clusterwocao-zuo-dekirulivy-plus-sparkmagicwoshi-sitemita/,
  /post/2015-10-12-pyconjp-2015nican-jia-sita-number-pyconjp/, /post/2016-05-05-detawo-ge-suo-niji-merukotodedetahuo-yong-nomin-zhu-hua-gajin-ndahua/]
---
2016/07/25に「夏真っ盛り！Spark + Python + Data Science祭り」を開催しました。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fconnpass.com%2Fevent%2F34680%2F" title="夏真っ盛り！Spark + Python + Data Science祭り (2016/07/25 19:00〜)" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://connpass.com/event/34680/">connpass.com</a></cite>

今回はClouderaに入って初めてのコミュニティイベントということでしたが、なんと400人を超える応募をいただいてとてもありがたい限りです。 会場をご提供いただいたDMM.comラボ様、発表いただいたサイバーエージェントの内藤さん、DMM.comラボの加嵜さん、LTの皆様ありがとうございました。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Ftogetter.com%2Fli%2F1004741" title="夏真っ盛り！Spark + Python + Data Science祭り まとめ #summerDS" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://togetter.com/li/1004741">togetter.com</a></cite>

# pandasを大規模データにつなぐIbis

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/q9kfzAPGQBoLA7" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Ibis: すごい pandas ⼤規模データ分析もらっくらく #summerDS](https://www.slideshare.net/Cloudera_jp/ibis-pandas-summerds "Ibis: すごい pandas ⼤規模データ分析もらっくらく #summerDS")** from **[Cloudera Japan](http://www.slideshare.net/Cloudera_jp)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/Cloudera_jp/ibis-pandas-summerds">www.slideshare.net</a></cite>

Ibisはpandasの作者でもある Wes McKinney([@wesmckinn](https://twitter.com/wesmckinn)) の作っているライブラリです。 ひとことで言うと、pandasのプログラマブルな処理を大規模データにもできるようにします。 大規模データは高速なSQLエンジンにまかせて、pandas likeなDSLでpandasと連携できるようにしており、データがTB以上のデータに対してもSQLを書かずに試行錯誤できます。

なお、日本語の情報はかなり少ないのですが[^1] 、こちらの[ブログ](http://linux.wwing.net/WordPress/?p=2501)が参考になると思います。 もし、Impalaを試すのであれば[Quick Start VM](http://www.cloudera.com/downloads/quickstart_vms/5-7.html)か、[Cloudera Director](http://www.cloudera.com/downloads/director/2-1-0.html)を使うとブラウザでポチポチするだけでAWS, GCP, Azureに簡単にImpalaクラスターが立てれるのでおすすめです。Director導入方法は[こちら](http://qiita.com/shiumachi/items/90649830cb9b45726d99)が参考になります。

Ibisの詳細は資料を見ていただければと思いますが、いくつか補足をしたいと思います。

## SQLじゃなくてプログラマブルなのは何が嬉しいの？

pandasをお使いの方はわかると思いますが、SQLに比べると試行錯誤がやりやすいと思います。例えば、SQLの途中結果を変数に格納できるので、途中までの処理は共通でそこから先を複数パターン作るというのも同じ変数に格納して、後段のメソッドチェーンを変えれば楽にできるというメリットが有ります。使っている感覚はRailsのActive Recordみたいなイメージです。

## Sparkより7倍速いのは嬉しいの？

大事なのは15TBのデータを4.4秒で処理できる[^2] というスピード感です。処理を投げて帰ってくるまでの時間が短いと、思考の中断が減ります。 例えば、ビルドやテストに時間がかかってコーヒーをいれにいく、みたいな経験はあるんじゃないかと思います。その断絶がなくなるので、考えを継続できますし、ポッと思いついたことをどんどん試行錯誤できます。

## Sparkとの住み分けは？

Ibisは、WesがPythonでend to endでPythonを使って分析をしたいという想いでスタートしています。 個人的にはJupyterとともに対話的に試行錯誤をする強力なツールになっていると思います。 もともとImpalaとPython/pandasをつなぐものとしてスタートしたのですが、RedshiftやPrestoなども今後対応していきたいということも言及されています。 なので、プロトタイピングにJupyterとIbisを使うというのが良いと思います。プロトタイプ後にSparkSQL[^3] でバッチとして安定化をはかるということもできるでしょう。

もう一つの方向性としては、[NetflixがグローバルモデルをSparkで、国・地域のモデルをRで学習している](https://www.infoq.com/jp/news/2016/07/meson-framework-netflix)ように、大規模な機械学習はSpark + MLlibで、絞った後のデータはIbis + scikit-learnでみたいな使い分けは可能だと思います。

# サイバーエージェント内藤さん： Amebaにおけるレコメンデーションシステムの紹介

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/2dcaCyZYeU8I3u" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Amebaにおけるレコメンデーションシステムの紹介](https://www.slideshare.net/cyberagent/ameba-64381671 "Amebaにおけるレコメンデーションシステムの紹介")** from **[cyberagent](http://www.slideshare.net/cyberagent)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/cyberagent/ameba-64381671">www.slideshare.net</a></cite>

Amebaでの協調フィルタリングによるHBaseを使ったリアルタイムレコメンドの話。 Hadoopスタックだとリアルタイム性を出すのにはHBaseを使うのが多いのですが[^4] 、更にClick数を取得してバンディットアルゴリズムも使っているというのは凄いですね。

単純なA/Bテストをするという話はDMM.comラボの加嵜さんもお話されていましたが、バンディットアルゴリズムを組み合わせることで、レコメンド結果が複数のロジックの中でも良い物に動的に改善されていくという仕組みが入っています。 僕個人としてはこうした取り組みを聞いたことがなかったので、とても驚きました。

# DMM.comラボ加嵜さん：Sparkを活用したレコメンドエンジンのパフォーマンスチューニング＆自動化

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/gVyO2JqZqd4GS7" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Sparkを活用したレコメンドエンジンのパフォーマンスチューニング＆自動化](https://www.slideshare.net/knagato/sparkrecommendtuning "Sparkを活用したレコメンドエンジンのパフォーマンスチューニング＆自動化")** from **[knagato](http://www.slideshare.net/knagato)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/knagato/sparkrecommendtuning">www.slideshare.net</a></cite>

チューニングの話もインパクトが大きかったですが、jsonで「レシピ」を書けば、自分のサービスのレコメンドモデルができるという話はとても驚きました。 これを使えば、レコメンドに詳しくない人でも簡単にサービスに導入できそうです。 おそらく、ログフォーマットをきちんと統一して横展開をしているのでしょうね。

# LT

## horiken4 さん：初めてのSparkでハマったこと

Google Data ProcでSparkを使ったら/tmpにjarが貯まるなど、いろいろハマった話を紹介いただきました。

## uryyyyyyyさん：EMR上でPython3系でpysparkする話

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Furyyyyyyy%2Fprivate%2Fefd4e96d292ffdedf2ef" title="EMR上でPython3系でpysparkする話 - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://qiita.com/uryyyyyyy/private/efd4e96d292ffdedf2ef">qiita.com</a></cite>

EMRにAnacondaをいれてPySparkでモデルを作る話でした。逆質問でJuliaを使ってると答えた人が2人くらいだったとのことで寂しかったです。

## suthio さん：Sparkで実装しているレコメンドエンジンの基本的なパフォーマンスチューニング について

DAGを見よう！という話でした。そして、ポケモンGO仲間を募集しているとのことです。

# 終わりに

やはり、自社で手を動かして取り組まれているという話は、様々な知見が含まれていてとても楽しかったです。 AmebaのHBaseを使ったリアルタイムレコメンド＋バンディットアルゴリズムという構成や、DMM.comラボさんのレコメンドの「レシピ」を書くだけで新規サービスのレコメンドモデルができるという話は衝撃的でした。

自分がホストしたイベントの中では過去最大の募集人数だったのですが、大盛況のうちに終わりました。ご協力・ご参加いただいた皆様ありがとうございました。 今回参加できなかった方もたくさんいらっしゃると思いますので、また次回もこういったイベントをできればと考えています。 乞うご期待ください。

[^1]: しかし、日本でIbisというと某研究会しか出てこないので非常につらい

[^2]: [http://blog.cloudera.com/blog/2016/02/new-sql-benchmarks-apache-impala-incubating-2-3-uniquely-delivers-analytic-database-performance/](http://blog.cloudera.com/blog/2016/02/new-sql-benchmarks-apache-impala-incubating-2-3-uniquely-delivers-analytic-database-performance/)

[^3]: こちらもIbisのスコープに入っています

[^4]: リクルートさんも[HBaseを使ったリアルタイムレコメンドをしています](http://www.slideshare.net/recruitcojp/20150625-cloudera)


