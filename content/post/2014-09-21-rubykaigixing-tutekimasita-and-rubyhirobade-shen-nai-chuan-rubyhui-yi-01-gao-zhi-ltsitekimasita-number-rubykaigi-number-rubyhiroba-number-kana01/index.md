---
title: "RubyKaigi行ってきました &amp; RubyHirobaで「神奈川Ruby会議01」告知LTしてきました #rubykaigi #rubyhiroba #kana01"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-09-21T22:07:11+00:00
lastmod: 2014-09-21T22:07:11+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
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

[slideshare id=39335806&doc=hiroba2014-140921015201-phpapp01]

- iruby notebookの紹介は東急できちんと準備してやりなおそうと思います
- [rubima](https://github.com/rubima/rubima/issues)にコミュニティ紹介の記事を書いて投稿するとよいと@muryoimplさんに言われました
- @beroberoさんの発表の質疑で、「何故数値計算にPythonなどではなくRubyを選んだんですか？」という質問が出てきたのを見て、なるほどこういう切り口もあるのかと思った。ちなみに、berobero氏曰くJuliaはSciRubyよりマシくらいな位置づけとのこと
- Railsガイドを翻訳している [@yasulab](https://twitter.com/yasulab) さんとお話出来てよかった。[gh-diff](https://github.com/melborne/gh-diff)の宣伝もしてきましたよ
- 悲しみのMagsafe2忘れ...

