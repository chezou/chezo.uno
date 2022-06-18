---
title: 'RubyKaigi行ってきました &amp; RubyHirobaで「神奈川Ruby会議01」告知LTしてきました #rubykaigi #rubyhiroba
  #kana01'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-09-21 22:07:11+00:00
lastmod: 2014-09-21 22:07:11+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [ruby, 数値計算, profile, '01', inside, julia, '2.1', よかっ, jekyll, android]
recommendations: [/post/2016-08-23-chuan-qi-rubyhui-yi-01wokai-cui-simasita-number-kwsk01/,
  /post/2013-10-06-kawasaki-dot-rb-number-003wokai-cui-simasita-number-kwskrb/, /post/2015-01-25-shen-nai-chuan-rubyhui-yi-wokai-cui-simasita-number-kana01/]
---
いっぱい面白い発表があったけど、諸般の事情により完結に

# RubyKaigi

- "Inside RubyMotion for Android"がやばかった。まさか、REPLを使ってAndroidのviewを動的に変更しているデモを見られるとは
- @tmm1氏の"Ruby 2.1 in Production"がとにかく"Profile! Profile! Profile!"ということで、Ruby2.1に上げるまでに徹底的にプロファイルツールを作成して遅いところを潰していく姿勢に会場とともにため息ばかりついた
- 須藤さんの"Three Ruby usages - High-level interface, Glue and Embedding - Inside Droonga"を聞いていると、GlueとしてのRubyをSWIG以外の方法でも触るべきだと感じた。JuliaはCしか叩けないけど、割りと楽なんだよな
- amaで@gogo\_tanakaさんの質問「数値計算にもRubyが盛り上がらないんですか？」の回答を聴くと、感覚が少しずれているなーと感じた。多分、ユーザがやりたいのは数値計算をして仕事をしたいのであって、数値計算ライブラリを作りたいわけではないという点に尽きるかなと。数式知らなくてもSVDしたい、みたいな
- 会期中に意識高まって、Juliaのpackageを2つリリースメール流した [★](https://groups.google.com/d/msg/julia-users/b4QvWps_7x4/6zdod5tXRT0J) [★](https://groups.google.com/d/msg/julia-users/YFN2v4C7URg/OgjNSvDILP0J)

  - ADAGrad.jlも実装していたけどDictとArrayどちらを使うべきかわからないので保留
- Ingressのagent各位ともっと交流すればよかった

# RubyHiroba

- 2015/1/17に開催する神奈川Ruby会議01の宣伝をしてきました
- 公式サイトは [http://kawasakirb.github.io/kana01/](http://kawasakirb.github.io/kana01/) です → [http://regional.rubykaigi.org/kana01/](http://regional.rubykaigi.org/kana01/) になりました

  - Jekyll in another Jekyll辛かったけど、会期中に解決できてよかった

<iframe src="//www.slideshare.net/slideshow/embed_code/key/FB5cOKqxtDfcLH" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/chezou/introduction-to-kanagawa-ruby" title="Introduction to Kanagawa Ruby Kaigi01 #kana01" target="_blank">Introduction to Kanagawa Ruby Kaigi01 #kana01</a> </strong> from <strong><a href="//www.slideshare.net/chezou" target="_blank">Aki Ariga</a></strong> </div>

- iruby notebookの紹介は東急できちんと準備してやりなおそうと思います
- [rubima](https://github.com/rubima/rubima/issues)にコミュニティ紹介の記事を書いて投稿するとよいと@muryoimplさんに言われました
- @beroberoさんの発表の質疑で、「何故数値計算にPythonなどではなくRubyを選んだんですか？」という質問が出てきたのを見て、なるほどこういう切り口もあるのかと思った。ちなみに、berobero氏曰くJuliaはSciRubyよりマシくらいな位置づけとのこと
- Railsガイドを翻訳している [@yasulab](https://twitter.com/yasulab) さんとお話出来てよかった。[gh-diff](https://github.com/melborne/gh-diff)の宣伝もしてきましたよ
- 悲しみのMagsafe2忘れ...

