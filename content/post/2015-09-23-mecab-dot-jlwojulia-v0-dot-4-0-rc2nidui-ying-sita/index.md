---
title: MeCab.jlをJulia v0.4.0-rc2に対応した
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2015-09-23 02:16:08+00:00
lastmod: 2015-09-23 02:16:08+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [julia, jl, pr, .com, github, ソース, issue, mecab, qiita, おかげ]
recommendations: [/post/2015-12-25-julia-tokyo-number-5wokai-cui-simasita-number-juliatokyo/,
  /post/2015-12-10-julianoqing-bao-woshou-ji-situdukeruniha/, /post/2014-12-03-juliahuan-jing-gou-zhu-2014-ver-number-julialang/]
---
ついに、Julia v0.4.0-rc2が2015/9/19出ましたね！ Dictの`[:symbol => :value]`といったsyntax sugarがなくなったりして、自分が作っているMeCab.jlでも対応をしました。

詳細はPRを見ていただければと思いますが、[Compat.jl](https://github.com/JuliaLang/Compat.jl)を使えば基本OKです。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fchezou%2FMeCab.jl%2Fpull%2F8" title="Suppress warnings on julia v0.4.0-rc2 by chezou · Pull Request #8 · chezou/MeCab.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/chezou/MeCab.jl/pull/8">github.com</a></cite>

（PRボロボロだったのであとから修正を加えました...）

bicycle1885さんのCompat.jlの解説もとてもわかり易いです。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fbicycle1885%2Fitems%2F1c848fa3bdccfe20be73" title="Juliaで異なるバージョンの差異を吸収する方法 - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://qiita.com/bicycle1885/items/1c848fa3bdccfe20be73">qiita.com</a></cite>

なお、Juliaの複数環境の構築はsymbolic linkでjulia3, julia4, julia-devみたいなのを用意するのが良いです。 IJuliaも含めたやり方は以下に詳しいです。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fantimon2%2Fitems%2Fa8cd98257219773b9ef3" title="Jupyter 環境設定補足 #pythontokai - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://qiita.com/antimon2/items/a8cd98257219773b9ef3">qiita.com</a></cite>

ちなみに、Google codeが死亡したおかげでMeCabのソースがGoogle driveに移動したのですが、そのおかげでソースのファイル名を指定できないBinDeps.jlが死んだので初issueとPR投げました

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2FBinDeps.jl%2Fpull%2F178" title="Add filename option for NetworkSource and RemoteBinaries by chezou · Pull Request #178 · JuliaLang/BinDeps.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/JuliaLang/BinDeps.jl/pull/178">github.com</a></cite>

Juliaの困ったときは、以下に日本語でissue立ててもらうか[Slack](https://julia-tokyo-inviter.herokuapp.com/)で聞いてもらえると良いです！（めっちゃお世話になりました）

[JuliaTokyo/julia-wakalang · GitHub](https://github.com/JuliaTokyo/julia-wakalang)


