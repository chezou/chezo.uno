---
title: 非英語ネイティブにとってのOSSのメンテナンスコスト
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2017-01-01 23:29:31+00:00
lastmod: 2017-01-01 23:29:31+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [oss, issue, 丸山, コード, 英語, 開発, メンテナンス, ネイティブ, プロダクト, codelunch]
recommendations: [/post/2016-03-30-zhuan-zhi-simasita/, /post/2016-12-21-number-eigo-tosi-aruihazi-chi-tinoye-wu-wai-huo-dong-nosok-kefang/,
  /post/2018-06-19_goodbye-cloudera/]
---
_disclaimer: この記事を書いている人はClouderaというHadoop/Sparkのディストリビューターの会社にいます。_

codelunch.fmの20回目を聞いていろいろ思うところがあったのでつらつら買いてみます。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fcodelunch.fm%2F20%2F" title="CodeLunch.fm" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://codelunch.fm/20/">codelunch.fm</a></cite>

この回のcodelunch.fmでは、前職の同僚である丸山さん（[@h13i32maru](https://twitter.com/h13i32maru)）と[@hokaccha](https://twitter.com/hokaccha)さんが、お互いの家庭環境の変化を交えながら個人プロダクトの開発について話しているエピソードです。これ自体なかなかおもしろい回なので、趣味でプロダクト開発している人は聞いてみるといいんじゃないかなと思います。

丸山さんは[Jasper](https://jasperapp.io/)や[ESDoc](https://esdoc.org/)を精力的に開発していますし、hokacchaさんは[nodebrew](https://github.com/hokaccha/nodebrew)や[adventar](http://www.adventar.org/)を作られています。彼らの話していた、個人で趣味プロダクトを開発するモチベーションは何かというところは、以下のようなことが話されていました。

- 自分が欲しいと思ったものを作りたい
- 他にも同じ問題で困っている人を自分のプロダクトで助けたい
- 新しい技術を試したい
- あわよくば、自分の作ったプロダクトで有名になりたい（承認欲求を満たしたい）

どれも同じエンジニアとしてはそうだよねという気持ちになります。

そんな丸山さんのESDoc関連の発言を見ていると、アクティブじゃないから他のにマージしろとかなかなか悩ましいなぁと見ていて思います。

{{< x user="h13i32maru" id="813322023690588160" >}}

本質的にはgithubのissueが辛いだけかもしれませんが(丸山さん自身も[ポジティブフィードバックを得にくいのが辛い](https://twitter.com/h13i32maru/status/814693960866144256)と言っている)、スターが1000を超える程度の人気のプロダクトは色々な人のアテンションを引くため、言葉を選ばず言うと「乱暴な」issueが立ちやすいのかもしれません。[^1]ですが、自分もスター19くらいの[tabula-py](https://github.com/chezou/tabula-py)というbindingも本家に拾われてからいろいろissueが来るようになりました。

OSSを出すパターンとしては、ざっと考えた限りでは以下のようなパターンがあるんじゃないかと考えます。カッコ内はその目的です。

- 誰も作っていない欲しいものがないから作ってOSS化する（自分をユーザとして満足させる、承認欲求を満たす）
- 会社で書いていたコードのうち、一部を汎用的に切り出してOSS化する（同じ問題を解いている他の人を楽にする、会社の認知を上げる、転職後もコードを使えるようにする）
- 会社として、大きいコードを戦略的にOSS化する（他社との差別化、プロダクト自体の認知を広める）

下に行けば行くほど、メンテナンスする人数も増えていくと思います。ここで、OSSのメンテナンスコストという点について考えたいと思います。というのも、個人ですべてOSSとしてメンテしていくときにこういうのをどう処理すればいいのかな、と考えたのがきっかけでした。

{{< x user="h13i32maru" id="814657477417443328" >}}

前職のクックパッドに入る前は、OSSに対する考えとしては、ソースコードは公開されており、コントリビュートの機会が開かれている素晴らしいものだと素朴に思っていました。RubyやSolrにお世話になり、自分もC++のコードの小さいbindingを書いたりしていました。

クックパッドに入った後は、社内でも使っているし社外にも使えるものはOSSとして公開しようという流れでOSSを出しているのを見てきました。業務として使うコードを公開することでユーザが増え、コードのクオリティが上がり会社の認知も増えるという効果も得ることができていた様に感じます。 ある意味では、その企業が業務としてのOSS活動をサポートしているからできることだとも思います。プロダクトにもよりますが、1人ないしは数人で開発をしているという開発状況になると思います。

Clouderaに入って、HadoopやSparkといった巨大なOSSは一社ではとてもじゃないけれどすべてをこなすことが出来ないものであるという認識になりました。 良くも悪くも複数の企業や[ASF](https://www.apache.org/)などのファウンデーションでメンテすることで、そのコードを長く使えるようにしているものだということを学んだのです。 OSSコミュニティとして他社と共同開発をしながら、一方でビジネスでは競争をしているという形になります。当然、個人や一社で開発するより圧倒的にフルタイムの開発人数は多くなります。

では、継続的に個人の趣味コードをOSSとしてメンテナンスしていく上での、メンテナンスコストはなんでしょうか？

一つの要素としては、先程から書いているように開発リソースの問題です。

開発者の時間は有限ですし、ユーザーが増える速度はコントリビュータが増える速度より速いです。 ESDocに関しては[organizationに一人しかいない](https://github.com/orgs/esdoc/people)のもさばく負荷が高い理由になるでしょう。 コミットしてくれる人を集めたり、issueを消化してくれるメンテナを集めたりして[優しい終身の独裁者](https://ja.wikipedia.org/wiki/%E5%84%AA%E3%81%97%E3%81%84%E7%B5%82%E8%BA%AB%E3%81%AE%E7%8B%AC%E8%A3%81%E8%80%85)として動くのもありかもしれませんが、個人として自由な裁量を持った開発をしたいという人もいるでしょう。 こうした中でどのように、増え続けるissueと戦うべきか、というのは難しい問題です。 なお、このあたりの話は、Sphinxメンテナのtk0miyaさんの記事とFreeBSDのPort maintainerのjj1bdxさんの記事が興味深かったです。

<iframe src="https://tk0miya.hatenablog.com/embed/2016/12/25/224306" title="Sphinx のメンテナになって一年が経過した話 - Hack like a rolling stone" class="embed-card embed-blogcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://tk0miya.hatenablog.com/entry/2016/12/25/224306">tk0miya.hatenablog.com</a></cite>

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fjj1bdx%2Fitems%2Fa9cd77807e0d689fb4b6" title="ほころびていくコミュニティとなかなかできない世代交代、そしてさよならアドベントカレンダー - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://qiita.com/jj1bdx/items/a9cd77807e0d689fb4b6">qiita.com</a></cite>

もう一つの要素としては、英語に困らない人にはノンネイティブの辛さが想像できない問題というのもあると思います。

自分のボスは、ネイティブと議論するときと英語が得意でないノンネイティブが混ざるときで、話すスピードもそうですが使う語彙を変えて話してくれます。 しかし、githubのissueなどpublicな場所ではこうした気を使ってくれる人は（自分の体感としては）珍しく、こちらが気合を入れて英語を読んだり書いたりする必要があります。 丸山さんとも昔話しましたが、issueの返信だと「この解釈で本当に良いんだろうか」とウンウンうなるときも少なくなく、スラングに苦しめられる時も多いです。[^2]All Ears Englishでも、「アメリカ人はノンネイティブの英語に慣れていないから、崩れた英語から汲み取ることができない」という話もありましたし、ここは結局ノンネイティブが頑張るしかないのですが、ネイティブにもここらへん認識してもらう方法はないものか、とも思います。

例えるなら、対面で話しができるスムーズさとメールでのみやりとりしかできないときの負荷のギャップが、ネイティブ同士のやりとりとノンネイティブがネイティブとやりとりするギャップに相当するんじゃないかなと思います。

もちろん、PR貰ってコードでやり取りするのはやりやすいですが、GithubでOSS活動をするということはそれだけでは済みません。 僕自身も英語で問い合わせメールが来てissueで辛いやり取りをして以来、最近はそういうコストをどうしたら抑えることができるかということを考えています。 ユーザーを拡大したければ英語でマーケティングをするのも大事になってきますし、英語圏の開発をしてくれるファンを増やせればもっと楽になるのかもしれませんが...。[^3]

とりとめもなくまとまりもないですが、他の人はどう考えて立ち向かっているのか教えてもらえるとうれしいです。

[^1]: もしかすると、彼のアピールの仕方が「他より良い」という点で攻めているので面倒なissueが立ちやすい可能性もあります

[^2]: [urban dictionary](http://www.urbandictionary.com/)がないと死にそうになります

[^3]: Issue templateやFAQである程度は対処できるとは思いますが決定打にはかけるなとも思います
