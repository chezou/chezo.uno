---
title: RNNLMベースの形態素解析器 JUMAN++ をhomebrewでインストールできるようにした
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2016-10-15 16:20:47+00:00
lastmod: 2016-10-15 16:20:47+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [juman, homebrew, core, jumanpp, issue, mecab, コーパス, formula, 部分, 辞書]
recommendations: [/post/2011-10-01-cjumannoinsutoruwotiyotutojian-dan-nisurucjuman-installer/,
  /post/2018-12-01_Windows-64bit-MeCab--KyTea-------2018-b283b6c7b33c/, /post/2016-12-31-2016nian-wozhen-rifan-tute/]
---
京大の黒橋・河原研から最近出た[JUMAN++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)をmacOSのhomebrewでinstallできるようにしました。

JUMAN++はRNNLMというディープラーニングベースの言語モデルを使っています。 こちらの記事を読んで知ったという方も多いのではないでしょうか。

[新形態素解析器JUMAN++を触ってみたけど思ったより高精度でMeCabから乗り換えようかと思った話 - Qiita](http://qiita.com/riverwell/items/438e88427363511e9f28)

インストール方法は、現段階では後述する理由のためhomebrew-coreにはまだ入っていないので、tapを使ってください。

[2016/10/23追記] やっと本家homebrewに入ったので、tapは要らなくなりました。 [/追記]

    $ brew install jumanpp

github

[chezou/homebrew-jumanpp](https://github.com/chezou/homebrew-jumanpp)

## JUMAN++のサイト凄い

JUMAN++のサイトには解析を試せるWebアプリケーションがあるのですが、それがなかなか面白いです。

この「どうも、julialang界の頑固おじさんです」というフレーズを解析した結果が[こちら](http://tulip.kuee.kyoto-u.ac.jp/demo/jumanpp_lattice?text=%E3%81%A9%E3%81%86%E3%82%82%E3%80%81julialang%E7%95%8C%E3%81%AE%E9%A0%91%E5%9B%BA%E3%81%8A%E3%81%98%E3%81%95%E3%82%93%E3%81%A7%E3%81%99)です。

こういうラティスを出力してくれます。

![](/img/2016/10/15/162047/20161015161841.png)

楽しい

## JUMAN++とMeCabどっちがいいの？

冒頭のQiitaの記事に対してはRNNLMベースだからというよりは、辞書の改善によるものなのでは？という話はMeCab作者の工藤さんからも指摘があります。

{{< tweet user="taku910" id="786520352297918464" >}}


[@overlast](https://twitter.com/overlast) さんが精力的に更新をしている[neologd](https://github.com/neologd/mecab-ipadic-neologd)との比較をしているため、MeCab側としては現在普通に入手可能なMeCabの辞書としては最も良いものを使っていると思います。 なので、neologd以前に良く問題とされていた「最近の用語が入っていない」という部分に関しては議論の対象にはなっていませんね。

表記ゆれや長音記号のハンドリングに関しては[JUMANの頃からやっていた](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN)ことです。 JUMANの頃からWikipediaを使った語彙獲得やオノマトペの処理など、未知語獲得を黒橋研として頑張っている印象がありました。

また、部分アノテーションか辞書かという話に関しては、以前から議論が分かれている所です。

[形態素解析の分野適応は、「点推定+(部分)アノテーション」と「品詞付き単語追加」でどう違うのかという疑問を持ったので、それをつぶやいたところ、@zzzelch…](https://plus.google.com/107334123935896432800/posts/Vayh8mndSZi)

JUMAN++(の前のJUMAN)とMeCabの比較は以下が詳しいのですが、使っている文法が違ったりなど癖が違うので注意が必要です。

[JUMAN メモ - murawaki の雑記](http://rekken.g.hatena.ne.jp/murawaki/20140402/p1)

個人的にはneologdが頻繁に辞書を更新してリリースし続けている状況に対して、JUMAN++の側がどれだけの頻度で更新されたモデルが出せるというところが実用的な差になるのではないでしょうか。普通のエンジニアが部分アノテーションのためのコーパスを作り続けるのは、正直かなり厳しいと思います。[^1] [JUMAN++の論文](http://aclweb.org/anthology/D/D15/D15-1276.pdf)でも、4万5千文を再学習することで性能がMeCabを越えたと言っています。

現段階では、実際に比較をしてみてどちらが用途に合うのかを判断するのが良いと思います。

なお、読み推定がしたい場合は[Kytea](http://www.phontron.com/kytea/index-ja.html)を使うといいと思います :)

## homebrew-coreに入っていない理由

この記事を書いている段階では、upstream(v1.01)のMakefileにあるバグのため、`make`に`-j`オプションを付与して並列でビルドすると失敗する問題があります。

このパッチを当てれば大丈夫です。

{{< gist chezou 076cb9c407de729ad2e2d04749f07f3e >}}

で、何故これがcoreに入っていないかというと、

- 特定のワークアラウンドが必要（並列ビルドを抑える `ENV.depararelize` を使う）な場合は、upstreamのissueを立ててそこへのリンクを貼る必要がある
- juman++は2016/10/15現在レポジトリが公開されておらず[^2] 、publicなissueがない
- homebrew-coreにはupstreamにマージされないパッチを当てるFormulaは受け入れられない

つまり、 **homebrewでビルド時のバグが有り、かつpublicなレポジトリ（正確にはpublicなticketやissueなど）がない** という条件下ではcoreに登録することはできないようです。 気持ちはわからなくもないけど、すべてGithubにissueがある（あるいは公開MLがある）という前提はちょっと不寛容じゃないかと思います。 Githubで公開されていることしか考えていないんでしょうかね...。

[Create formula of jumanpp, RNNLM based Japanese morphological analyzer by chezou · Pull Request #5875 · Homebrew/homebrew-core](https://github.com/Homebrew/homebrew-core/pull/5875)

はじめての、新規Formula作成でしたがちょっと疲れました。。。

[^1]: sugyanさんのアイドルコーパスも好きだから続けられると思っているし、それくらいコーパス作るの大変

[^2]: じきに[githubかbitbucketに公開される予定](https://twitter.com/pnnc205j/status/783697937465348098)とのこと


