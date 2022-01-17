---
title: '#JapanR で話題だった「データサイエンティスト養成読本R活用編(通称"Julia入門本")」を読みました #JuliaAC'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-12-13 00:02:00+00:00
lastmod: 2014-12-13 00:02:00+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [julia, 入門, 読本, 外観, dplyr, 興味, 基礎, データサイエンティスト, 養成, '12']
recommendations: [/post/2015-12-10-julianoqing-bao-woshou-ji-situdukeruniha/, /post/2015-12-25-juliadede-raretamainayan-yu-wosheng-rishang-gerufang-fa-number-juliaac/,
  /post/2014-12-03-juliahuan-jing-gou-zhu-2014-ver-number-julialang/]
---
この記事は[Julia Advent Calendar](http://qiita.com/advent-calendar/2014/julialang)の12日目の記事です。

昨日12/12に発売された、データサイエンティスト養成読本 R活用編をいただきましたので、読ませていただきました。

![](/img/2014/12/13/000200/20141212232744.jpg)

シリーズ第一冊目の「データサイエンティスト養成読本」と比較するとよりRに特化した内容になっています。

- 里さん、酒巻さんによる心構え的な話や基礎となる統計知識でざっと外観したあとで、
- 市川さんのRでのモダンな集計方法
- 福島さんの時系列分析の基礎
- 安倍さんによる.NET FrameworkからRを使う話
- 和田さんによるH2Oやparallelの話
- [@sorami](https://twitter.com/sorami)さん、西薗さんによるJuliaの話

が展開されています。

<iframe src="https://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&amp;bc1=000000&amp;IS2=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=chezou-22&amp;o=9&amp;p=8&amp;l=as4&amp;m=amazon&amp;f=ifr&amp;ref=ss_til&amp;asins=4774170577" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><iframe src="https://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&amp;bc1=000000&amp;IS2=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=chezou-22&amp;o=9&amp;p=8&amp;l=as4&amp;m=amazon&amp;f=ifr&amp;ref=ss_til&amp;asins=4774158968" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>

表紙を見ていただくとわかりますが、「Julia入門」の文字がでかでかと掲げられています。凄い。 日本の商業誌ではJuliaについて書かれた本は、おそらくはじめてだろうとのことです[^1] 。

話としては、Juliaの出来た歴史的な経緯と基礎的な使い方が記されています。Juliaってなんだろう？という人には外観をしる上で取っ付き易い文章になっていると思います。特に本文中にでてくるJohn Myles White[^2] やStefan Karpinskiなど、コアなコミッターの情報がちりばめられているのはJuliaというググらビリティの低い名前から情報を収集する重要な緒となると思います。

ここで興味をもった人は、[Julia Advent Calendar](http://qiita.com/advent-calendar/2014/julialang)の記事を色々読まれると良いのではないでしょうか。

Julia以外で特に興味深かったのは、市川さんによるdplyrやtidyr, pipeRの話です。特に、dplyrのSQLっぽい集計処理やpipeRでのメソッドチェーンっぽい処理を見ていると、「それ、Ruby(Active Record)でできるんやで」と一周回ってきた感覚になりました[^3] 。

本書は割りと濃い話が多いので、Rの入門書を読んだけど、もっとモダンな書き方をしたい！応用したい！という人にオススメです。また、Rの人たちが使い始めているJuliaってどんな言語だろう？と興味が湧いた方にもオススメです。

[^1]: 薄い本は既に出ています [http://yomichi.hateblo.jp/entry/2014/01/05/160714](http://yomichi.hateblo.jp/entry/2014/01/05/160714)

[^2]: 入門機械学習やバンディットアルゴリズム入門の著者としても知られる

[^3]: もちろん、Rで処理できるけど速度が速いことが売りですが


