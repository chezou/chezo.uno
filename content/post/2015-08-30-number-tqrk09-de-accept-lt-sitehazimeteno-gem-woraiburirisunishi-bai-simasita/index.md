---
authors: [aki]
categories: null
date: '2015-08-30 14:10:51-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2015-08-30 14:10:51-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: '#tqrk09 で Accept LT してはじめての Gem をライブリリースに失敗しました'
keywords: [tag, tags, surface, kytea, '100.0', 名詞, 語尾, 天気, str, working]
recommendations: [/post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/,
  /post/2011-09-23-kyteawota-yan-yu-deshi-uratupa-plus-amatome/, /post/2011-09-14-nltkkarakyteadekopasuwodu-miip-mujpkyteatokenizerzuo-rimasita/]
---

Tokyu Ruby Kaigi 09 でAccept LTのトリで話しました。 3分だってのに盛りすぎ、かつDEMOで接続が悪くなるという前回もあった失敗を重ねてはじめてのGemをライブリリースすることに失敗しました。

なお、カリーヴルストは無事リリースできました。

<iframe src="//instagram.com/p/68wonPAdwS/embed/" data-entry-image="http://instagram.com/p/68wonPAdwS/media/?size=l" width="612" height="710" frameborder="0" scrolling="no" allowtransparency="true"></iframe><cite class="hatena-citation"><a href="https://instagram.com/p/68wonPAdwS/">instagram.com</a></cite>

レシピはクックパッドって便利なサイトを使いました。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fcookpad.com%2Frecipe%2F3131580" title="簡単★カリーヴルスト by エスビー食品" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="http://cookpad.com/recipe/3131580">簡単★カリーヴルスト by エスビー食品</a></iframe><cite class="hatena-citation"><a href="http://cookpad.com/recipe/3131580">cookpad.com</a></cite>

その後、きちんとリリースしたので今では Macをお使いのあなたなら、

    brew install kytea gem install kytea

で kyteaがRubyから使えるようになります！

[kytea | RubyGems.org | your community gem host](https://rubygems.org/gems/kytea)

kyteaはどんな子かというと、 三期も放送されているという「Working」に対してきちんと読み推定をしてくれる優秀な形態素解析です。

    $ echo Working | mecab Working 名詞,固有名詞,組織,\*,\*,\*,\* EOS $ echo Working | kytea Working/名詞/わーきんぐ

YAPCの間使って頑張ってSWIGの挙動を調べた結果、Ruby側で更なるwrapperを書くという屈辱を味わっていますが、 おかげで、ぼちぼちな使い方ができるようになったのでよしとしています。

    str = "今日はいい天気です。"kytea.segment(str)#=\> ["今日", "は", "い", "い", "天気", "で", "す", "。"]kytea.tag\_info\_of(str)#=\> "今日/名詞/きょう は/助詞/は い/形容詞/い い/語尾/い 天気/名詞/てんき で/助動詞/で す/語尾/す 。/補助記号/。 "kytea.tags\_of(str)#=\> [{:surface=\>"今日", :tags=\>[[{:tag=\>"名詞", :val=\>3.610404674503611}], [{:tag=\>"きょう", :val=\>1.0726515803715995}]]},# {:surface=\>"は", :tags=\>[[{:tag=\>"助詞", :val=\>3.5500698037485963}], [{:tag=\>"は", :val=\>100.0}]]},# {:surface=\>"い", :tags=\>[[{:tag=\>"形容詞", :val=\>2.5966088884369523}], [{:tag=\>"い", :val=\>100.0}]]},# {:surface=\>"い", :tags=\>[[{:tag=\>"語尾", :val=\>2.7064013574728385}], [{:tag=\>"い", :val=\>100.0}]]},# {:surface=\>"天気", :tags=\>[[{:tag=\>"名詞", :val=\>4.220721634732509}], [{:tag=\>"てんき", :val=\>100.0}]]},# {:surface=\>"で", :tags=\>[[{:tag=\>"助動詞", :val=\>2.9093304720685786}], [{:tag=\>"で", :val=\>0.99994530321086}]]},# {:surface=\>"す", :tags=\>[[{:tag=\>"語尾", :val=\>2.5160490891753264}], [{:tag=\>"す", :val=\>0.9998735552127426}]]},# {:surface=\>"。", :tags=\>[[{:tag=\>"補助記号", :val=\>3.070959942739055}], [{:tag=\>"。", :val=\>100.0}]]}]

ブログを書いて、サントリーさんの応募ハガキを投函するまでがTokyu Ruby Kaigiなので、エンドレスTokyuにならないよう頑張ります！