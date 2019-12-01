---
title: "データを一箇所に集めることでデータ活用の民主化が進んだ話"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2016-05-05T22:20:46+00:00
lastmod: 2016-05-05T22:20:46+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
先日、この記事を読んで分析のハードルを下げること大事だよね、というのを思い出したのでつらつらと書いてみようと思います。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Furaura%2Fitems%2F8020989e79a6985b0c29&quot; title=&quot;マーケティング担当者にSQLを完全マスターさせた話 - Qiita&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://qiita.com/uraura/items/8020989e79a6985b0c29&quot;&gt;qiita.com&lt;/a&gt;&lt;/cite&gt;

内容としては正直タイトル詐欺で、SlackからRDSにクエリ発行できるようにして、各種権限を持っているエンジニアでなくても分析できるようになったよ、という話です。

ここでいう「データ活用の民主化」というのはかっこ良く言ってみたかっただけで、「データ分析を生業にしている人以外もデータを活用してビジネスを進められるようになる」というくらいのニュアンスだと思って下さい。 「データ分析」というとアナリストの人がやること、みたいな職務が分かれている環境もあるとは思いますが、そうではない会社（前職）の一例です。

## データ活用が広まった流れ

1. 数秒〜数十秒で対話的にクエリが返ってくると、トライアンドエラーが100倍くらいできる
2. 今まで実行計画を気にして避けていたことにガンガン挑戦して、新しいメタデータ達が付与される
3. エンジニアがSQLに慣れ親しむ\*1と、ノウハウがチームや社内ブログに蓄積される
4. 身近なエンジニアがサポートできるようになり、Webディレクターの人もSQLを覚えてKPIを主体的に考え始める

こういう流れでSQLが社内のエンジニアからWebディレクターの人たちに広まっていきました。 また、SQLの苦手意識が減ってきたことで、プロダクトのフェーズに応じて変化するKPIを考える力が、数字が得意ではないWebディレクター\*2にも身についてきました。

## 前提

この流れを支える前提としては、

- Redshiftに入るデータを整備するいわゆる[データエンジニアリング](http://insightdataengineering.com/blog/Data_Science_vs_Data_Engineering.html)をしている人\*3がいた事
- [@mineroaokiさん](https://twitter.com/mineroaoki)が「データの移動は悪だ！必要なテーブルは言えば集める！」\*4と一貫して主張し続けて、一箇所でSQL叩けばだいたいなんとかなる（と思える）ようにしてくれていたこと\*5
- 分析をする人が楽できるようにsshやproxyもなしで[Postico](https://eggerapps.at/postico/)みたいなGUIクライアントで直接Redshift叩けるようにしてくれたこと

といった事実があります。 3つめのポイントなんかは、前述のQiitaに書かれていた記事のポイントですよね。

ここでいう「データを一箇所に集める」ということは、分析する人の立場からすると「一箇所でSQL叩けばだいたいなんとかなる」という状況です。 もちろん、処理方法はSQLに限った話ではないですが、

- 分析のために余計なデータ転送のコストをかけない
- 一定の前処理はなされており、何かしらの統一した方法でデータを処理すればよい

という状況を想定しています。

ここまでお膳立てされて、最初は面倒くさいと思って僕含むRubyに逃げていたエンジニアたちも[Window関数最高！](http://techlife.cookpad.com/entry/2015/12/18/151257)と言い始めるに至りました。

また、多くのWebディレクターの人たちはRubyなどのスクリプト言語は書けない人がほとんどでしたが、データが一箇所に集まったおかげで「SQLだけ覚えればエンジニアの手を借りること無く色々できる！」と思っていただけたのも良かったのかもしれません。

@mineroaokiさんの思想はこちらのスライドにたっぷり詰まっています。P.12から「一箇所にまとめる」話がありますので、そこだけでも読んでみると良いでしょう。

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/1KKYwrA60I1FMR&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[Cookpad TechConf 2016 - DWHに必要なこと](https://www.slideshare.net/mineroaoki/cookpad-techconf-2016-dwh &quot;Cookpad TechConf 2016 - DWHに必要なこと&quot;)** from **[Minero Aoki](http://www.slideshare.net/mineroaoki)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/mineroaoki/cookpad-techconf-2016-dwh&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

なお、Airbnbは[バッチ処理用とアドホッククエリ用とでクラスターをレプリしている](https://medium.com/airbnb-engineering/reair-easy-to-use-tools-for-migrating-and-replicating-petabyte-scale-data-warehouses-5153f8a433da)ようですが、分析に必要なデータが一箇所にまとまっていると言っても差し支え無いでしょう。

## ちなみに

実はもう一つの要素として、インフルエンサーとなるディレクターの人が居たのも事実です。 彼女は、今や[他のチームにSQLコンサル（！）](https://twitter.com/h13i32maru/status/722215455536996356)もしているようですが、昔はSQLができなくてエンジニアに毎回お願いしていたそうです。 その当時一緒に組んでいたエンジニア（SQLはめちゃ得意）が、あまりに面倒くさそうに対応するのが嫌でSQLを覚え始めたと聞きました。 その後、社内のデータ分析相談チャットで質問しまくったり、青木さんに質問したり、使ったクエリを自分のメモとしてストックすることで、他のディレクターに3,4段はネストするサブクエリ含んだSQLを展開するに至っています。

彼女がSQLを武器にできるようになったのはもう一つ、青木さんの本の助けもあったと聞いています。 おそらく、他のWebディレクターの人たちにとっては、同じポジションの人に相談できるのは似たようなところを躓いたりした経験を聞けたりするのが良いのだと思います。

[![10年戦えるデータ分析入門 SQLを武器にデータ活用時代を生き抜く (Informatics &amp;IDEA)](http://ecx.images-amazon.com/images/I/513Kq0DFpnL._SL160_.jpg &quot;10年戦えるデータ分析入門 SQLを武器にデータ活用時代を生き抜く (Informatics &amp;IDEA)&quot;)](http://www.amazon.co.jp/exec/obidos/ASIN/4797376279/chezou-22/)

[10年戦えるデータ分析入門 SQLを武器にデータ活用時代を生き抜く (Informatics &amp;IDEA)](http://www.amazon.co.jp/exec/obidos/ASIN/4797376279/chezou-22/)

- 作者: 青木峰郎
- 出版社/メーカー: SBクリエイティブ
- 発売日: 2015/06/30
- メディア: 単行本
- [この商品を含むブログ (3件) を見る](http://d.hatena.ne.jp/asin/4797376279/chezou-22)

## データを一箇所に集めると民主化が進むのか？

もちろん、ただ集めるだけでは進みません。

「一箇所に集める」とはデータ分析をする人のコストを徹底的に下げる、ということに他なりません。 データ分析基盤を用意する人にとっては正直面倒なことも多いとは思います。 ですが、使ってもらってなんぼのデータ分析基盤は、最大限分析する人にやさしくするのが必須です。 自分より苦手意識を持つ人に、「あちらのDBは実行計画気をつけて、こちらのDBはjoinすると辛いから...」みたいな面倒くさいことやってくれると思いますか？

その上で、そうしたデータをどう料理すればいいのかを、まずはエンジニアを中心とした比較的データやSQLに慣れ親しんでいる人がお手本を見せます。 もちろん、得られた知見を含む、加工したデータも蓄えていきます。

このときに、社内Wikiやブログではコピペで動く状態のクエリ（コメントもできれば付けて）と結果を添えて共有すると良いでしょう。 SQLが苦手な人でも、「コピペではじめるDAUの分析」みたいなタイトルの記事だったらきっと読んでくれます。

良いツールや本を広めていくのと同じように、「何ができるようになるか」という具体例とともに、少しずつ仲間を増やしていくことが大事です。

## データ活用の民主化が進むと

[定番料理の提案](http://techlife.cookpad.com/entry/2015/09/08/094902)の話でも、「検索セッション」の話が出てきていますが、検索チームなら「検索セッション」を見て仮説を立てて検証するよね、というように、生のデータを見るだけではなく、セッションのような塊で見ることで仮説を立てる、ということがデータに詳しくない人（元のデータやクエリを作った人ではない人）でもできるようになります。

もちろん、Jupyter notebookのようなノートブック系のツールが発展することで、それらが加速することはあると思いますが、本質的に大事なのは「データにどういう切り口を与えて見ればいいのか」ということを、多くの人ができるようになることです。

パソコンやワープロが普及したことで、タイプライター専業の人の職がなくなってしまいましたが、その代わりに何かをしたい人がワープロを道具として新しいことを生み出すことができるようになりました。 SQLやデータも同じで、データ活用の民主化が進むことでドメインに対する知識やパッションを持った人が、道具としてのデータを使って新しいことを生み出すことができるようになると信じています。

この話を他の人にすると「でも、それエンジニアが凄い会社だからできたんでしょ？」と言われるのですが、多分データを一箇所に集めて誰でも分析できるようになった時にどうなるか、というイメージがわかないのがコストを割けない1つの原因なのではないか、と思いこういった記事を書いてみました。 もちろん、特にデータエンジニアリングを中心にいくつかの技術的ハードルはあるとは思いますが、チャレンジする価値はあると思います。

\*1:前職はRuby大好きな人が多かったため、アプリケーション用のSQLはかけるけどサブクエリやWindow関数バリバリの分析用クエリ書ける人は最初は少なく、手元でRubyで処理することが多かった

\*2:後に、もともと学校の算数・数学大嫌いだったと笑いながら言っていたのが印象的でした

\*3:@mineroaokiさんたち

\*4:実際に、テラバイト規模のデータを移動するのにN時間とかアホみたいなことも世の中にはあったりしますよね

\*5:もちろん、権限ないと見れないスキーマとかもありましたが

