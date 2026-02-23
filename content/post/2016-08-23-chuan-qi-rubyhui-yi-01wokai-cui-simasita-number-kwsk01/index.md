---
authors: [aki]
categories: null
date: '2016-08-23 15:25:47-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2016-08-23 15:25:47-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: '川崎Ruby会議 01を開催しました #kwsk01'
keywords: [ruby, kawasaki, 発表, rb, 会議, 川崎, tシャツ, rails, 都内, '01']
recommendations: [/post/2013-10-06-kawasaki-dot-rb-number-003wokai-cui-simasita-number-kwskrb/,
  /post/2022-06-18-kawasaki rb 9 years reflection/, /post/2013-06-29-kawasaki-dot-rb-number-001-di-1hui-mitoatupuwokai-cui-simasita-number-kwskrb/]
---

さる 8/20 に川崎Ruby会議01を開催しました。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fregional.rubykaigi.org%2Fkwsk01%2F" title="トップページ - 川崎Ruby会議01" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://regional.rubykaigi.org/kwsk01/">regional.rubykaigi.org</a></cite>

川崎Ruby会議は、[kawasaki.rb](https://kawasakirb.github.io/)の主催する地域Ruby会議です。 ちゃんとしたまとめはるびまに出ると思うので、ここでは開催の経緯なんかを簡単に書こうと思います。

なお、発表内容が気になる方は[タイムテーブル](http://regional.rubykaigi.org/kwsk01/#section-4)にあるスライドや動画へのリンクを見ると良いと思います。

[togetter](http://togetter.com/li/1014759)

## きっかけは Ruby Kaigi 2015

1. [日本酒が事実上無限に飲める会](http://agile.esm.co.jp/news/2015-12-29-rubykaigi2015-drinkup-report.html)に参加したところ、[咳さん](https://twitter.com/m_seki)に「次のregionalはやらないの」と言われ、基調講演者が決まればありかもと答える
2. 翌日、miyagawaさんと飲んでる[かくたにさん](https://twitter.com/kakutani)と話して、「2回以上続くregionalはやっぱり特定の地域コミュニティがやってるね」と言われる
3. さらに翌朝、帰る直前の[mameさん](https://twitter.com/mametter)に会って「川崎のregionalやるとしたら、基調講演とかしていただけます？」「いいよ」と快諾いただく
4. 次のミートアップで、kawasaki.rbのメンバーに「発表してみたい？やってみたい？」と聞いたら思いの外反応が良かった

というようにトントン拍子でした。

自分としては、やるならいつもの地域コミュニティの皆が話せる場をつくりたい、と思っていたので、これはこれで良かったです。

## とにかく楽をする

神奈川の時はペアプロあり、パネルディスカッションありのもりもりだったのですが、今回は「できるだけ楽をする」ということに徹しました。 東京Ruby会議11は[かなりの額を動かす](http://magazine.rubyist.net/?0054-TokyoRubyKaigi11OrganizeReport)のでかなり重い感じだったのと対象的に、我々は

- 手間を掛けない[^1] 
- お金をかけない

という方式で行きました。

なので、どうしてもやりたい！という人が現れないかぎりは、「やれたら良いよね」はやらないという方針のもと進めてきました。

当初はサイトロゴもなしで行こうとしていました。スタッフTシャツも皆大好き[ミュートンTシャツ](http://tvkshop.net/SHOP/tvk-muton-tns.html)で行こうとしていました。そしたら、ロゴを作るよと実行委員の[ぺらさん](https://twitter.com/peranikov/)の奥さんが言ってくださり、更にはミュートンの可愛さが理解できないためかTシャツもデザインをしていただくという流れになりました。[TMIXさま](https://tmix.jp/)いつもありがとうございます！

正直、この方法はやる気のある人に負荷がかかってしまうというデメリットはあるものの、手を動かす人が一番推進力はあるかなとも思うので、悩ましいところです。

なお、ぺらさんの奥様経由で[重要なリンク](https://www.amazon.co.jp/registry/wishlist/8YU0BYZJ7S6H)が届いているので共有させていただきますね。

> [川崎Ruby会議01のスタッフTシャツ、デザイン素敵です！ #tmix #kwsk01](https://www.instagram.com/p/BJUwblshYNb/)
> 
>  
> 
> igaigaさん(@igaiga555)が投稿した写真 - <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2016-08-20T08:46:48+00:00">2016 8月 20 1:46午前 PDT</time>

<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>
## やってみた感想

コンセプトの「kwskバザー」は、多分なんのこっちゃわからんだろうなぁと思いながら提示しましたが、大江戸Ruby会議の「生活発表会」からヒントを得ました。 始めた3年前の当初からPythonの話もあり、ずっと「kawasaki.rbはkawasaki.pyなのでは！？」というご指摘をいただき続けてきたので、いつもどおりやっていれば多様性がでるだろうな、という思いもあり、それを全面に出してみました。

都内だと特定の言語でも人が集まるかもしれませんが、川崎まで来ると遠い人は来ないのとRalisやってる人口も相対的に都内より少ないので、地域に根ざしたテックコミュニティとしてやってきました。なので、C#やScala、はてはサーバーレスアーキテクチャの話が出てきたわけです。

実際にその多様性について、簡単にまとめたリストが以下になります。気になる方は是非スライドや動画で確認してみてください。

- Rubyとファミコンの仕様
- C#とC++/CLI
- Scala
- Rubyと思ったら猫動画
- Rails
- Railsから気がつけばPHPに変わっていたでござる
- "Railsエンジニア"はただの枕詞のサーバーレス
- Python
- Elixer本の宣伝
- 世界をまたにかける話
- Rubyと思ったら数学の話で終わってしまったでござる

{{< amazon asin="4274219151" title="プログラミングElixir" >}}

[プログラミングElixir](http://www.amazon.co.jp/exec/obidos/ASIN/4274219151/chezou-22/)

- 作者: Dave Thomas,笹田耕一,鳥井雪
- 出版社/メーカー: オーム社
- 発売日: 2016/08/19
- メディア: 単行本（ソフトカバー）
- [この商品を含むブログを見る](http://d.hatena.ne.jp/asin/4274219151/chezou-22)

また、パーフェクトRubyの読書会も続けているためか、「Ruby初心者です」という方もちょこちょこ来ていただいています。kawasaki.rbがきっかけで今回発表された蓑島さんのように一人エンジニアの環境で独学で業務でコードを書くようになった人、転職した人、Herokuのイベントに登壇した人、Railsを学び始めて起業した人など様々な人がいるのも特徴です。 正直、Rubyにとても詳しい人には物足りない側面もあるのかもしれないとは思うのですが、asakusa.rbなどとはまた違った路線で来ているのかなと思っています。 「ここに来れば困ったことを質問できる」とか「ここに来れば自分の知見を気軽に発表できる」という場所を続けてきたかいがあって、今回のregionalにつながったのだと思います。

{{< amazon asin="4774158798" title="パーフェクトRuby (PERFECT SERIES 6)" >}}

[パーフェクトRuby (PERFECT SERIES 6)](http://www.amazon.co.jp/exec/obidos/ASIN/4774158798/chezou-22/)

- 作者: Rubyサポーターズ,すがわらまさのり,寺田玄太郎,三村益隆,近藤宇智朗,橋立友宏,関口亮一
- 出版社/メーカー: 技術評論社
- 発売日: 2013/08/10
- メディア: 大型本
- [この商品を含むブログ (22件) を見る](http://d.hatena.ne.jp/asin/4774158798/chezou-22)

個人的には、[mameさんの発表中にも言われていた「最適化の心構え」](http://d.hatena.ne.jp/ku-ma-me/20160822/p1)のうち、

> 効果を検証せよ：実行平均時間の単純比較ではなく統計的検定とか使うといい。有意差がなかったら変更を捨てろ。

がとても印象的でした。普段検定というと限定された時にしか使われないという偏見があったのですが、ソフトウェア開発にも生きてくるというのは目から鱗が落ちました。

発表・参加いただいた皆様、どうもありがとうございました。そして、実行委員の皆様、本当に何もしない実行委員長でしたが全力でサポートいただきありがとうございました。

なお、[明日はいつものkawasaki.rb](https://kawasakirb.doorkeeper.jp/events/50947)を開催しますので、興味を持たれた方は是非ご参加ください :)

[^1]: Tokyuリスペクト