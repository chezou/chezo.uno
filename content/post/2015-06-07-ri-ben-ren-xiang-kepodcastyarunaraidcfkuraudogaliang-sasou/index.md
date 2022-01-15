---
title: 日本人向けPodcastやるならIDCFクラウドが良さそう
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2015-06-07 21:00:00+00:00
lastmod: 2015-06-07 21:00:00+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [録音, 無料, 転送, skype, クラウド, gb, ストレージ, tb, ゲスト, 調整]
recommendations: [/post/2015-11-22-idcfkuraudono500yuan-sabadepodcast-serverwohazimete8keyue-gajing-timasita/,
  /post/2015-02-20-number-ingress-nopodcast-shui-yaritong-xin-woshi-memasita-number-mizuyari/,
  /post/2015-02-14-garagebanddeskypetomaikunoyin-wobie-toratukudelu-yin-surufang-fa/]
---
[rubyist.club](http://rubyist.club/)というpodcastをやっているのですが、[IDCFクラウド](http://www.idcf.jp/cloud/)の上で動いています。

# tl;dr

- IDCFクラウド月500円で3TBまで転送量無料なので、国内向けPodcastには便利

# いいところ

安いこと。 IDCFクラウドは、一番小さいインスタンスなら月500円で使えて月3TBまで転送量が無料です。\*1ただし、この構成だと15GBのボリュームしか使えませんが、まぁpodcastのデータはたかが知れているので大丈夫でしょう。 Mackerelも無料で制限されたプランがついてきます。

あと、ちょいちょい3000円クーポンを配る[キャンペーンを](http://www.idcf.jp/cloud/cp/?cl=co_t01) [している](http://www.idcf.jp/topics/20150515001.html) ので、試しに始めるのは気軽にできます。

# わるいところ

料金体系がわかりにくいところです。AWSもたいがいなんだと思いますが、IDCFクラウドもよくわからないです。

僕がハマったのは、オブジェクトストレージ(S3 compatibleなストレージ)。 こちらは50GB未満の保存料は無料だけど、転送量は月10GBまでしか無料でなくて、Matzに宣伝していただいたrubyist.clubはあっさり超えたので辞めました。

また、[定期スナップショット](http://www.idcf.jp/cloud/faq/sna_042.html)も厄介で、とろうと思った時にいくら掛かるのかパッとわからないし、シミュレータではスナップショットの「ス」の字も書いてない。おそらくアーカイブデータなのはわかるけど、この不親切さはちと厳しい。

IDCF自体の障害はちょこちょこ発生しているようですが、今のところCDNも経由してるしなんとかなっています。

# 録音環境

ついでですが、以前にも少し[書きました](https://chezou.hatenablog.com/entry/2015/02/14/235008)が、ソフトウェア構成が変わったので書きます。

- Skype
  - [Ecamm Call recorder for skype](http://www.ecamm.com/mac/callrecorder/)でバックアップ用に会話を録音
- GarageBand
  - 自分の声の録音および、領域のカット
- [Audacity](http://sourceforge.net/projects/audacity/)
  - [compressor用plugin](http://theaudacitytopodcast.com/tap005-my-secret-audacity-recipe-for-great-audio/)で音量調整をしてる
  - yusukebeさんはlevelatorで調整しているみたいですが、こちらの方がより自分で調整できるので気に入っています

以前書いたsoundflowerは、クロックが狂う原因になることがわかったので使用をやめています。

ゲストの環境の典型的なパターンは

- iPhoneで口元で録音
  - [PCM録音Lite](http://www.teach-me.biz/iphone/app/bn/pcm-lite.html)みたいなアプリでwav形式で録音をしてもらう
- Mac/iPadなどでSkype

という構成にしてもらっています。これは、口の近くでiPhoneを置いて録音することで、ゲインが稼げてかつ音量も安定するからです。 結構キーボード叩く音とか入っちゃうんですけどね...\*2。指向性のマイクを持っていない人がゲストのことが多いので、こういう方法でアプローチしています。

\*1:たしか、rebuild.fmは[linode](https://www.linode.com/pricing)使ってて2~3TB無料なので、それくらいなら大丈夫かと踏んでいる

\*2:🐸の声も入ってしまった


