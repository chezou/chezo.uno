---
title: "#tqrk09 で Accept LT してはじめての Gem をライブリリースに失敗しました"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-08-30T21:10:51+00:00
lastmod: 2015-08-30T21:10:51+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
Tokyu Ruby Kaigi 09 でAccept LTのトリで話しました。 3分だってのに盛りすぎ、かつDEMOで接続が悪くなるという前回もあった失敗を重ねてはじめてのGemをライブリリースすることに失敗しました。

なお、カリーヴルストは無事リリースできました。

&lt;iframe src=&quot;//instagram.com/p/68wonPAdwS/embed/&quot; data-entry-image=&quot;http://instagram.com/p/68wonPAdwS/media/?size=l&quot; width=&quot;612&quot; height=&quot;710&quot; frameborder=&quot;0&quot; scrolling=&quot;no&quot; allowtransparency=&quot;true&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://instagram.com/p/68wonPAdwS/&quot;&gt;instagram.com&lt;/a&gt;&lt;/cite&gt;

レシピはクックパッドって便利なサイトを使いました。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fcookpad.com%2Frecipe%2F3131580&quot; title=&quot;簡単★カリーヴルスト by エスビー食品&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;a href=&quot;http://cookpad.com/recipe/3131580&quot;&gt;簡単★カリーヴルスト by エスビー食品&lt;/a&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://cookpad.com/recipe/3131580&quot;&gt;cookpad.com&lt;/a&gt;&lt;/cite&gt;

その後、きちんとリリースしたので今では Macをお使いのあなたなら、

    brew install kytea gem install kytea

で kyteaがRubyから使えるようになります！

[kytea | RubyGems.org | your community gem host](https://rubygems.org/gems/kytea)

kyteaはどんな子かというと、 三期も放送されているという「Working」に対してきちんと読み推定をしてくれる優秀な形態素解析です。

    $ echo Working | mecab Working 名詞,固有名詞,組織,\*,\*,\*,\* EOS $ echo Working | kytea Working/名詞/わーきんぐ

YAPCの間使って頑張ってSWIGの挙動を調べた結果、Ruby側で更なるwrapperを書くという屈辱を味わっていますが、 おかげで、ぼちぼちな使い方ができるようになったのでよしとしています。

    str = &quot;今日はいい天気です。&quot;kytea.segment(str)#=\&gt; [&quot;今日&quot;, &quot;は&quot;, &quot;い&quot;, &quot;い&quot;, &quot;天気&quot;, &quot;で&quot;, &quot;す&quot;, &quot;。&quot;]kytea.tag\_info\_of(str)#=\&gt; &quot;今日/名詞/きょう は/助詞/は い/形容詞/い い/語尾/い 天気/名詞/てんき で/助動詞/で す/語尾/す 。/補助記号/。 &quot;kytea.tags\_of(str)#=\&gt; [{:surface=\&gt;&quot;今日&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;名詞&quot;, :val=\&gt;3.610404674503611}], [{:tag=\&gt;&quot;きょう&quot;, :val=\&gt;1.0726515803715995}]]},# {:surface=\&gt;&quot;は&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;助詞&quot;, :val=\&gt;3.5500698037485963}], [{:tag=\&gt;&quot;は&quot;, :val=\&gt;100.0}]]},# {:surface=\&gt;&quot;い&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;形容詞&quot;, :val=\&gt;2.5966088884369523}], [{:tag=\&gt;&quot;い&quot;, :val=\&gt;100.0}]]},# {:surface=\&gt;&quot;い&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;語尾&quot;, :val=\&gt;2.7064013574728385}], [{:tag=\&gt;&quot;い&quot;, :val=\&gt;100.0}]]},# {:surface=\&gt;&quot;天気&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;名詞&quot;, :val=\&gt;4.220721634732509}], [{:tag=\&gt;&quot;てんき&quot;, :val=\&gt;100.0}]]},# {:surface=\&gt;&quot;で&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;助動詞&quot;, :val=\&gt;2.9093304720685786}], [{:tag=\&gt;&quot;で&quot;, :val=\&gt;0.99994530321086}]]},# {:surface=\&gt;&quot;す&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;語尾&quot;, :val=\&gt;2.5160490891753264}], [{:tag=\&gt;&quot;す&quot;, :val=\&gt;0.9998735552127426}]]},# {:surface=\&gt;&quot;。&quot;, :tags=\&gt;[[{:tag=\&gt;&quot;補助記号&quot;, :val=\&gt;3.070959942739055}], [{:tag=\&gt;&quot;。&quot;, :val=\&gt;100.0}]]}]

ブログを書いて、サントリーさんの応募ハガキを投函するまでがTokyu Ruby Kaigiなので、エンドレスTokyuにならないよう頑張ります！


