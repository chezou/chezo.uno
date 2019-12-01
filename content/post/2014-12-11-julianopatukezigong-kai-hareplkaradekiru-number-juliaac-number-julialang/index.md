---
title: "Juliaのパッケージ公開はREPLからできる #JuliaAC #julialang"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-12-11T00:00:00+00:00
lastmod: 2014-12-11T00:00:00+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
この記事は、[Julia Advent Calendar](http://qiita.com/advent-calendar/2014/julialang)の11日目の記事です。 10日目は夜道先生の[NumericExtensions.jl の話](http://yomichi.hateblo.jp/entry/2014/12/10/052839)でした。

Juliaのパッケージを作っても、野良パッケージを作るだけでは多くの人に使ってもらえません。 RでいうCRAN、Rubyでいうgemのように、Juliaでは[METADATA.jl](https://github.com/JuliaLang/METADATA.jl)というエコシステムでパッケージが管理されています。 パッケージはすべてgithub上ですべてホスティングされています。(だから、先日の[ロシアのgithubアクセス禁止騒ぎ](http://jp.techcrunch.com/2014/12/04/20141203github-russia/)みたいなのに巻き込まれると何も出来ません...) METADATA.jlもPull Requestベースで管理されているのですが、中身について議論されることはあまりなく、基本的に1日程度でどんどん取り込まれます。(CRANは厳正な審査がいるそうですね！)

また、パッケージをMETADATA.jlに登録すると[パッケージ検索ができるようになります](http://pkg.julialang.org/)。ちなみに、デイリーでstableとnightlyバージョンでテストがこけると[自動で斧が投げられる仕組み](https://github.com/chezou/MeCab.jl/issues/1)とかがあります。

さて、パッケージの作り方は[@bicycle1885](https://twitter.com/bicycle1885)さんの下記のJuliaTokyo #1のスライドが詳しいです。

&lt;iframe src=&quot;http://www.slideshare.net/slideshow/embed_code/36649709&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[Juliaのパッケージをつくろう!](https://www.slideshare.net/KentaSato/julia-36649709 &quot;Juliaのパッケージをつくろう!&quot;)** from **[Kenta Sato](http://www.slideshare.net/KentaSato)** 

[Juliaのパッケージをつくろう!](http://www.slideshare.net/KentaSato/julia-36649709)

今日は、そこで検証されていなかったPkg.publish()についてご紹介したいと思います。 そもそも、この発表の段階ではGithubの[2 factor authに対応されていなかった](https://github.com/JuliaLang/julia/issues/5252)のですが、[少し前にできるようになりました](https://github.com/JuliaLang/julia/commit/a5b1f3066e62356bc59a2ca542358b620d6e0435)。

&lt;script src=&quot;https://gist.github.com/c578aed2d97ed2634b5b.js&quot;&gt; &lt;/script&gt;

[gistc578aed2d97ed2634b5b](https://gist.github.com/c578aed2d97ed2634b5b)

`Pkg.update()`して(この場合は更新なので)`Pkg.tag(&quot;PackageName&quot;)`して、`Pkg.publish()`するだけです。 初回はパスワードの入力とアクセストークンの入力が求められるので、[githubでtokenを生成して](https://github.com/settings/applications)REPLに入力をしましょう。

すると、自分のMETADATA.jlがbranch切られてpushされて、ブラウザが開いてPull Requestが作られます。(自分が試した時はChromeがちょうどクラッシュしたので、手でPR作りなおしたのでもしかするとMETADATA.jlのページが開くだけだったかもしれません)

![f:id:chezou:20141207213426p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20141207/20141207213426.png &quot;f:id:chezou:20141207213426p:plain&quot;)

![f:id:chezou:20141207213437p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20141207/20141207213437.png &quot;f:id:chezou:20141207213437p:plain&quot;)

最高便利！

明日はbicycle1885さんの「PythonistaのためのJulia100問100答」です。

