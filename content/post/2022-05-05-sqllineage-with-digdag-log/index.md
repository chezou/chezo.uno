---
title: sqllineage を使って digdag のログから Treasure Data のクエリのリネージを作ってみた
subtitle: オープンソースを使って Hive や Trino のクエリからリネージを作ろう
date: 2022-05-05 19:58:10-07:00
summary: ''
draft: false
featured: false
authors: [aki]
lastmod: 2022-05-05 19:58:10-07:00
tags: []
categories: [digdag, lineage, sql]
projects: []
image: {caption: sqllineage で Treasure Workflow のリネージを出してみた例, focal_point: '', preview_only: false}
keywords: [sql, 可視化, td, sqllineage, 実装, digdag, データ, python, レベル, 流れ]
recommendations: [/post/2016-05-05-detawo-ge-suo-niji-merukotodedetahuo-yong-nomin-zhu-hua-gajin-ndahua/,
  /post/2014-01-18-ke-xue-ji-suan-niokerujun-zhi-hua-aruihanazepythongazhao-shi-nita-yan-yu-nosieawoduo-tuteiruka/,
  /post/2019-12-24-python-custom-scripting/]
---
データリネージとは、DBなどでどのデータがどこから来てどこに行った、という「来歴」とも呼ばれる情報です。

自分がこの言葉を知ったのは、前職でCloudera Navigatorという製品を扱ったときにこの機能が実装されていることを知りました。
引き継いだ複雑なSQLなどのワークフローを渡されたときに、どういう流れになっているのかを可視化できるのがとても魅力でした。

{{< figure src="./nav_lineage.webp" title="Cloudera Navigatorのlineage。 https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/cn_lineage_generation.html より" >}}

そんなlineageですが、Pythonの sqllineage というパッケージで分析・可視化できることを知りました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/reata/sqllineage" data-iframely-url="//iframely.net/4q6WPtz?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

sqllineage は Pythonで実装されているSQLのlinegaeを解析する部分と、Reactで実装された可視化のウェブアプリケーション sqllineagejs で成り立っています。

実は去年ぐらいにちらほら使っている人がいたのは後から知りました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://dev.classmethod.jp/articles/try-sqllineage/" data-iframely-url="//iframely.net/XlQhNj3?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

</br>

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://zenn.dev/yohei/articles/2021-05-08-sql-lineage-snowflake" data-iframely-url="//iframely.net/jwgoEni?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

これを使ってTreasure Dataのデータの流れの可視化をしてみたいと思ったのですが、TDではちょうどworkflowエンジンのdigdagのログに実行されたSQLが書かれているのに気づきました。

そこで、digdagのTDのSQLを実行する `td>`, `td_ddl>` オペレータからSQLを抽出・変換するコマンド、 digdaglog2sql を作り、可視化をしてみました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/digdaglog2sql" data-iframely-url="//iframely.net/5Up1iQ9?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

詳しい使い方は、GitHubを見ていただければと思いますが、Python 3.7以上が入っている環境であれば、pipで簡単にインストールできます。

```sh
pip install --user digdaglog2sql
```

TDからダウンロードしてきたワークフローのログがあれば、そこからSQLを抽出して保存できます。

```sh
digdaglog2sql --input workflow-log.txt --output output.sql
```

また、ワークフローのSession IDを指定すれば、そこからSQLに変換した結果を保存できます。

```sh
export TD_API_KEY=1234XXX/YYYYYYYY
digdaglog2sql --session-id 12345 --site us --output output.sql
```

また、endpointオプションを使えば自前でホストしたdigdagからもSQLを取得できます。

```sh
digdaglog2sql --session-id 12345 --endpoint digdag.example.com --output output.sql
```

~~注意点としては、2022/05/05現在のPyPIにある sqllineage と その裏側で依存している sqlparse の最新バージョンでは、 Trino やHiveなどの一部の機能がうまくColumnレベルのlineageの解析ができません。~~

{{% callout note %}}
2022/05/11 現在、sqllineageの Hive, Trino に関する問題は修正され 1.3.5 でリリースされました。
これに伴い、sqllineageをsourceからインストールする際に必要だったnodeも不要になりました。

2022/10/06 sqlparseの 0.4.3 もリリースされたので　upstreamの修正はすべて反映されました。
{{% /callout %}}

~~今、Pull Requestを出しているところなので、これらがリリースされれば解決されると思います。~~

* ✅ https://github.com/reata/sqllineage/pull/252 -> 1.3.5 でリリース済み
* ✅ https://github.com/reata/sqllineage/pull/255 -> 1.3.5 でリリース済み
* ✅ https://github.com/andialbrecht/sqlparse/pull/662 -> 0.4.3 でリリース済み
* ✅ https://github.com/andialbrecht/sqlparse/pull/664 -> 0.4.3 でリリース済み

~~ひとまず、パッチを当てたbranchをGitHubに用意したので、 nodeをインストールした環境で 以下のようにインストールしてください。~~

```sh
pip install git+https://github.com/chezou/sqlparse.git@trino#egg=sqlparse==0.4.3.dev0
pip install sqllineage
```

sqllineageをインストールした後は、出力したSQLファイルを指定すれば、可視化できます。

```sh
$ sqllineage -g -f output.sql
 * SQLLineage Running on http://localhost:5000/?f=output.sql
```

ブラウザを開けば、このようなColumnレベルやテーブルレベルの lineage が作成でき、拡大縮小もしながら眺められます。

{{< figure src="./featured.webp" title="SQL lineageの例" >}}

ぜひ、試してみてください。
