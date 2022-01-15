---
title: IDCFクラウドの500円サーバーでpodcast serverをはじめて8ヶ月が経ちました
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2015-11-22 21:30:37+00:00
lastmod: 2015-11-22 21:30:37+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [ストレージ, オブジェクト, rubyist, 転送, おかげさま, クラウド, '500', club, 安定, podcast]
recommendations: [/post/2015-06-07-ri-ben-ren-xiang-kepodcastyarunaraidcfkuraudogaliang-sasou/,
  /post/2015-05-03-rubyist-dot-club-hazimetemasita-number-rubyistclub/, /post/2015-12-30-2015nian-wozhen-rifan-tute/]
---
どうも、最近PSYCHO-PASSを見終わってシュタインズ・ゲートを見ています。 この記事はIDCFクラウド1周年キャンペーンを応援する記事です。\*1

Rubyistといろいろなことを話すpodcast [rubyist.club](http://rubyist.club/) をはじめて半年経ちました。 最近リリース前のドタバタでご無沙汰していますが、12月には次回の配信をできると思います。

IDCFクラウドは、 [@bash0C7](https://twitter.com/bash0C7) さんが使ってますよー、というのをいつかのお友達紹介キャンペ言っていて知りました。おかげさまで、そこからクーポンを使ってしのいでいます :)

[rubyist.clubはおかげさまで安定運用をしています](https://chezou.hatenablog.com/entry/2015/06/07/210000)。クーポンのおかげでほとんどまだお金を払っていないのですが、それを割り引いてもカジュアルに使うのには良いです。 AWSほど複雑な設定はしづらいですが、逆に言うとシンプルに使えるのが便利です。 本当はプログラマブルにAPI経由で使えるようなのですが、そのへんの経験が浅い自分でもGUIベースで使えるので楽ちんです。ゆくゆくは、itamaeで構成管理をしたいなぁと思っています。

S1プランは500円で使えるのですが、オブジェクトストレージとかを使わない分には本当に500円を超えることはまず無いです。 オブジェクトストレージはCyber Duckとかを使うことでS3のように便利に使えるので良いのですが、転送量課金が結構大きいので、おそらくpodcastのような転送量が増えるコンテンツにはノード内にデータをおけるならそれで済ますのが良いでしょう。 また、オブジェクトストレージはちょいちょい障害の報告がきますが、通常のノードはほとんど落ちることはないので、安定して使えます。

ドキュメントや使用事例がweb上の情報としては少ない感じがするのがあれですが、それを補って余りあるお値打ち感が魅力です。

是非、この機会に使ってみるとよいでしょう！

\*1:つまり、宣伝ですね


