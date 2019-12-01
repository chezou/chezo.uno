---
title: "MeCab.jlをJulia v0.4.0-rc2に対応した"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-09-23T02:16:08+00:00
lastmod: 2015-09-23T02:16:08+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
ついに、Julia v0.4.0-rc2が2015/9/19出ましたね！ Dictの`[:symbol =&gt; :value]`といったsyntax sugarがなくなったりして、自分が作っているMeCab.jlでも対応をしました。

詳細はPRを見ていただければと思いますが、[Compat.jl](https://github.com/JuliaLang/Compat.jl)を使えば基本OKです。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fchezou%2FMeCab.jl%2Fpull%2F8&quot; title=&quot;Suppress warnings on julia v0.4.0-rc2 by chezou · Pull Request #8 · chezou/MeCab.jl&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://github.com/chezou/MeCab.jl/pull/8&quot;&gt;github.com&lt;/a&gt;&lt;/cite&gt;

（PRボロボロだったのであとから修正を加えました...）

bicycle1885さんのCompat.jlの解説もとてもわかり易いです。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fbicycle1885%2Fitems%2F1c848fa3bdccfe20be73&quot; title=&quot;Juliaで異なるバージョンの差異を吸収する方法 - Qiita&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://qiita.com/bicycle1885/items/1c848fa3bdccfe20be73&quot;&gt;qiita.com&lt;/a&gt;&lt;/cite&gt;

なお、Juliaの複数環境の構築はsymbolic linkでjulia3, julia4, julia-devみたいなのを用意するのが良いです。 IJuliaも含めたやり方は以下に詳しいです。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fantimon2%2Fitems%2Fa8cd98257219773b9ef3&quot; title=&quot;Jupyter 環境設定補足 #pythontokai - Qiita&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://qiita.com/antimon2/items/a8cd98257219773b9ef3&quot;&gt;qiita.com&lt;/a&gt;&lt;/cite&gt;

ちなみに、Google codeが死亡したおかげでMeCabのソースがGoogle driveに移動したのですが、そのおかげでソースのファイル名を指定できないBinDeps.jlが死んだので初issueとPR投げました

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2FBinDeps.jl%2Fpull%2F178&quot; title=&quot;Add filename option for NetworkSource and RemoteBinaries by chezou · Pull Request #178 · JuliaLang/BinDeps.jl&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://github.com/JuliaLang/BinDeps.jl/pull/178&quot;&gt;github.com&lt;/a&gt;&lt;/cite&gt;

Juliaの困ったときは、以下に日本語でissue立ててもらうか[Slack](https://julia-tokyo-inviter.herokuapp.com/)で聞いてもらえると良いです！（めっちゃお世話になりました）

[JuliaTokyo/julia-wakalang · GitHub](https://github.com/JuliaTokyo/julia-wakalang)


