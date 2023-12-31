---
title: 2023年を振り返って
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: [misc]
date: 2023-12-30 19:00:00-07:00
lastmod: 2023-12-30 19:00:00-07:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [vancouver, social, 仕事, プロジェクト, あと, コールセンター, cad, accent, 炎上, 投入]
recommendations: [/post/2021-12-18-8-months-after-relocating-vancouver/, /post/2022-12-30-2022-year-in-review/,
  /post/2023-04-05-first-time-skiing-in-25-years/]
---

今年もあと一日になりましたが、[昨年同様](https://chezo.uno/post/2022-12-30-2022-year-in-review/)一年を振り返っていきたいと思います。

## OSS活動・対外活動

ChromaというVector DBのOSSにコントリビュートしました。ChromaはRAGやLLMの文脈でよく使われるもののようです。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chroma-core/chroma/pull/1361" data-iframely-url="//iframely.net/Zj8hyr9?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

tabula-pyの裏側にjpype経由で使うようにして速くしたのですが、残念なことに Python 3.12 サポートがかなり時間がかかったので今はoptionalにしています。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/blog/2023-09-09-tabula-py-280/" data-iframely-url="//iframely.net/f64jYQx"></a></div></div><script async src="//iframely.net/embed.js"></script>


また、tabula-pyの質問はStackOverflowに流していたのですが、[moderatorの気分でGitHub issue作ってねという文言が消される](https://meta.stackoverflow.com/questions/426607/is-it-forbidden-to-suggest-to-create-an-github-issue-discussion-for-other-proble/426610)ということが分かったので、今までの感謝とともにGitHub Discussionsに移行しました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/tabula-py/discussions" data-iframely-url="//iframely.net/PIG05ED?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

<br/>

あとは、NotionをscrapingしてPDFにするやつなんかも作りました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/vangohan-pdf" data-iframely-url="//iframely.net/cP0eFmn?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

<br/>


RubyKaigi 2023にもただの参加者としてですが参加できたので、その様子をバンクーバーのえんじに屋podcastでお話させていただきました。

https://www.vancouver-engineers.com/133

また、Frogさんでキャリアのインタビューもしてもらいました。行き当たりばったりなキャリア経験ではありますが、きれいにまとめていただきました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://frogagent.com/interview/ariga/" data-iframely-url="//iframely.net/yH4K5NE?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

## 仕事

昨年炎上プロジェクトに投入されて火消しをするも、いろいろあってぽしゃり、そしてまた、別の炎上プロジェクトに投入されてそちらはなんとかかんとか生き延びている、という状況です。突っ込まれてから、4カ月後の社外カンファレンスでデモまでこぎつけられたのは、ML系プロジェクトだからだなぁという良い経験をさせていただきました。6 pageのレポート作成からのexecutiveの説得、UX設計、PRD議論、アーキテクチャ設計、実装、他のエンジニアリングチームのとりまとめとまあ全部やりました。

最近の悩みは、クオーターごとに実装期間がほぼ1週間くらいしかないことでしょうか。楽しい時間は一瞬で過ぎ去ってしまう。。。soft skillを生かして仕事では動いていますが、やはりhard skillも伸ばしておかないと上流だけしかできないのね、と言われてしまうのが怖いです。スタッフ+としてどう生きていくのがいいのだろうか。副業などで手を動かす仕事をやりたいものです。

社内ハッカソンで、RAG (retrieval augmented generation)のアプリを作りました。[terapyon podcastで聞いていたおかげで](https://podcast.terapyon.net/) [Gradio](https://www.gradio.app/)を使い、さくっとデモアプリまで行けました。なお、RAGは短文で検索するときの検索性能が全然でないため、OOBじゃ全然使えないということも学びました。しかし、検索と推薦は楽しいですねぇ。

## プライベート

PRカードをついに手に入れました。永住権自体は昨年末に得ていたのですが、物理カードを得たので、これでビザ的には一番安心できる状況ですし、海外旅行も行けます。あと、海外の会社で働くのも楽になりました。

スキーを20年ぶりに再開してドはまりしています。ujihisaさんと何度も滑りに行ってますがローカルの山まで30分、Whistlerまで2時間なので更に滑りまくりたいです。今年はエルニーニョ現象のため、雪が全然なくてつらいです。パラレルをちゃんとものにしていきたい。

あと、忘れもしないのは銀行のコールセンターに [accent discrimination](https://www.forbes.com/sites/janicegassam/2022/11/18/accent-discrimination-is-still-a-pervasive-issue-in-the-workplace-research-finds/?sh=46859d85697e) を受けたこと。Scotiabankという銀行を移住時に開設したのですが、全国一律のコールセンターの人に英語わからない認定を食らって[バトルしました](https://sizu.me/chezou/posts/a811we9eha27)。上司が出てきて謝罪をもらったんですが、そういう銀行を使うのは癪なので、TDに移行してすべてうまくいっています。1Passwordで自社名とconflictすることくらいがネックなだけです。なお、ショックだったのは、某日本人コミュニティで「あなたの考えすぎじゃないですか」というセカンドレイプを受けたことでした。 unconscious biasのトレーニングを会社で受けていてよかったなと思った瞬間です。

転んでもただは起きぬということで、[American English accentのレッスン](https://rachelsenglish.com/)を受けるようになりました。理屈より実践という感じの手法なのですが、なるほど実際そうするのねーというのが身についてきて、けだるい英語のリスニングができるようになった気がしています。

12月を丸っと休みにしたのですが、家族が次々と怪我をして看護休暇として追われています。ずっとワンオペで子供と犬の世話をしている日々なので、ゆっくりとした休みが欲しいなあと思う次第です。

## 振り返りと来年に向けて

今年は、いろいろと迷いの多い一年だったように思います。来年は40の大台に乗るので、仕事方面は人生で一回くらいプロモーションしていきたいなと思いますし、プライベートは英語とスキーを上達したいと思っています。

中長期的には、Greator Vancouverで家を買うには大体 1M CADが必要なのですが、その頭金として300K CADを貯めればいいことが分かったので、何とかしていきたいと思います。手っ取り早いのは、スタートアップで一発当てて$1M手に入れるか、big techに入って高給取りになることなんですが、まずは地道に貯めていこうかなと思います。

2年半バンクーバーエリアに住んでみてわかったのは、家賃上昇が激しく（Vancouver cityは2023年12月で[平均2BR $4300, 3BR $6200](https://www.zumper.com/rent-research/vancouver-bc)）living costはめちゃくちゃ高いわりに仕事があまりない（シニア以上はシアトルはじめUSに人が流れてしまうのが定番）という現状なんですが、医療費がかからない、スキーに行きやすいなどのメリットとの天秤でまだこの地にとどまることになると思います。が、平均年収$59Kの国で$100K超えの年収がないと一人暮らしできないVancouverやTrontoは異常なので、職があればAlbertaなどに行くのが良いんだろうなぁ。

Social media関連は色々と整理したり[^social]展開しなおしたりしたのですが、人と話すことで刺激を得たいと思っているので、Vancouver近辺にいらした際にはお声がけください。もちろん、近隣にお住いの皆さんは引き続きよろしくお願いいたします。

[^social]: 某toxicな持ち主のプラットフォームからは完全撤退しました
