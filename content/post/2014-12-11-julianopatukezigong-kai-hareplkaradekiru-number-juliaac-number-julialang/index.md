---
title: 'Juliaのパッケージ公開はREPLからできる #JuliaAC #julialang'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-12-11 00:00:00+00:00
lastmod: 2014-12-11 00:00:00+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [julia, pkg, jl, パッケージ, github, request, pull, ac, bicycle, '1885']
recommendations: [/post/2015-12-25-julia-tokyo-number-5wokai-cui-simasita-number-juliatokyo/,
  /post/2015-09-23-mecab-dot-jlwojulia-v0-dot-4-0-rc2nidui-ying-sita/, /post/2015-12-10-julianoqing-bao-woshou-ji-situdukeruniha/]
---
この記事は、[Julia Advent Calendar](http://qiita.com/advent-calendar/2014/julialang)の11日目の記事です。 10日目は夜道先生の[NumericExtensions.jl の話](http://yomichi.hateblo.jp/entry/2014/12/10/052839)でした。

Juliaのパッケージを作っても、野良パッケージを作るだけでは多くの人に使ってもらえません。 RでいうCRAN、Rubyでいうgemのように、Juliaでは[METADATA.jl](https://github.com/JuliaLang/METADATA.jl)というエコシステムでパッケージが管理されています。 パッケージはすべてgithub上ですべてホスティングされています。(だから、先日の[ロシアのgithubアクセス禁止騒ぎ](http://jp.techcrunch.com/2014/12/04/20141203github-russia/)みたいなのに巻き込まれると何も出来ません...) METADATA.jlもPull Requestベースで管理されているのですが、中身について議論されることはあまりなく、基本的に1日程度でどんどん取り込まれます。(CRANは厳正な審査がいるそうですね！)

また、パッケージをMETADATA.jlに登録すると[パッケージ検索ができるようになります](http://pkg.julialang.org/)。ちなみに、デイリーでstableとnightlyバージョンでテストがこけると[自動で斧が投げられる仕組み](https://github.com/chezou/MeCab.jl/issues/1)とかがあります。

さて、パッケージの作り方は[@bicycle1885](https://twitter.com/bicycle1885)さんの下記のJuliaTokyo #1のスライドが詳しいです。

<iframe src="https://www.slideshare.net/slideshow/embed_code/36649709" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Juliaのパッケージをつくろう!](https://www.slideshare.net/KentaSato/julia-36649709 "Juliaのパッケージをつくろう!")** from **[Kenta Sato](https://www.slideshare.net/KentaSato)** 

[Juliaのパッケージをつくろう!](http://www.slideshare.net/KentaSato/julia-36649709)

今日は、そこで検証されていなかったPkg.publish()についてご紹介したいと思います。 そもそも、この発表の段階ではGithubの[2 factor authに対応されていなかった](https://github.com/JuliaLang/julia/issues/5252)のですが、[少し前にできるようになりました](https://github.com/JuliaLang/julia/commit/a5b1f3066e62356bc59a2ca542358b620d6e0435)。

<script src="https://gist.github.com/c578aed2d97ed2634b5b.js"> </script>

[gistc578aed2d97ed2634b5b](https://gist.github.com/c578aed2d97ed2634b5b)

`Pkg.update()`して(この場合は更新なので)`Pkg.tag("PackageName")`して、`Pkg.publish()`するだけです。 初回はパスワードの入力とアクセストークンの入力が求められるので、[githubでtokenを生成して](https://github.com/settings/applications)REPLに入力をしましょう。

すると、自分のMETADATA.jlがbranch切られてpushされて、ブラウザが開いてPull Requestが作られます。(自分が試した時はChromeがちょうどクラッシュしたので、手でPR作りなおしたのでもしかするとMETADATA.jlのページが開くだけだったかもしれません)

![](/img/julia_ac_pkg_publish/20141207213426.png)

![](/img/julia_ac_pkg_publish/20141207213437.png)

最高便利！

明日はbicycle1885さんの「PythonistaのためのJulia100問100答」です。


