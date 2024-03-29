---
title: サイバー攻撃としてのフェイクニュース
description: このポストは、最近もやもやっと思っていることを吐き出したポエムである。厳格なファクトチェックを経たものと期待しないで欲しい。
date: '2017-01-16T14:55:32+09:00'
categories: []
authors: [aki]
keywords: [ニュース, 攻撃, ロシア, facebook, 記事, ドイツ, こと, 情報, instant, アメリカ]
recommendations: [/post/2014-12-15-number-ingress-dehurutaimunopuroezientotochu-hui-tutahua/,
  /post/2019-03-29_ngekkan-lambda-note-article/, /post/2016-12-21-number-eigo-tosi-aruihazi-chi-tinoye-wu-wai-huo-dong-nosok-kefang/]
---

_このポストは、最近もやもやっと思っていることを吐き出したポエムである。厳格なファクトチェックを経たものと期待しないで欲しい。_

### tl;dr

*   サイバー攻撃としてプロパガンダをばらまくことを行うハッカーグループがいる
*   彼らはfake newsサイトをいくつも作って選挙等に介入している
*   不正アクセスして得た結果を、自分たちに有利な情報をフィルターしてWikileaksに流し、ニュースの情報源をコントロールしている

### 本文

ここ最近、日本でも”fake news”という単語を聞くようになってきた。僕が聞いたのは、rebuild.fmでその単語が出てきたときだったが、何故出演者がFacebookも引き合いに出して、怒りを感じているのかがわからなかったので少し調べてみた。もちろん、足りない視点などあるとは思うので、見つけたらこっそり教えて欲しい。

日本語でフェイクニュースや偽ニュースと言うと、虚構新聞のことか、とかマスメディアが嘘ついてるんでしょ、みたいなイメージがパッと思い浮かぶかもしれない。（ちなみに、DMM英会話で話をしているセルビアの人にも話を振ったら「ニュースは総じてfake newsである」みたいなことを言っていたので、そういう人は一定数いるのだとは思う）つい最近、NHKのニュースでBBCがフェイクニュースを検証するという記事が流れたが、ファクトチェックをするのは良いことだ、という程度のはてブを見ても反応しか見受けられなかった。

[**英ＢＢＣがフェイク・ニュースを検証 | NHKニュース**  
_事実ではないことを記事の形式で発信するにせのニュース「フェイク・ニュース」がインターネット上で広がっていることを受けてイギリスの公共放送ＢＢ…_www3.nhk.or.jp](http://www3.nhk.or.jp/news/html/20170114/k10010839281000.html "http://www3.nhk.or.jp/news/html/20170114/k10010839281000.html")[](http://www3.nhk.or.jp/news/html/20170114/k10010839281000.html)

確かに、アメリカの大統領選ではテレビ討論でもファクトチェックをリアルタイムでするなど、事実確認にはかなり厳格に行っているように見える。

しかし、なぜ今更ファクトチェックの話をBBCが言うのだろうか？なぜ、fake newsが問題視されているのだろうか？確かに、ニュースとしてアメリカの選挙にロシアがfake newsを通じて干渉していた、という話は聞くがどのようなことが問題なのだろうか。ロシアのアメリカ大統領選への干渉は以下のコラムがわかりやすくまとまっているので、ご存じない方は一読すると良いだろう。

[**暴露が続くアメリカ政治――ロシアが仕掛ける「情報攻撃」**  
_Sergei Karpukhin-REUTERS ＜近年、軍を動かすと同時に「情報攻撃」を展開するロシアの「ハイブリッド戦争」が注目されていた。アメリカ大統領選挙にともなうさまざまな「暴露」は、プーチンにとって「反撃」だった...＞ .…_www.newsweekjapan.jp](http://www.newsweekjapan.jp/tsuchiya/2017/01/post-19.php "http://www.newsweekjapan.jp/tsuchiya/2017/01/post-19.php")[](http://www.newsweekjapan.jp/tsuchiya/2017/01/post-19.php)

#### プロパガンダを攻撃とするハッカーグループ

実は、ドイツもロシアからのfake newsを中心とした攻撃に頭を抱えている。

[**ハッカー集団「APT 28」がドイツに対する「情報戦争」を拡大 |**  
_ドイツの情報機関によれば、APT 28グループ（別名：Fancy Bear）が、ドイツおよび西側諸国に対する「情報戦争」を強化しているという。…_the01.jp](https://the01.jp/p0004005/ "https://the01.jp/p0004005/")[](https://the01.jp/p0004005/)

このSecurity Affairsの記事によると、ドイツの外交情報機関（BND、連邦情報局）のブルーノ・カール長官はこう言っている。

> 「（国民の間に）『政治不信の感情を作り出すことだけを目的として行われるサイバー攻撃』の存在も報告されている。これらは公の発言に対する、そして民主主義に対する一種の圧力であり、受け入れられないものだ」とカール長官は『南ドイツ新聞』に語った。

いわゆる、プロパガンダというものは第二次世界大戦のときの新聞などを使った情報統制などをイメージしていた。しかし、現代においてfake newsを他国を攻撃するための武器として使われているのである。

記事によると、これらはAPT28というロシアのハッカーグループが中心となって行なっているというのである。政治的なダメージを与えるために機密文書を盗み、それをばらまくというのである。（この「ばらまく」というのにも問題があるがそれは後ほど説明する）本文中ではドイツがロシア政府は直接指示している証拠はつかめていないが、容認している根拠は示せると言っている。つまり、プロパガンダを中心とした政治への干渉を目的としたハッカーグループが存在しているということである。

> [ソーシャルメディア](http://securityaffairs.co/wordpress/14436/intelligence/us-af-notice-military-use-social-media.html)は新しい戦場となりつつある。BfVは「[PSYOP](http://securityaffairs.co/wordpress/52322/hacking/us-threatens-kremlin.html)（心理戦による軍事行動）の一環として行われるプロパガンダ活動」の急増を観察しており、また「ドイツの政党、および議会を標的としたフィッシング攻撃」の数が跳ね上がっていることを指摘した。

という指摘もあり、ただの経済的なダメージを与えるフィッシング攻撃やDDoS、クラッキングといった攻撃から、国に対しての攻撃を目的とした攻撃に切り替わっていることが伺える。

#### ソーシャルメディアとfake newsの親和性

特にここで指摘されている「ソーシャルメディア」というのが厄介で、何故”Fakebook”などという指摘を受けているのか。

[**ネットに広がる「フェイク・ニュース」― 嘘と真実の見分け方とは**  
_「フェイク・ニュース」という言葉をよく聞くようになりました。 先の米大統領選挙では、フェイク（嘘）のニュースが広がったためにクリントン民主党候補が敗れ、トランプ共和党候補が勝ったとも言われました。 【参考記事】 トランプを大統領にした…_www.newsweekjapan.jp](http://www.newsweekjapan.jp/stories/world/2016/12/post-6474.php "http://www.newsweekjapan.jp/stories/world/2016/12/post-6474.php")[](http://www.newsweekjapan.jp/stories/world/2016/12/post-6474.php)

ニューズウィークジャパンの記事によると、

> 一連の嘘のニュースは米国の主要ニュース・サイトに掲載されたニュースよりもフェイスブックでのシェア数が多かったという調査結果が出ています。

米国のニュースサイトよりもFacebookの影響が大きかったことが指摘されている。

また、東洋経済の記事によれば、

[**ロシアによる｢米大統領選干渉｣がマズい理由 | アメリカ**  
_2017年1月20日、ドナルド・トランプが第45代米大統領に就任する。トランプ大統領選出は予想を覆す結果で…_toyokeizai.net](http://toyokeizai.net/articles/-/149930 "http://toyokeizai.net/articles/-/149930")[](http://toyokeizai.net/articles/-/149930)

> ロシア政府はまた、クリントンに関する捏造された「ウソの情報」を拡散した。たとえば、同氏が「パーキンソン病を患っているという事実を隠している」、あるいは、「ローマ法王がトランプ支持を公言した」など、事実とは異なる情報を、フェイスブックやツイッターなどSNSを通じて広く拡散した。

とあり、SNSを通じた嘘の情報を流しているという話である。これだけを見ると、「こんなデマに自分は騙されない」と思ってしまうかもしれない。（少なくとも自分は最初に聞いた時にそう思った）

しかし、Facebookを通じたニュースには別の問題も指摘されている。Tech CrunchはFacebookのInstant Articlesの二次効果について指摘している。Instant Articleは[ニュースなどの記事をサクサクみるために、Facebookがシンプルなデザインで配信してアプリ内で見られるというものだ。](http://wired.jp/2015/05/20/instant-articles-facebook/)

[**Facebook previews journalism features like digests and subscription trials**  
_Between fake news and publishers struggling to keep a loyal connection to their readers, Facebook’s relationship with…_techcrunch.com](https://techcrunch.com/2017/01/11/facebook-journalism-project/ "https://techcrunch.com/2017/01/11/facebook-journalism-project/")[](https://techcrunch.com/2017/01/11/facebook-journalism-project/)

> But the hidden, second-order effect was that publishers had their identities sterilized. Instead of people reading on their websites with their custom branding, unique visual style and heavy promotion of their other stories, the Facebook-hosted Instant Articles from different outlets looked largely identical.  
> （筆者抄訳）  
> しかし、隠された2次効果は、出版社がアイデンティティを無菌化したということだった。 出版社のカスタムブランド、ユニークなビジュアルスタイル、そして他の関連ストーリーの重い宣伝が付いたウェブサイトの代わりに、FacebookがホストしているInstant Articlesは様々な出版社の記事がそっくりな見た目になった。

{{< figure src="1__XlSdHvipcZOOpYGLAPD28A.png" title="Instant Articlesの例（画像は[公式blog](https://media.fb.com/2016/04/12/instant-articles-now-open/)から）" >}}
Instant Articlesの例（画像は[公式blog](https://media.fb.com/2016/04/12/instant-articles-now-open/)から）

確かに、一番左の画像を見てもらうとわかるが、情報源がどこかがわかりにくい。右二つの開いたあとの記事も、ロゴなどはできるだけ少なくなるようになっている。Facebookのアプリからニュースを見る比率が高くなると、ソースを意識的に気にしないと、どこのニュースか見失ってしまいやすいのも頷ける。

対象的に、Googleも似たような目的で検索結果から高速に記事を見ることができるAMPでは、配信元が大きく出るようになっており、比較的誤解はしづらいデザインとなっているようにうつる。

{{< figure src="1__Y68oZLKS9EO43X7hV3gR__g.png" title="GoogleのAMPの例（画像は[公式ブログ](https://japan.googleblog.com/2016/02/blog-post_25.html)から）" >}}
GoogleのAMPの例（画像は[公式ブログ](https://japan.googleblog.com/2016/02/blog-post_25.html)から）

加えて、FacebookなどのSNSを通じたニュースを、何度も同じタイトルを見るうちに自分の頭のなかに刷り込まれて、興味を持って開いてしまうという経験はないだろうか。僕自身は複数回見たら「そろそろ読むかな」という気になることが多い。一度見たものや聞いた音楽は、二回目以降に出会うと親近感が湧くのと似ているかもしれない。

ソーシャルメディアからの記事を読むことは避けるのは難しいし、そこに紛れてるfake newsを避けるのは困難だ。信頼のおける友人がシェアしていたり、意見を表明して議論が盛り上がっていると、あたかもその記事の内容は（間違っていたとしても）真実かのように思えてくるときがある。

昔はSNSを通じたニュースを見るときも、大学の先生だからロジカルに裏取りしているだろうとか考えていた時期もあった。が、結局3.11の後にわかったのは、専門外の話は話半分で聞かないといけない、権威などというものはあてにはできないということだと思っている。

#### プロパガンダに利用されるWikiLeaks

では、Facebookのニュースの供給源である、新聞などのメディアはどうだろうか。先程の東洋経済の記事によると、

> ロシアが民主党だけでなく、共和党のメールシステムもハッキングしていたとCIAが報告したことだ。つまり、ロシアはウィキリークスを使って民主党のメールを拡散したものの、共和党のメールは拡散しなかったということ。

とあり、スノーデン事件のときのように、大きな国家の不正を暴く存在という印象づけられていたWikiLeaksが、今度はリークする情報をコントロールすることで他国を攻撃するツールになっているのである。ジャーナリストがメディア側も些細な事だからと論旨が覆る話をサラリと流したりすることもあるため、バイアスが係ることは否めない。正しさハラスメント問題を使われた時にも受けてがなんとかしないといけないとは思っていたが、それ以前に情報源が操作されていたり印象が操作されているということが起こりうる時代なのである。

だからといって、すべての記事にファクトチェックをしていられるほど人生は無限にはない。情報ができる速度のほうが人がファクトチェックする速度より速いのだ。だから、冒頭の記事のようにBBCがファクトチェックを行うと宣言したのであり、[ドイツは500人体制でファクトチェックをする部門を設立した](http://www.smh.com.au/world/germany-probes-russian-fake-news-campaigns-in-leadup-to-elections-20170109-gtolqr.html)のである。Facebookも[外部の協力者と共にファクトチェックを行うと宣言](http://jp.techcrunch.com/2016/12/16/20161215facebook-now-flags-and-down-ranks-fake-news-with-help-from-outside-fact-checkers/)している。

#### ソフトウェアエンジニアとしてできることは？

しかし、人手では限界があるだろう。[NICTが災害時のデマを可視化する研究](https://www.nict.go.jp/press/2014/11/05-1.html)をしていたりもするが、残念ながら多くの人が本当と思わされてしまったことを全自動でfakeやプロパガンダと判定するのは、WELQのようにクラウドソースされた怪しい記事を、Googleは残念ながら自動で弾くことはできなかったように、まだ難しいと個人的には思う。

[嘘言を言った少女のために外交関係が悪化したドイツとロシア](http://www.cnn.co.jp/world/35077204.html)や、[fake newsを信じて核攻撃を示唆したパキスタン国防省](http://www.asahi.com/articles/ASJDX6F2NJDXUHBI02X.html)のように、fake newsはまぬけな対岸の火事ではなく、サイバー攻撃として仕組まれているものの一つであるという可能性を疑って見たほうが良いと、一エンジニアとして思う。

ちょっと昔だと、陰謀論乙、と思っていたのだが、いかんせん[ロシアの干渉をアメリカの情報機関が断定](http://www.newsweekjapan.jp/tsuchiya/2017/01/post-19.php)してから、雲行きが怪しくなってきた。

一エンジニアとして、今後どういう情報による攻撃が起こり得て、それをどうすれば防げるのか、というのは、興味深くもあるが、それを防ぐというのはかなり難しそうな気がしている。おそらく、機械学習や[強いAI](https://ja.wikipedia.org/wiki/%E5%BC%B7%E3%81%84AI%E3%81%A8%E5%BC%B1%E3%81%84AI)が解決の糸口につながるとは思うが、まだまだギャップは大きいように思う。

「[新しい戦前](http://p-shirokuma.hatenadiary.com/entry/20170115/1484440590)」という言葉が、杞憂で終わるように、できることを考え続けていきたい。選挙期間の選挙に関するネット上の発言は禁止されるという、馬鹿みたいな昔に戻るというディストピアだけは避けたい。
