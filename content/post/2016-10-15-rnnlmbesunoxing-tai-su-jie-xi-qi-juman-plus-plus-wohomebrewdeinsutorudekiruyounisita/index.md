---
title: "RNNLMベースの形態素解析器 JUMAN++ をhomebrewでインストールできるようにした"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2016-10-15T16:20:47+00:00
lastmod: 2016-10-15T16:20:47+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
京大の黒橋・河原研から最近出た[JUMAN++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)をmacOSのhomebrewでinstallできるようにしました。

JUMAN++はRNNLMというディープラーニングベースの言語モデルを使っています。 こちらの記事を読んで知ったという方も多いのではないでしょうか。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Friverwell%2Fitems%2F438e88427363511e9f28&quot; title=&quot;新形態素解析器JUMAN++を触ってみたけど思ったより高精度でMeCabから乗り換えようかと思った話 - Qiita&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://qiita.com/riverwell/items/438e88427363511e9f28&quot;&gt;qiita.com&lt;/a&gt;&lt;/cite&gt;

インストール方法は、現段階では後述する理由のためhomebrew-coreにはまだ入っていないので、tapを使ってください。

[2016/10/23追記] やっと本家homebrewに入ったので、tapは要らなくなりました。 [/追記]

    $ brew install jumanpp

github

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fchezou%2Fhomebrew-jumanpp&quot; title=&quot;chezou/homebrew-jumanpp&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://github.com/chezou/homebrew-jumanpp&quot;&gt;github.com&lt;/a&gt;&lt;/cite&gt;

## JUMAN++のサイト凄い

JUMAN++のサイトには解析を試せるWebアプリケーションがあるのですが、それがなかなか面白いです。

このリンクに対して、

[http://tulip.kuee.kyoto-u.ac.jp/demo/jumanpp\_lattice?text=%E3%81%A9%E3%81%86%E3%82%82%E3%80%81julialang%E7%95%8C%E3%81%AE%E9%A0%91%E5%9B%BA%E3%81%8A%E3%81%98%E3%81%95%E3%82%93%E3%81%A7%E3%81%99](http://tulip.kuee.kyoto-u.ac.jp/demo/jumanpp_lattice?text=%E3%81%A9%E3%81%86%E3%82%82%E3%80%81julialang%E7%95%8C%E3%81%AE%E9%A0%91%E5%9B%BA%E3%81%8A%E3%81%98%E3%81%95%E3%82%93%E3%81%A7%E3%81%99)

こういうラティスを出力してくれます。

![f:id:chezou:20161015161841p:plain](https://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20161015/20161015161841.png &quot;f:id:chezou:20161015161841p:plain&quot;)

楽しい

## JUMAN++とMeCabどっちがいいの？

冒頭のQiitaの記事に対してはRNNLMベースだからというよりは、辞書の改善によるものなのでは？という話はMeCab作者の工藤さんからも指摘があります。

&gt; これってほとんど辞書による改善だと思う...[https://t.co/NnbXreOR48](https://t.co/NnbXreOR48)
&gt; 
&gt; — Taku Kudo (@taku910) [October 13, 2016](https://twitter.com/taku910/status/786520352297918464)

&lt;script async src=&quot;//platform.twitter.com/widgets.js&quot; charset=&quot;utf-8&quot;&gt;&lt;/script&gt;

[@overlast](https://twitter.com/overlast) さんが精力的に更新をしている[neologd](https://github.com/neologd/mecab-ipadic-neologd)との比較をしているため、MeCab側としては現在普通に入手可能なMeCabの辞書としては最も良いものを使っていると思います。 なので、neologd以前に良く問題とされていた「最近の用語が入っていない」という部分に関しては議論の対象にはなっていませんね。

表記ゆれや長音記号のハンドリングに関しては[JUMANの頃からやっていた](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN)ことです。 JUMANの頃からWikipediaを使った語彙獲得やオノマトペの処理など、未知語獲得を黒橋研として頑張っている印象がありました。

また、部分アノテーションか辞書かという話に関しては、以前から議論が分かれている所です。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fplus.google.com%2F107334123935896432800%2Fposts%2FVayh8mndSZi&quot; title=&quot;形態素解析の分野適応は、「点推定+(部分)アノテーション」と「品詞付き単語追加」でどう違うのかという疑問を持ったので、それをつぶやいたところ、@zzzelch…&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://plus.google.com/107334123935896432800/posts/Vayh8mndSZi&quot;&gt;plus.google.com&lt;/a&gt;&lt;/cite&gt;

JUMAN++(の前のJUMAN)とMeCabの比較は以下が詳しいのですが、使っている文法が違ったりなど癖が違うので注意が必要です。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Frekken.g.hatena.ne.jp%2Fmurawaki%2F20140402%2Fp1&quot; title=&quot;JUMAN メモ - murawaki の雑記&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://rekken.g.hatena.ne.jp/murawaki/20140402/p1&quot;&gt;rekken.g.hatena.ne.jp&lt;/a&gt;&lt;/cite&gt;

個人的にはneologdが頻繁に辞書を更新してリリースし続けている状況に対して、JUMAN++の側がどれだけの頻度で更新されたモデルが出せるというところが実用的な差になるのではないでしょうか。普通のエンジニアが部分アノテーションのためのコーパスを作り続けるのは、正直かなり厳しいと思います。\*1[JUMAN++の論文](http://aclweb.org/anthology/D/D15/D15-1276.pdf)でも、4万5千文を再学習することで性能がMeCabを越えたと言っています。

現段階では、実際に比較をしてみてどちらが用途に合うのかを判断するのが良いと思います。

なお、読み推定がしたい場合は[Kytea](http://www.phontron.com/kytea/index-ja.html)を使うといいと思います :)

## homebrew-coreに入っていない理由

この記事を書いている段階では、upstream(v1.01)のMakefileにあるバグのため、`make`に`-j`オプションを付与して並列でビルドすると失敗する問題があります。

このパッチを当てれば大丈夫です。&lt;script src=&quot;https://gist.github.com/chezou/076cb9c407de729ad2e2d04749f07f3e.js&quot;&gt; &lt;/script&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://gist.github.com/chezou/076cb9c407de729ad2e2d04749f07f3e&quot;&gt;gist.github.com&lt;/a&gt;&lt;/cite&gt;

で、何故これがcoreに入っていないかというと、

- 特定のワークアラウンドが必要（並列ビルドを抑える `ENV.depararelize` を使う）な場合は、upstreamのissueを立ててそこへのリンクを貼る必要がある
- juman++は2016/10/15現在レポジトリが公開されておらず\*2、publicなissueがない
- homebrew-coreにはupstreamにマージされないパッチを当てるFormulaは受け入れられない

つまり、 **homebrewでビルド時のバグが有り、かつpublicなレポジトリ（正確にはpublicなticketやissueなど）がない** という条件下ではcoreに登録することはできないようです。 気持ちはわからなくもないけど、すべてGithubにissueがある（あるいは公開MLがある）という前提はちょっと不寛容じゃないかと思います。 Githubで公開されていることしか考えていないんでしょうかね...。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2FHomebrew%2Fhomebrew-core%2Fpull%2F5875&quot; title=&quot;Create formula of jumanpp, RNNLM based Japanese morphological analyzer by chezou · Pull Request #5875 · Homebrew/homebrew-core&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://github.com/Homebrew/homebrew-core/pull/5875&quot;&gt;github.com&lt;/a&gt;&lt;/cite&gt;

はじめての、新規Formula作成でしたがちょっと疲れました。。。

\*1:sugyanさんのアイドルコーパスも好きだから続けられると思っているし、それくらいコーパス作るの大変

\*2:じきに[githubかbitbucketに公開される予定](https://twitter.com/pnnc205j/status/783697937465348098)とのこと


