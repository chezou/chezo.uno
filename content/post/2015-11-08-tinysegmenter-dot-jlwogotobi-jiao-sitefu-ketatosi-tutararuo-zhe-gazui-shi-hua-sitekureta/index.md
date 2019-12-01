---
title: "TinySegmenter.jlをGoと比較して負けたと思ったら若者が最適化してくれた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-11-08T19:00:00+00:00
lastmod: 2015-11-08T19:00:00+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
先日、[TinySegmenter.jlの話](http://chezou.hatenablog.com/entry/2015/10/21/234317)を書いたら各方面から反響を頂きました。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Frepeatedly.github.io%2Fja%2F2015%2F10%2Ftinysegmenter-benchmark-and-d%2F&quot; title=&quot;TinySegmenterのベンチマーク + D言語版 - Go ahead!&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://repeatedly.github.io/ja/2015/10/tinysegmenter-benchmark-and-d/&quot;&gt;repeatedly.github.io&lt;/a&gt;&lt;/cite&gt;

[http://woxtu.tumblr.com/post/132337169740/rust-tinysegmenter](http://woxtu.tumblr.com/post/132337169740/rust-tinysegmenter)
&lt;script async src=&quot;https://secure.assets.tumblr.com/post.js&quot;&gt;&lt;/script&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://woxtu.tumblr.com/post/132337169740/rust-tinysegmenter&quot;&gt;woxtu.tumblr.com&lt;/a&gt;&lt;/cite&gt;

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fikasamt%2Fitems%2F471bfae96ce590a4fe82&quot; title=&quot;ベンチマーク - TinySegmenterをCrystalで書いてみた。雑だけど。 - Qiita&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://qiita.com/ikasamt/items/471bfae96ce590a4fe82&quot;&gt;qiita.com&lt;/a&gt;&lt;/cite&gt;

そんな中で、ikawahaさんがGoでも同様の最適化を実装していました。

&lt;iframe src=&quot;http://ikawaha.hateblo.jp/embed/2015/10/23/161351&quot; title=&quot;TinySegmenter.jl の高速化手法を追っかけてみた - 押してダメならふて寝しろ&quot; class=&quot;embed-card embed-blogcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://ikawaha.hateblo.jp/entry/2015/10/23/161351&quot;&gt;ikawaha.hateblo.jp&lt;/a&gt;&lt;/cite&gt;

それと比較するために、とりあえず[Julia templateをPR](https://github.com/shogo82148/TinySegmenterMaker/pull/10)して比較しました。

![](/img/2015/11/08/190000/20151108175610.png)

| Ruby | Perl | Python | Node.js | C++ | Go | Julia | Julia (hash optimized) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 132.98 | 134 | 111.85 | 105.31 | 48 | 10.50 | 11.70 | 10.35 |

実はTinySegmenterMakerのshogo82148さんが一部のhashのkeyをordしたIntで表現するというさらなる最適化を進めていたので、 ちょっと負けてしまったのですがJuliaのDictを生成するときのhash計算が遅いということを[bicycle1885さんが特定してくれた](https://gist.github.com/bicycle1885/918a0fee5dbb3d68f05a)ので、Julia本体の最適化が進めば同じくらいにはなりそうだね、ということがわかりました(表のhash optimized)。

ちなみに、SGJ先生は「実は言語間の比較ではなくて最適化の比較になっていたんだけどね（てへぺろ）」[みたいなこと](https://github.com/chezou/TinySegmenter.jl/issues/8#issuecomment-154558591)を告白しており、ikawahaさんの目の付け所は正しかったようです。

そういう意味では、Stringとしても処理できるし頑張れば最適化できるJuliaは楽しいですね、という気持ちになりました。今時のコンパイル型の言語だと突き詰めれば似たような性能になるんでしょうね。


