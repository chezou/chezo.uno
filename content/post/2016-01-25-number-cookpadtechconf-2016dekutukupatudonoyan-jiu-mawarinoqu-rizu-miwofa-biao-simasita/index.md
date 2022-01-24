---
title: '#CookpadTechConf 2016でクックパッドの研究まわりの取り組みを発表しました'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2016-01-25 00:00:00+00:00
lastmod: 2016-01-25 00:00:00+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [仕組み, '2016', カテゴリ, ため, 情報, techconf, 推薦, ありがたい, 開催, 機械学習]
recommendations: [/post/2017-10-20_OReilly-ml-for-business-cf835ff4c128/, /post/2016-11-14-cloudera-world-tokyo-2016deji-jie-xue-xi-purodakutonozuo-rifang-wohua-simasita-number-cwt2016/,
  /post/2016-03-30-zhuan-zhi-simasita/]
---
1/23に開催された[Cookpad TechConf 2016](http://techconf.cookpad.com/)で、クックパッドの研究開発に関する取り組みを紹介させていただきました。

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/GEKzIf4kdyFWOF" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[R&D at Foodtech company - #CookpadTechConf 2016](https://www.slideshare.net/chezou/rd-at-foodtech-company-cookpad-techconf-2016 "R&D at Foodtech company - #CookpadTechConf 2016")** from **[Michiaki Ariga](http://www.slideshare.net/chezou)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/chezou/rd-at-foodtech-company-cookpad-techconf-2016">www.slideshare.net</a></cite>

メッセージとして伝えたかったことは、

- [たべみる](http://info.tabemiru.com/)という主にtoB向けに提供しているクックパッドの検索履歴を可視化したサービスを[学術提供](https://cookpad.com/terms/tabemiru/academy)開始しました
- 普段はAndroid書いてるアプリエンジニアが、自らレシピをカテゴリ分類できる仕組みがありますよ

ということです。

[2016/01/25 10:04追記] たべみるの学術アカウントは無償提供させていただいております [/追記]

たべみるは、社内でも季節の食材やトレンドを見てレシピを選定するためにも活用しているのですが、地域ごとの差異なんかもわかったりします。なので、生の検索データではないのですが統計的に見やすくなった情報をインタラクティブに調べることができるので、研究のあたりを付けるための仮説を出すためには十分使えるんじゃないかなと思っています。

もう一つは、アプリエンジニアも機械学習できる仕組みの話ですが、これには少し端折った点があります。 普通の機械学習をするためには（DeepLearningはまた違うけど）、テキストから適切な情報を取り出してベクトルに変換する必要があります。そして、その変換の仕方が肝になってきているのですが、そこは既に知見があるので仕組みの裏側に隠蔽されています。また、今回の資料にはないですが、クックパッドにはユーザーが推薦するカテゴリ情報というものがあり、カテゴリベースで正解データを与えることが出来ます。そして、それがかなり有用な教師データとなっています。

あとは、さらりとデグレを防ぐために性能をチェックしてます、という話も含めていますが、ここに至るまでに痛い失敗をしたのでこういう形に落ち着いています。機械学習の予測モデルは、確率的な要素が含まれるので普通のrspecなどのテストではなかなか検出できません。そこで、少数の評価セットを予め用意しておいて、性能が一定基準以下になったらアラートをモデルの更新を止める仕組みが入っています。過去には、これがなかったために、テキストからベクトル化するために使っている辞書データのミスマッチで予測器が壊れてしまったこともありました。

比較的小さいチームなので、特に気をつけているのがその研究はユーザーにどういう価値があるのか？という事を考えること。自分が取り組んでいる情報推薦なんかは割りとプロダクトと表裏一体なのですが、これからも先端を見据えつつ実際に役に立つ技術を追求していけたらと思います。

今回、運営側の方々も少数精鋭で開催していただいて本当にありがたいと思います。1月のカンファレンスは辛いんですよね...[^1] 。 楽屋で青木さんがmirakuiさんを煽るのを聞きながら皆で爆笑したり、いつものカンファレンスとは一味ちがった楽しみ方ができました。 去年は神奈川Ruby会議の開催をできて、今年は32歳になる前にCookpad TechConfで登壇と大きな経験を積めて本当にありがたい限りです。

ちなみに、今日が誕生日なので例のリスト置いておきますね[^2] 

[http://www.amazon.co.jp/registry/wishlist/34KS1RGABYTM7/](http://www.amazon.co.jp/registry/wishlist/34KS1RGABYTM7/)

[^1]: 大晦日・元旦に神奈川Ruby会議の打ち合わせした記憶が蘇ってきます

[^2]: この手法、2年連続である


