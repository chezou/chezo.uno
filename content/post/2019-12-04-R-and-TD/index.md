---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "RとTreasure Data"
subtitle: ""
summary: "RTDとRPrstoを使ってRからTreasure Dataにアクセスしてみよう"
authors: [aki]
tags: [R]
categories: [R, TreasureData]
date: 2019-12-04T00:00:00+09:00
lastmod: 2019-12-04T00:00:00+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["RTD"]
---

この記事は、[Arm Treasure Data advent calendar](https://adventar.org/calendars/3932) 3日目です。

公式ドキュメントは、 [Rについてはあまり書かれていない](https://support.treasuredata.com/hc/en-us/articles/360001487927-R-Language-Driver-Install)のですが、RからTreasureDataを使うにはRJDBC以外にもいくつかの方法があります。

基本的には、RPrestoとRTDをおさえておくのが良いでしょう。

- [RPresto](https://github.com/prestodb/RPresto)
  - Facebookが開発しているPrestoのR client。TreasureDataでもアドホックなクエリを投げるときに便利
- [RTD](https://github.com/chezou/RTD)
  - Rからdata frameをTreasure Dataにアップロードするのに使えるR client
- [sparklytd](https://github.com/chezou/sparklytd)
  - RStudio社が開発するRのSpark clientであるsparklyrのplugin
  - 内部で使うtd-sparkはSparkのサポートバージョンが上がるのが速いが、sparklyrのSparkの新バージョンサポートが遅いので少し低調なメンテナンス

実際の、RPrestoとRTDの使い方は以下のRmarkdownを見ていただくのが良いかと思います。
https://rpubs.com/chezou/TD-from-RPresto-RTD


# RTDのインストール

インストールは、 `devtools::install_github` を使うか、 `install-github.me` を使うことでできます。

RTDは v0.2.0 からCRANに上げるのを辞めました。これはこれで一つの記事が書けるのですがそれはまた別の機会に譲ろうと思います。


```R
source("https://install-github.me/chezou/RTD@v0.2.0")
```

インストール後は、`apikey` と `endpoint` を適切なものを渡して上げることで、uploadができます。例えば `nycflights13` パッケージの `flights` データをアップロードしてみましょう。

```R
library(RTD)

client <- Td(apikey = Sys.getenv("TD_API_KEY"), endpoint="api.treasuredata.com")
td_upload(client, "test", "flights", nycflights13::flights, overwrite=T)
```

v0.1.0 ではembulkが必須でしたが、今のバージョンは bulk import APIを使うようになっているため、特に追加でツールをインストールする必要はありません。

# RPrestoでの接続

`src_presto` する際には、 `user` に TDのAPI keyを渡すこと、hostは[こちらのendpoint](https://support.treasuredata.com/hc/en-us/articles/360001474288-Sites-and-Endpoints#Endpoints)を参照してください。schemaはDatabase名、 catalogは `td-presto`のままにしてください。

```R
library(RPresto)
library(dplyr)

db <- src_presto(
  host="https://api-presto.treasuredata.com",
  port=443,
  user=Sys.getenv("TD_API_KEY"),
  schema='test',
  catalog='td-presto'
)

flights_tbl <- tbl(db, 'flights')
```

`flights_tbl` にテーブルが変数として割り当てられました。が、実際にはdplyrの諸々の処理を実行するときにSQLが走るのでalias程度に考えてください。

# dplyrとggplot2で可視化する

それでは、 `flights_tbl` をdplyrを使い集計して飛行機の平均遅延時間などを算出して、ggplot2で可視化してみましょう。

```R
delay <- flights_tbl %>%
  group_by(tailnum) %>%
  summarise(count = n(), dist = mean(distance, na.rm = TRUE), delay = mean(arr_delay, na.rm = TRUE)) %>%
  filter(count > 20, dist < 2000) %>%
  collect

# plot delays
library(ggplot2)
ggplot(delay, aes(dist, delay)) +
  geom_point(aes(size = count), alpha = 1/2) +
  geom_smooth() +
  scale_size_area()
```

このような図ができたかと思います。

![](rpresto_ggplot.png)

それでは、HappyなRとTreasureDataライフを！
